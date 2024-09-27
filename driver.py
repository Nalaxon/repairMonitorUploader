import config as config
from rp_adapter import Repairmonitor
from excel_read import Excel_Reader

# ### do not edit
# languages_supported = ['en', 'de', 'nl', 'fr']

# ### config do edit
# lang = 'de'
# # e.g. windwos absolut path C:\users\Nalaxon\RepMon -DataSource.xlsx
# # e.g.: wsl absolut path /c/users/Nalaxon/RepMon\ -DataSource.xlsx
# data_file_path = 'RepMon -DatenSource.xlsx' # file in same directory

# # in excel file header starts in line skip_header
# excel_skip_header=8
# ### end config

### check config
# if (lang not in languages_supported):
#         print("language has to be one of: " + ','.join(languages_supported))

# def get_lang_specific(lang):
#         save_draft = {'en':'Save+draft', 'de':'Konzept+speichern', 'nl':'Bewaar+concept', 'fr':'Sauvegarder+brouillon'}
#         complete_repair = {'en':'Complete+repair', 'de':'Reperatur+abschließen', 'nl':'Reparatie+afronden', 'fr':'Achever+la+réparation+'}
#         return {'Save+draft':save_draft[lang], 'Complete+repair':complete_repair[lang]}


rpa = Repairmonitor()
rpa.login_in()
data_reader = Excel_Reader(config)

for i, json in enumerate(data_reader.generate_json(rpa.get_add_repair_page_data)):
        print('process line ' + str(i))
        print(str(json))
        rpa.post_add_repair_with_data(config.lang, json)
