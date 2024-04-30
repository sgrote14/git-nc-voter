"""
SCRIPT SUMMARY
    This script is used to upload new data to Registered Voters database.
"""
import time
import django
import os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'django_project.settings')
django.setup()
from voter_profiles.models import *


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
file_path = '../../ncvoter_Statewide.txt'
df_sample = pd.read_csv(file_path, sep='\t', encoding='iso-8859-1', nrows=1)
dtype_dict = {'county_id': int, 'birth_year': int}
dtype = 'str'
combined_dtypes = get_dtype_dict(df_sample, dtype_dict, dtype)
chunk_size = 1000
file_inst = RegVoterFile.objects.get(pk=1)
start_date = RegVoterFile.objects.get(pk=1).file_date
fk_dict = {
    'county_id': {county.pk: county for county in County.objects.all()},
    'status_code': {status.pk: status for status in StatusCode.objects.all()},
    'status_reason': {reason.pk: reason for reason in StatusReason.objects.all()},
    'race_code': {race.pk: race for race in RaceCode.objects.all()},
    'ethnic_code': {ethnic.pk: ethnic for ethnic in EthnicityCode.objects.all()},
    'party_code': {party.pk: party for party in PartyCode.objects.all()},
    'gender_code': {gender.pk: gender for gender in GenderCode.objects.all()},
}  # Create dictionary of objects for all foreign keys in registered model (to optimize DB queries)
params = {
    'sep': '\t',
    'encoding': 'iso-8859-1',
    'dtype': combined_dtypes,
    'parse_dates': ['registr_dt']
}  # Used in final function to help read file into DF correctly


def get_inst(fk_dictionary, key1, key2, model_class, **kwargs):
    try:
        instance = fk_dictionary[key1][key2]
    except:
        instance = model_class(pk=key2, **kwargs)
        instance.save()
        fk_dictionary[key1][key2] = instance

    return instance


def create_voter_instance(file, chunks, **kwargs):
    counter = -1
    for chunk in pd.read_csv(file, chunksize=chunks, **kwargs):
        counter = counter + 1
        total_chunks = counter * chunks
        print(total_chunks)

        chunk.replace('nan', '')
        chunk.fillna('', inplace=True)

        instances = []

        for index, row in chunk.iterrows():
            county_id_inst = get_inst(fk_dict, 'county_id', row['county_id'], County, county_name=row['county_desc'])
            status_code_inst = get_inst(fk_dict, 'status_code', row['status_cd'], StatusCode,
                                        status_desc=row['voter_status_desc'])
            status_reason_inst = get_inst(fk_dict, 'status_reason', row['reason_cd'], StatusReason,
                                          status_reason_desc=row['voter_status_reason_desc'])
            race_code_inst = get_inst(fk_dict, 'race_code', row['race_code'], RaceCode)
            ethnic_code_inst = get_inst(fk_dict, 'ethnic_code', row['ethnic_code'], EthnicityCode)
            party_code_inst = get_inst(fk_dict, 'party_code', row['party_cd'], PartyCode)
            gender_code_inst = get_inst(fk_dict, 'gender_code', row['gender_code'], GenderCode)
            model_instance = RegisteredVotersActive(
                # all non-foreign keys
                nc_id=row['ncid'],
                voter_registration_number=row['voter_reg_num'],
                start_date=start_date,
                first_name=row['first_name'],
                middle_name=row['middle_name'],
                last_name=row['last_name'],
                name_suffix=row['name_suffix_lbl'],
                street_address=row['res_street_address'],
                city=row['res_city_desc'],
                zip_code=row['zip_code'],
                state=row['state_cd'],
                mail_address_1=row['mail_addr1'],
                mail_address_2=row['mail_addr2'],
                mail_address_3=row['mail_addr3'],
                mail_address_4=row['mail_addr4'],
                mail_city=row['mail_city'],
                mail_state=row['mail_state'],
                mail_zip_code=row['mail_zipcode'],
                phone_number=row['full_phone_number'],
                registration_date=row['registr_dt'],
                birth_year=row['birth_year'],
                birth_state=row['birth_state'],
                drivers_license=row['drivers_lic'],
                congress_dist_abbreviation=row['cong_dist_abbrv'],
                superior_court_abbreviation=row['super_court_abbrv'],
                judicial_dist_abbreviation=row['judic_dist_abbrv'],
                nc_senate_abbreviation=row['nc_senate_abbrv'],
                nc_house_abbreviation=row['nc_house_abbrv'],
                precinct_abbreviation=row['precinct_abbrv'],
                precinct_desc=row['precinct_desc'],
                municipality_abbreviation=row['municipality_abbrv'],
                municipality_desc=row['municipality_desc'],
                ward_abbreviation=row['ward_abbrv'],
                ward_desc=row['ward_desc'],
                county_comm_abbreviation=row['county_commiss_abbrv'],
                county_comm_desc=row['county_commiss_desc'],
                township_abbreviation=row['township_abbrv'],
                township_desc=row['township_desc'],
                school_dist_abbreviation=row['school_dist_abbrv'],
                school_dist_desc=row['school_dist_desc'],
                fire_dist_abbreviation=row['fire_dist_abbrv'],
                fire_dist_desc = row['fire_dist_desc'],
                water_dist_abbreviation=row['water_dist_abbrv'],
                water_dist_desc = row['water_dist_desc'],
                sewer_dist_abbreviation=row['sewer_dist_abbrv'],
                sewer_dist_desc = row['sewer_dist_desc'],
                sanitation_dist_abbreviation=row['sanit_dist_abbrv'],
                sanitation_dist_desc = row['sanit_dist_desc'],
                rescue_dist_abbreviation=row['rescue_dist_abbrv'],
                rescue_dist_desc = row['rescue_dist_desc'],
                municipal_dist_abbreviation=row['munic_dist_abbrv'],
                municipal_dist_desc = row['munic_dist_desc'],
                prosecutorial_dist_abbreviation=row['dist_1_abbrv'],
                prosecutorial_dist_desc = row['dist_1_desc'],
                voter_tab_dist_abbreviation=row['vtd_abbrv'],
                voter_tab_dist_desc = row['vtd_desc'],
                # all foreign keys
                county_id=county_id_inst,
                status_code=status_code_inst,
                status_reason_code=status_reason_inst,
                race_code=race_code_inst,
                ethnicity_code=ethnic_code_inst,
                party_code=party_code_inst,
                gender_code=gender_code_inst,
                file_id=file_inst
                # using the below as a placeholder for now...will need to capture it from the voter_file_check script
            )
            instances.append(model_instance)
        RegisteredVotersActive.objects.bulk_create(instances)


create_voter_instance(file_path, chunk_size, **params)
