# real-estate-sqlite

## PROJECT (for SLHSCS-2022) : Appraisal Data Import 

### create_database.py
* Using the PDF file, create a script that will build the table 'prop' that will hold all data from the 'PROP.TXT' file.
* All numeric values are integers and date fields are strings.
* Dates will be converted when inserted below.
* You do not have to load all 400_ fields from the PDF file. Start with 'prop_id' and end with 'land_acres'.
* Any fields named 'filler' are skipped.
* This script should delete the 'prop' table if it exists prior to rebuilding.

### import_data.py
* Load the data from 'PROP_10000.TXT' into the database.
* There is also a 'PROP_10.TXT' file with just the first 10 records to use for testing, but the created table will hold all 10000 records from 'PROP_10000.TXT'.
* Any date fields must be converted from the format "MM-DD-YYYY" to the ISO-8601 "YYYY-DD-MM" when stored in the SQLite database.
  
