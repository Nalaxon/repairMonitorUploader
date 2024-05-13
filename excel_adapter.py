mapping = {
        'field_reference_number': 'Nr. 2)',
        'field_kind_product_target_id':'Produkt 3)',
        'field_brand_target_id':'Marke 5)',
        'field_categorie':'Kategorie',
        'field_product_buildyear':'Prod.-Jahr 6)',
        'field_model':'Modell/Typ/Serien-nummer 7)',
        'field_cause_of_fault':'Problem/Ursache 8)',
        'field_repairer':'Reparateur 9)',
        'field_fault':'gefundener Defekt 10)',
        'field_product_repaired':'Ergebnis',
        'field_solution':'Maßnahmen 12)',
        'field_repair_source':'InfoLink',
        'field_hint':'Tipp für andere Reparateure 15)',
        'field_repairability':'',
        'field_repair_information_resourc':'Info-Quelle',
        'field_repair_failed':'Erfolglos',
        'field_repair_information':' Infos verwendet'
}

def getOrNone(data, key):
        if data.get(key) == 0:
                return None
        return data.get(key)

def getOrBlank(data, key):
        if data.get(key) == 0:
                return ''
        return data.get(key)

def product_repaired_from_key(key):
        key_val = {1:'yes', 2:'half',3:'no'}
        return key_val[key]
        

def field_repair_failed_adapter(page_data, row_data, default_value):
        if row_data is None:
                return default_value
        return page_data[row_data]

def field_repair_information_adapter(row_data, lang):
        data_source = {
                'de': {
                        'Nein, nicht gesucht': 'unknown',
                        'Nein, nicht gefunden': 'no',
                        'Ja':'yes'
                },
                'en': {
                        "No, didn't look for it": 'unknown',
                        "No, couln't find it": 'no',
                        'Yes':'yes' 
                },
                'fr': {
                        "Non, pas cherché": 'unknown',
                        "Non, pas trouvé": 'no',
                        'Oui':'yes' 
                },
                'nl': {
                        "Nee, niet gezocht": 'unknown',
                        "Nee, niet gevonden": 'no',
                        'Ja':'yes' 
                }
        }
        return data_source.get(lang).get(row_data)
