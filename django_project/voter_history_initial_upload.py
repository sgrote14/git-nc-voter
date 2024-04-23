"""
SCRIPT SUMMARY
    This script is used to upload new data to VoterHistory model
"""
import time
import django
import os
import pandas as pd

# Need help speeding this up!!!

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'django_project.settings')
django.setup()
from voter_profiles.models import RegisteredVotersActive, County, VoterHistory


# Accepts DF, dict (column: dtype),& default dtype. Returns new dict with specified dtypes + default for all DF columns.
def get_dtype_dict(dataframe, specified_dtypes, dtype):
    # Get all columns in the DataFrame
    all_columns = dataframe.columns

    # Create a dictionary with 'str' as default data type for columns not in specified_dtypes
    default_dtypes = {col: dtype for col in all_columns if col not in specified_dtypes}

    # Combine specified_dtypes with default_dtypes
    combined_dtypes = {**specified_dtypes, **default_dtypes}

    return combined_dtypes  #


# Creates required variables needed for every function.
file_path = '../../ncvhis_Statewide.txt'
df_sample = pd.read_csv(file_path, sep='\t', encoding='iso-8859-1', nrows=1)
dtype_dict = {'county_id': int}
dtype = 'str'
combined_dtypes = get_dtype_dict(df_sample, dtype_dict, dtype)
chunk_size = 100000
fk_dict = {
    'nc_id': {},
    'county_id': {county.pk: county for county in County.objects.all()}
} # I didn't do this for nc_id because that would require querying 8.5 million records
params = {
    'sep': '\t',
    'encoding': 'iso-8859-1',
    'dtype': dtype_dict,
    'parse_dates': ['election_lbl']
}  # Used in final function to help read file into DF correctly


def get_inst(fk_dictionary, key1, key2, model_class, **kwargs):
    try:
        instance = fk_dictionary[key1][key2]
    except:
        if key1 == 'nc_id':
            try:
                instance = model_class.objects.get(pk=key2)
                fk_dictionary[key1][key2] = instance
            except:
                instance = None
                print("Registered Voter does not exist!")
        else:
            instance = model_class.objects.get(pk=key2, **kwargs)
            instance.save()
            fk_dictionary[key1][key2] = instance

    return instance


def create_voter_hist_instance(file, chunks, **kwargs):
    counter = -1
    for chunk in pd.read_csv(file, chunksize=chunks, **kwargs):
        counter = counter + 1
        total_chunks = counter * chunks
        print(total_chunks)

        chunk.replace('nan', '', inplace=True)
        chunk.fillna('', inplace=True)

        instances = []

        for index, row in chunk.iterrows():
            reg_voter_inst = get_inst(fk_dict, 'nc_id', row['ncid'], RegisteredVotersActive)
            county_id_inst = get_inst(fk_dict, 'county_id', row['county_id'], County, county_name=row['county_desc'])
            if reg_voter_inst is None:
                print("No active registered voter")
            else:
                model_instance = VoterHistory(
                    reg_voter=reg_voter_inst,
                    county_id=county_id_inst,
                    voter_registration_num=row['voter_reg_num'],
                    election_date=row['election_lbl'],
                    election_description=row['election_desc'],
                    voting_method=row['voting_method'],
                    voted_party=row['voted_party_cd'],
                    precinct_abbreviation=row['pct_label'],
                    voted_county_id=row['voted_county_id'],
                    voted_district_label=row['vtd_label']
                )
                instances.append(model_instance)
        VoterHistory.objects.bulk_create(instances)


create_voter_hist_instance(file_path, chunk_size, **params)
