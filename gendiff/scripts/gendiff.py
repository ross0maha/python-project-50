import json
import yaml
from gendiff.tree import get_diff
from gendiff.formatters.formatting import formatting


def load_file(file):
    with open(file, 'r') as in_file:
        if file.endswith('.json'):
            return json.load(in_file)
        elif file.endswith('.yaml') or file.endswith('.yml'):
            return yaml.safe_load(in_file)


def generate_diff(first_file, second_file, format='stylish'):
    first_dict = load_file(first_file)
    second_dict = load_file(second_file)
    diff = get_diff(first_dict, second_dict)
    return formatting(diff, format)
