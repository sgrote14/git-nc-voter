"""
SCRIPT SUMMARY
    Checks NC BoE website for new data on registered voters. If new data is found, it will update Voter File table
    and then call function to update registered voter table.
"""

from datetime import datetime
import pytz
import django
import os
import requests
import xml.etree.ElementTree as ET

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'django_project.settings')
django.setup()
from voter_profiles.models import RegVoterFile, VoterHistoryFile

# Step one is to make a request to the URL and Soupify content
reg_voter_url = 'https://s3.amazonaws.com/dl.ncsbe.gov/data/ncvoter_Statewide.zip'
vot_history_url = 'https://s3.amazonaws.com/dl.ncsbe.gov/data/ncvhis_Statewide.zip'

reg_voter_response = requests.get(reg_voter_url)
vot_history_response = requests.get(vot_history_url)


def new_file_check(response, model_class):
    if response.status_code == 200:

        last_mod_date_str = response.headers['Last-Modified']
        last_mod_date = datetime.strptime(last_mod_date_str, '%a, %d %b %Y %H:%M:%S %Z')
        last_mod_date = last_mod_date.replace(tzinfo=pytz.utc)

        latest_df_file = model_class.objects.order_by('-file_date').first()
        if latest_df_file is None:
            print('There are no existing files')
        else:
            if last_mod_date > latest_df_file.file_date:
                print('There are new files. Trigger upload process')
            else:
                print("No new files")

    else:
        print(f"Request failed. HTTP status code: {response.status_code}")


new_file_check(reg_voter_response, RegVoterFile)
new_file_check(vot_history_response, VoterHistoryFile)

# Next Steps
# 1. Call function to upload data to Registered Voters table
# 2. Clean up the code
