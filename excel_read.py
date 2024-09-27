import pandas
from excel_adapter import mapping, product_repaired_from_key, field_repair_failed_adapter, getOrNone, getOrBlank, field_repair_information_adapter

# def get(row, field_key):
#         mapped_key = mapping.get(field_key)
#         row_"value" = row[mapped_key]
#         adapter_func = adapter.get(field_key)
#         result_"value" = adapter_func(row_"value")
#         return result_"value"

class Excel_Reader:

        def __init__(self, config):
                self.df = None
                self.lang = config.lang
                self.lang_specific = config.get_lang_specific(config.lang)
                self.df = pandas.read_excel(config.data_file_path, header=config.excel_skip_header)
                self.df = self.df.dropna(subset=[mapping.get('field_reference_number')])
                self.repair_date = config.repair_date
                self.operation = config.operation

        def generate_json(self, get_page_data):
                for index, row in self.df.iterrows():
                        page_data = get_page_data(self.lang)
                        template_op = self.lang_specific[self.operation]
                        template_date = self.repair_date
                        # print(str(mapping['field_repair_failed']) + ':' + str(row.get(mapping['field_repair_failed'])) + ':')
                        # print(str(field_repair_failed_adapter(page_data['field_repair_failed'], get(row,mapping['field_repair_failed']), '_none')))
                        # yield {
                        #         mapping['field_reference_number']:row.get(mapping['field_reference_number']),
                        #         mapping['field_kind_product_target_id']:row.get(mapping['field_kind_product_target_id']),
                        #         mapping['field_brand_target_id']:row.get(mapping['field_brand_target_id']),
                        #         mapping['field_categorie']:row.get(mapping['field_categorie']),
                        #         mapping['field_product_buildyear']:getOrBlank(row,mapping['field_product_buildyear']),
                        #         mapping['field_model']:getOrBlank(row,mapping['field_model']),
                        #         mapping['field_cause_of_fault']:row.get(mapping['field_cause_of_fault']),
                        #         mapping['field_repairer']:row.get(mapping['field_repairer']),
                        #         mapping['field_fault']:row.get(mapping['field_fault']),
                        #         mapping['field_product_repaired']:product_repaired_from_key(row[mapping['field_product_repaired']]),
                        #         mapping['field_solution']:getOrBlank(row,mapping['field_solution']),
                        #         mapping['field_repair_failed']:field_repair_failed_adapter(page_data['field_repair_failed'], getOrNone(row, mapping['field_repair_failed']), '_none'),
                        #         mapping['field_repair_source']:getOrBlank(row,mapping['field_repair_source']),
                        #         mapping['field_hint']:getOrBlank(row,mapping['field_hint'])
                        # }
                        yield {
                                'changed':page_data['changed'], #1713118290,
                                'field_repair_date[0][value]':template_date, #'2024-04-14',
                                'form_build_id':page_data['form_build_id'], #'form-sepwkqBXhiMS6Jk85kN_y-vJNYw76MpaUamlsrBDSAM',
                                'form_token': page_data['form_token'], #'dkg-qmxcaZptzt25m8VjSjEU4yDB4xYL7w10zYnjyEM,
                                'form_id':'node_repair_form',
                                'field_reference_number[0][value]':int(row[mapping['field_reference_number']]), #1,
                                'field_kind_product[0][target_id]':row[mapping['field_kind_product_target_id']], #'Battery+tester',
                                'field_kind_product[0][kp_other]':'',
                                'field_brand[0][autocomplete_fill_field]':'',#row[mapping['field_brand_target_id']], #'Philips',
                                'field_categorie': page_data['field_categorie'][row[mapping['field_categorie']]], #1685,
                                'field_kind_product[0][autocomplete_fill_field]':'',#row[mapping['field_kind_product_target_id']], #'Battery+tester'
                                'field_brand[0][target_id]':row[mapping['field_brand_target_id']], #'Philips',
                                'field_brand[0][other]':'',
                                'field_product_buildyear[0][value]':str(getOrBlank(row,mapping['field_product_buildyear'])).split('.')[0], #'',
                                'field_model[0][target_id]':getOrBlank(row,mapping['field_model']), #'',
                                'field_cause_of_fault[0][value]':row[mapping['field_cause_of_fault']], # ''
                                'field_repairer[0][target_id]':row[mapping['field_repairer']], #'',
                                'field_fault[0][value]':row[mapping['field_fault']], #'',
                                'field_product_repaired':product_repaired_from_key(row[mapping['field_product_repaired']]), #'yes', : 'half', 'no'
                                'field_solution[0][value]':getOrBlank(row,mapping['field_solution']), #'',
                                'field_repair_failed':field_repair_failed_adapter(page_data['field_repair_failed'], getOrNone(row,mapping['field_repair_failed']), '_none'), #'_none'
                                'field_advice[0][value]':'',
                                'field_repair_information':field_repair_information_adapter(row[mapping['field_repair_information']], self.lang),
                                'field_repair_source[0][value]':getOrBlank(row,mapping['field_repair_source']), #'',
                                'field_hint[0][value]':getOrBlank(row,mapping['field_hint']), #'',
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