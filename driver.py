""" programm entry point """

import config as conf
from rp_adapter import Repairmonitor
from excel_read import ExcelReader

rpa = Repairmonitor()
rpa.login_in()
data_reader = ExcelReader(conf)

for i, json in enumerate(data_reader.generate_json(rpa.get_add_repair_page_data)):
    print('process line ' + str(i))
    print(str(json))
    rpa.post_add_repair_with_data(conf.LANG, json)
