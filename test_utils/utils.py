import os
import json


def read_json_file(path_to_json_file):
    abs_path_to_json_file = os.path.abspath(path_to_json_file)
    with open(abs_path_to_json_file, encoding='utf-8-sig') as json_f:
        text = json_f.read()
        json_data = json.loads(text)
        return json_data
