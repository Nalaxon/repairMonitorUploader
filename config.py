""" Configuration file, set your settings here"""

### configure here
# your language
LANG = 'de'
# time when repaire cafe took place (please not the format: YYYY-MM-DD)
REPAIR_DATE = '2024-05-09'
# file you want to upload (expects full path if not in same folder
DATA_FILE_PATH = 'RepMon -DatenSource.xlsx'
# in excel file header starts in line skip_header
EXCEL_SKIP_HEADER=8
# save your excel into draft so you can review what the uploader created
OPERATION = 'Save+draft'



### do not edit below
languages_supported = ['en', 'de', 'nl', 'fr']

operations_supported = ['Save+draft', 'Complete+repair']

### check config
if LANG not in languages_supported:
    print("language has to be one of: " + ','.join(languages_supported))

if OPERATION not in operations_supported:
    print("Following operations allowed only: " + ','.join(languages_supported))


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
