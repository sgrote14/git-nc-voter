# nc_voter_data

This is a web application that provides information and statistics on registered voters in North Carolina. Voter data will come from the NC BOE and the application will be built using the Django framework.

**NC BOE Datasets**

1. NC Registered Voters
    - Contains all legally available voter specific information 
    - Checking here for updates: https://dl.ncsbe.gov/?prefix=data/
      - Source file: https://s3.amazonaws.com/dl.ncsbe.gov/data/ncvoter_Statewide.zip
    - Seems to be updated on a weekly basis

2. Party Change List
    - Includes voter_reg_num and what party they switched to and from and when 
    - CSV file that is a running total for the calendar year
      - https://s3.amazonaws.com/dl.ncsbe.gov/data/PartyChange/2024_party_change_list.csv
    - This will be used as an initial data dump to provide the initial historical data…but once this app is live, we will be capturing these party changes in the “NC Registered Voters” files

3. NC Voter History
   - Information on how registered voters have voted for the last 10 years

**Applications**
1. NC Snapshot and Trends
    - Aggregate Registration by Party data 
      - By state and by individual counties 
      - Additional filters: zip code, race, ethnicity, age, gender, etc. 
      - Trend Analytics (change over the last 1yr, 6m, 3m)
2. Individual Voter Profiles 
   - See voter information and history 
   - Add notes
3. Voter Groupings
   - Voters that left the party (DEM to anything)
   - Voters that just came to the party (anything to DEM)
   - Voters that left the REP party (REP to UNA)
   - Consistent Voters 
   - Inconsistent Voters 
   - Ability to export this data

**Data Model**

- Upload initial voter data to “Current Voter Registration Data” table (primary data table)
    - Set Start Date == File Date (this is when this data was first captured)
    - Set End Date to Null (this data is still valid)
- When new voter data is uploaded by NC BOE, we follow this process:
   - Check for changes with the “Current Voter Registration Data” table:
     - New Voter is identified by a new “NC ID” being found 
         - Record gets added to “Current Voter Registration Data” table following same logic as initial upload (start date == file data & end date is null)
     - Removed Voter identified by missing record with current NC ID 
         - Set End Date == File Data (this data is no longer valid as of this date)
     - Changed Voter is identified by matching NC ID’s and then checking for any field changes 
         - Old record will have End Date == File Date (no longer valid)
         - New record added with start date == file date & end date == null
  




