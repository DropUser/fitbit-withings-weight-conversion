# fitbit-withings-weight-conversion
A simple Python script to convert a Fitbit Account Archive into a set of CSV files to be imported within the Withings Healthmate App

This script requires Python 3.5+ and Pandas

To use this script, follow the below steps
2. Create and download your Fitbit data export at https://www.fitbit.com/settings/data/export
3. Extract the archive to a known location
4. The weight data should be located under "FirstNameLastName\Personal & Account"
5. Execute script
6. Enter source data folder and location where you wish to output the result.
7. Go to your Withings web dashboard at https://healthmate.withings.com/
8. Click the arrow in the upper right hand corner and select Settings
9. Choose your profile
10. Select Import My Data under Manage My Data
11. Select Choose File under Weight and select the first output .csv file
12. Select save and check "Ok" when it asks if you are sure, this can take a few minutes
13. Page will eventually refresh and data will be uploaded, do this for each output file
