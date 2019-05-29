import os
import json
from lib.common import basic_get_request, basic_delete_request
from resources.endpoints import endpoints


def read_json_file(path_to_json_file):
    abs_path_to_json_file = os.path.abspath(path_to_json_file)
    with open(abs_path_to_json_file, encoding='utf-8-sig') as json_f:
        text = json_f.read()
        json_data = json.loads(text)
        return json_data


def delete_all_fixtures():
    all_fixtures_before_deletion = basic_get_request(endpoints["get_fixtures"]).json()
    for x in range(len(all_fixtures_before_deletion), 0, -1):
        basic_delete_request(endpoints["get_fixture_by_id"] + str(x))
