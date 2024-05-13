# Repair Monitor Uploader
An python script that allows you to upload excel sheets (xlsx, in the following spread sheet) automatically to repairmonitor.org

# How to use

## Run Linux / Mac / Windows
4. Run in terminal: `pipenv exec python driver.py`
This will upload `RepMon -DataSource.xlsx` to repairmonitor.org as the user given in `.credentials/auth.yml` with the date given in 

## Adopt mapping
The file excel_adapter.py includes a mapping of your excel column names and the internal names.
Make the right  (after the `:`) fit your column names

## Adopt adapters
The file excel_adapter.py includes adapter functions that allow you to transform values of you spread sheet to fit the needed values for repairmonitor.org
The needed values are part of the documentation of each adapter function.

# Setup
See Requirements below!
1. Edit config.yaml to use either de, en, fr, nl
2. Add your password + user name to .credentials/auth.yml
3. Run in terminal: `pipenv install`
4. Provide spread sheet
5. Adopt mapping (see below)
5. Adopt adapters (see below)

# Requirements
* Python3
* pipenv
* spread sheet File including following information:
  * Reference number
  * Kind of product
  * Category
  * Barnd
  * Year of production
  * Model, type number and/or serial number
  * Problem description + probably cause
  * Repairer
  * Defect found
  * Repair status (repaird, not/half repaird)
  * Additional information on repair (what did you repair, why didn't you repair)
  * reparability (optional)
  * information used (yes, no)
  * Information Link if used
  * Information source if used
  * Suggestions for other repairers

# Help
* To get help with the usage please use conversesion
* If you find bugs please report them as issues
* If you wanna help please issue an PR

# Thanks
To Werner Valeskine and Reapair Café Voitsberg to provide data source.