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
from voter_profiles.models import VoterFile

# Step one is to make a request to the URL and Soupify content
url = 'https://s3.amazonaws.com/dl.ncsbe.gov?delimiter=/&prefix=data/'
response = requests.get(url)

# parse using xml library, find target file and extract last modified date
if response.status_code == 200:
    xml_content = response.text
    tree = ET.ElementTree(ET.fromstring(xml_content))
    root = tree.getroot()

    namespace = {'s3': 'http://s3.amazonaws.com/doc/2006-03-01/'}
    contents = root.findall('s3:Contents', namespace)

    target_file = 'data/ncvoter_Statewide.zip'
    last_file = contents[-1]
    last_file_name = last_file.find('s3:Key', namespace).text

    # I believe it's always the last file so using this if/else statement to avoid looping
    if last_file_name == target_file:
        last_mod_date = last_file.find('s3:LastModified', namespace).text
        print(last_file_name, last_mod_date)
    else:
        for content in contents:
            file_name = content.find('s3:Key', namespace).text
            if file_name == 'data/ncvoter_Statewide.zip':
                last_mod_date = content.find('s3:LastModified', namespace).text
                print(file_name, last_mod_date)
            else:
                print("Script failed")
                continue
else:
    print(f'Failed to fetch the xml file. HTTP Status code: {response.status_code}')

most_recent_file = VoterFile.objects.order_by('-file_date').first()
print(most_recent_file)

date_time_object = datetime.strptime(last_mod_date, '%Y-%m-%dT%H:%M:%S.%fZ').astimezone(
    pytz.timezone('America/New_York'))
if date_time_object > most_recent_file.file_date:
    print("We have a new file!")
else:
    print("We don't have a new file")

# Next Steps
# 1. Upload data to VoterFile table
# 2. Call function to upload data to Registered Voters table
# 3. Clean up the code
