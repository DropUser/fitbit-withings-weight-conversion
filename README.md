# fitbit-withings-weight-conversion
A simple Python script to convert a Fitbit Account Archive into a set of CSV files to be imported within the Withings Healthmate App

To use this script, follow the below steps
1. Create and download your Fitbit data export at https://www.fitbit.com/settings/data/export
2. Extract the archive to a known location
3. The weight data should be located under "FirstNameLastName\Personal & Account"
4. Execute script
5. Enter source data folder and location where you wish to output the result.
6. Go to your Withings web dashboard at https://healthmate.withings.com/
7. Click the arrow in the upper right hand corner and select Settings
8. Choose your profile
9. Select Import My Data under Manage My Data
10. Select Choose File under Weight and select the first output .csv file
11. Select save and check "Ok" when it asks if you are sure, this can take a few minutes
12. Page will eventually refresh and data will be uploaded, do this for each output file
