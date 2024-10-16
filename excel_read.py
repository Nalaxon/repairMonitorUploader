""" Reads form excel
and uses excel_adapter to translate from your data to repair monitor required data """
import pandas as pd
import excel_adapter as ea
from excel_adapter import mapping

# def get(row, field_key):
#         mapped_key = mapping.get(field_key)
#         row_"value" = row[mapped_key]
#         adapter_func = adapter.get(field_key)
#         result_"value" = adapter_func(row_"value")
#         return result_"value"

class ExcelReader:
    """ Reads data from excel an transforms it with excel_adapter to repair monitor format """

    def __init__(self, config):
        self.df = None
        self.lang = config.LANG
        self.lang_specific = config.get_lang_specific(config.LANG)
        self.df = pd.read_excel(config.DATA_FILE_PATH, header=config.EXCEL_SKIP_HEADER -1)
        self.df = self.df.dropna(subset=[mapping.get('field_reference_number')])
        self.loop_start = config.PROCESS_FILE_START
        if config.PROCESS_FILE_START is not None:
            self.loop_start -= config.EXCEL_SKIP_HEADER
        self.loop_end = config.PROCESS_FILE_END
        if config.PROCESS_FILE_END is not None:
            self.loop_end -= config.EXCEL_SKIP_HEADER -1
        if config.REPAIR_DATE is not None:
            self.repair_date = config.REPAIR_DATE
        else:
            row = config.REPAIR_DATE_POSITION['row']
            column = config.REPAIR_DATE_POSITION['column']
            repair_date = pd.read_excel(config.DATA_FILE_PATH, dtype=str, keep_default_na=False).iat[row-2, column-1]
            self.repair_date = repair_date[:10]
        print('Repair date: ' + str(self.repair_date))
  
        self.operation = config.OPERATION

    def generate_json(self, get_page_data):
        ''' Returns repair monitor format aka json form blob '''
        for i, row in self.df.iterrows():

            
            if self.loop_start is not None and i < self.loop_start -1:
                continue
            if self.loop_end is not None and i == self.loop_end-1:
                break

            print(f'generate_json: {i} : {self.loop_start} - {self.loop_end}')
            page_data = get_page_data()
            template_op = self.lang_specific[self.operation]
            template_date = self.repair_date

            yield {
                'changed':page_data['changed'], #1713118290,
                'field_repair_date[0][value]':template_date, #'2024-04-14',
                 #'form-sepwkqBXhiMS6Jk85kN_y-vJNYw76MpaUamlsrBDSAM',
                'form_build_id':page_data['form_build_id'],
                #'dkg-qmxcaZptzt25m8VjSjEU4yDB4xYL7w10zYnjyEM,
                'form_token': page_data['form_token'],
                'form_id':'node_repair_form',
                'field_reference_number[0][value]':int(row[mapping['field_reference_number']]), #1,
                #'Battery+tester',
                'field_kind_product[0][target_id]':row[mapping['field_kind_product_target_id']],
                'field_kind_product[0][kp_other]':'',
                #row[mapping['field_brand_target_id']], #'Philips',
                'field_brand[0][autocomplete_fill_field]':'',
                #1685,
                'field_categorie': page_data['field_categorie'][row[mapping['field_categorie']]],
                #row[mapping['field_kind_product_target_id']], #'Battery+tester'
                'field_kind_product[0][autocomplete_fill_field]':'',
                'field_brand[0][target_id]':row[mapping['field_brand_target_id']], #'Philips',
                'field_brand[0][other]':'',
                #'',
                'field_product_buildyear[0][value]':str(ea.get_or_blank(row,mapping['field_product_buildyear'])).split('.', maxsplit=1)[0],
                'field_model[0][target_id]':ea.get_or_blank(row,mapping['field_model']), #'',
                'field_cause_of_fault[0][value]':row[mapping['field_cause_of_fault']], # ''
                'field_repairer[0][target_id]':row[mapping['field_repairer']], #'',
                'field_fault[0][value]':row[mapping['field_fault']], #'',
                #'yes', : 'half', 'no'
                'field_product_repaired':ea.product_repaired_from_key(row[mapping['field_product_repaired']]),
                'field_solution[0][value]':ea.get_or_blank(row,mapping['field_solution']), #'',
                #'_none'
                'field_repair_failed':ea.field_repair_failed_adapter(page_data['field_repair_failed'], ea.get_or_none(row,mapping['field_repair_failed']), '_none'),
                'field_advice[0][value]':'',
                'field_repair_information':ea.field_repair_information_adapter(row[mapping['field_repair_information']], self.lang),
                'field_repair_source[0][value]':ea.get_or_blank(row,mapping['field_repair_source']), #'',
                'field_hint[0][value]':ea.get_or_blank(row,mapping['field_hint']), #'',
                'op':template_op, #'Save+draft',
                'advanced__active_tab':'edit-revision-information'
        }



# {
# 	"changed": "1714568734",
# 	"field_repair_date[0]["value"]": "2024-05-01",
# 	"form_build_id": "form-Eidjj3ivzJ8Fdyo_P1-srOlQ9doyP1AA10lnrsoZM2Y",
# 	"form_token": "4mcGyUYbshNyZ0_9CXZlcd3tkhCSgZ0zSxVphE524e0",
# 	"form_id": "node_repair_form",
# 	"field_reference_number[0]["value"]": "1",
# 	"field_kind_product[0][target_id]": "Weihwasserfass",
# 	"field_kind_product[0][kp_other]": "",
# 	"field_brand[0][autocomplete_fill_field]": "KTM",
# 	"field_categorie": "1679",
# 	"field_kind_product[0][autocomplete_fill_field]": "Weihwasserfass",
# 	"field_brand[0][target_id]": "KTM",
# 	"field_brand[0][other]": "",
# 	"field_product_buildyear[0]["value"]": "1967",
# 	"field_model[0][target_id]": "FX-4589",
# 	"field_cause_of_fault[0]["value"]": "Hecheinschwerfer+defekt",
# 	"field_repairer[0][target_id]": "werner",
# 	"field_fault[0]["value"]": "Scheinwerfer+defekt",
# 	"field_product_repaired": "yes", "half", "no"
# 	"field_solution[0]["value"]": "Scheinwerfer+getauscht",
# 	"field_repair_failed": "_none",
# 	"field_advice[0]["value"]": "",
# 	"field_repairability": "2",
# 	"field_repair_information": "yes", "no" (nicht gefunden), "unknown" (nicht gesucht)
# 	"field_repair_information_resourc": "supplier", "user" (kollege)
# 	"field_repair_source[0]["value"]": "quelle+reperatur-info",
# 	"field_hint[0]["value"]": "wer+anders+hat+auch+geholfen",
# 	"op": "Konzept+speichern",
# 	"advanced__active_tab": "edit-revision-information"
# }
