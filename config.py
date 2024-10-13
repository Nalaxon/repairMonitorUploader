""" Configuration file, set your settings here"""

import sys

### configure here
# your language
LANG = 'de'
# Cell of REPAIR Date with Date Format(!), keep REPAIR_DATE = None if using this one
REPAIR_DATE_POSITION = {'column': 6, 'row':3}
# Start line from which to start consume data, set to None if you want to process whole file
PROCESS_FILE_START = 37
# End line until to consume data. If None and PROCESS_FILE_START ist set, only a this single line will be consumed
PROCESS_FILE_END = None

# time when repaire cafe took place, keept that 'None' if you use REPAIR_DATE_POSITION (please not the format: YYYY-MM-DD, e.g.: '2024-10-02')
REPAIR_DATE = None
# file you want to upload (expects full path if not in same folder
DATA_FILE_PATH = 'RepMon -DatenSource.xlsx'
# in excel file header starts in line skip_header
EXCEL_SKIP_HEADER=9
# save your excel into draft so you can review what the uploader created
OPERATION = 'Save+draft'



### do not edit below
INVALID_CONFIG = 1

languages_supported = ['en', 'de', 'nl', 'fr']

operations_supported = ['Save+draft', 'Complete+repair']

### check config
if LANG not in languages_supported:
    print("Invalid config: Language has to be one of: " + ','.join(languages_supported))
    sys.exit(INVALID_CONFIG)

if OPERATION not in operations_supported:
    print("Invalid config: Following operations allowed only: " + ','.join(languages_supported))
    sys.exit(INVALID_CONFIG)


if EXCEL_SKIP_HEADER <= 0:
    print("Invalid config: EXCEL_SKIP_HEADER requires to be an positiv number. 1 means no rows are skipped. Unless you really don't require any mapping you always need to skip at least one row!")
    sys.exit(INVALID_CONFIG)



if REPAIR_DATE is not None and ('column' in REPAIR_DATE_POSITION or 'row' in REPAIR_DATE_POSITION):
    print("Invalid config: Either use REPAIR_DATE to set a date, or use REPAIR_DATE_POSITION to specify the date within excel file")
    sys.exit(INVALID_CONFIG)

if PROCESS_FILE_START is not None and PROCESS_FILE_START is not PROCESS_FILE_END:
    print('PROCESS_FILE_END wasn\'t will only consume one line!')
    PROCESS_FILE_END = PROCESS_FILE_START + 1


def get_lang_specific(lang):
    '''Translate OPERATION to chosen LANG'''
    save_draft = {
        'en':'Save+draft',
        'de':'Konzept+speichern',
        'nl':'Bewaar+concept',
        'fr':'Sauvegarder+brouillon'
        }
    complete_repair = {
        'en':'Complete+repair',
        'de':'Reperatur+abschließen',
        'nl':'Reparatie+afronden',
        'fr':'Achever+la+réparation+'
        }
    return {'Save+draft':save_draft[lang], 'Complete+repair':complete_repair[lang]}
