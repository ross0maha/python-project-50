import json
import yaml


def load_data(file):
    with open(file, 'r') as in_file:
        if file.endswith('.json'):
            return json.load(in_file)
        elif file.endswith('.yaml') or file.endswith('.yml'):
            return yaml.safe_load(in_file)
