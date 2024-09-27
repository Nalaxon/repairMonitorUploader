### configure here
# your language
lang = 'de'
# time when repaire cafe took place (please not the format: YYYY-MM-DD)
repair_date = '2024-05-09'
# file you want to upload (expects full path if not in same folder
data_file_path = 'RepMon -DatenSource.xlsx'
# in excel file header starts in line skip_header
excel_skip_header=8
# save your excel into draft so you can review what the uploader created
operation = 'Save+draft'



### do not edit below
languages_supported = ['en', 'de', 'nl', 'fr']

### check config
if (lang not in languages_supported):
        print("language has to be one of: " + ','.join(languages_supported))


def get_lang_specific(lang):
        save_draft = {'en':'Save+draft', 'de':'Konzept+speichern', 'nl':'Bewaar+concept', 'fr':'Sauvegarder+brouillon'}
        complete_repair = {'en':'Complete+repair', 'de':'Reperatur+abschließen', 'nl':'Reparatie+afronden', 'fr':'Achever+la+réparation+'}
        return {'Save+draft':save_draft[lang], 'Complete+repair':complete_repair[lang]}