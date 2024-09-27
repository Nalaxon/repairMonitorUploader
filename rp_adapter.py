import requests
from lxml import html
import yaml

# Uncomment if you need to log your requests
# import http.client as http_client
# import logging

def try_(requests_data, expected_status_code = 200):
    ''' Utility to encapsulate http error handling '''
    if requests_data.status_code != expected_status_code:
        print('Hmm, something went wrong by interacting with ' + requests_data.url)
    return requests_data

def parse_opt_dict(tree, xpath):
    ''' Utility to parse Joomla options '''
    options = tree.xpath(xpath)
    opt_dict = {option.text:option.get('value') for option in options}
    return opt_dict

class Repairmonitor:
    """ Class to interact with repair montor Joomla forms """

    def __init__(self):
        self.session = None

        # Uncomment if you need to log your requests
        # http_client.HTTPConnection.debuglevel = 1
        # logging.basicConfig()
        # logging.getLogger().setLevel(logging.DEBUG)
        # requests_log = logging.getLogger("requests.packages.urllib3")
        # requests_log.setLevel(logging.DEBUG)
        # requests_log.propagate = True

    def login_in(self):
        ''' login with ./credential/auth.yml defined credentials '''
        self.session = requests.Session()
        tree = html.fromstring(try_(self.session.get('https://www.repairmonitor.org/')).content)
        secrete = tree.xpath('//input[@name="form_build_id"]/@value')[0]
        password = ''
        user = ''

        with open(".credentials/auth.yml", 'r', encoding="utf-8") as stream:
            try:
                credentials = yaml.safe_load(stream)
                password = credentials['password']
                user = credentials['user']
            except yaml.YAMLError as exc:
                print('Could not read .credentials/auth.yml!\n' + exc)
                exit(1)

        payload = {'name' : user, 'pass': password, 'form_build_id':secrete, 'form_id':'user_login_form', 'op':'log+in'}

        try_(self.session.post('https://www.repairmonitor.org/en/node/61?destination=/en/node/61', data = payload))

        overview_page = try_(self.session.get('https://www.repairmonitor.org/en/node/61?check_logged_in=1'))
        print(overview_page.content)
    # we are in :)


    def get_page_tree(self, url):
        ''' get parseable content of site '''
        page = try_(self.session.get(url))
        return html.fromstring(page.content)

    def get_add_repair_page_data(self, lang):
        ''' Fetch data required to interact with the form '''
        url = 'https://www.repairmonitor.org/' + lang + '/node/add/repair'
        print('get ' + url)
        new_repair_tree = self.get_page_tree(url)
        changed = new_repair_tree.xpath('//input[@name="changed"]/@value')[0]
        form_build_id = new_repair_tree.xpath('//input[@name="form_build_id"]/@value')[0]
        form_token = new_repair_tree.xpath('//input[@name="form_token"]/@value')[0]

        categories = {}
        repair_failed = {}
        categories = parse_opt_dict(new_repair_tree, '//select[@id="edit-field-categorie"]/option')
        repair_failed = parse_opt_dict(new_repair_tree, '//select[@id="edit-field-repair-failed"]/option')

        # print(str(repair_failed))

        return {
            'changed':changed,
            'form_build_id':form_build_id,
            'form_token':form_token,
            'field_categorie':categories,
            'field_repair_failed':repair_failed
        }

    def post_add_repair_with_data(self, lang, data):
        ''' Add the repair to either drafts or completed repairs '''
        url = 'https://www.repairmonitor.org/' + lang + '/node/add/repair'
        # print(str(data))
        try_(self.session.post(url, data=data))

# 'changed':1713118290,
# 'field_repair_date[0]["value"]'='2024-04-14',
# 'form_build_id'='form-sepwkqBXhiMS6Jk85kN_y-vJNYw76MpaUamlsrBDSAM',
# 'form_token'='dkg-qmxcaZptzt25m8VjSjEU4yDB4xYL7w10zYnjyEM,
# 'form_id'='node_repair_form',
# 'field_reference_number[0]["value"]'=1,
# 'field_kind_product[0]["target_id"]':'Battery+tester',
# 'field_kind_product[0]["kp_other"]':'',
# 'field_brand[0]["autocomplete_fill_field"]':'Philips',
# 'field_categorie'=1685,
# 'field_kind_product[0]["autocomplete_fill_field"]':'Battery+tester'
# 'field_brand[0]["target_id"]':'Philips',
# 'field_brand[0]["other"]':'',
# 'field_product_buildyear[0]["value"]':'',
# 'field_model[0]["target_id"]':'',
# 'field_cause_of_fault[0]["value"]':
# 'field_repairer[0]["target_id"]':'',
# 'field_fault[0]["value"]':'',
# 'field_product_repaired'='yes',
# 'field_solution[0]["value"]':'',
# 'field_repair_failed':'_none'
# 'field_advice[0]["value"]':'',
# 'field_repair_source[0]["value"]':'',
# 'field_hint[0]["value"]':'',
# 'op':'Save+draft',
# 'advanced__active_tab'='edit-revision-information'

