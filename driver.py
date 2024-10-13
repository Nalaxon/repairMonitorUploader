""" programm entry point """

import config as conf
from rp_adapter import Repairmonitor
from excel_read import ExcelReader

rpa = Repairmonitor(conf.LANG)
rpa.login_in()
data_reader = ExcelReader(conf)

for i, json in enumerate(data_reader.generate_json(rpa.get_add_repair_page_data)):
    print('process line ' + str(i +1))
    print(str(json))
    rpa.post_add_repair_with_data(json)

rpa.verify_upload()
