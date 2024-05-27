import json
import yaml


def get_data(source, format):
    match format:
        case 'json':
            return json.load(source)
        case 'yaml':
            return yaml.safe_load(source)
        case 'yml':
            return yaml.safe_load(source)


def load_file(file):
    with open(file, 'r') as in_file:
        return get_data(in_file, file.split('.')[-1])
