""" Configuration file, set your settings here"""

import sys

### configure here
# your language
LANG = 'de'
# time when repaire cafe took place (please not the format: YYYY-MM-DD)
REPAIR_DATE = '2024-05-09'
# file you want to upload (expects full path if not in same folder
DATA_FILE_PATH = 'RepMon -DatenSource2.xlsx'
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
