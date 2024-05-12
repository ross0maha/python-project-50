import json
import yaml
from gendiff.scripts.parser import parser


def load_file(file):
    with open(file, 'r') as in_file:
        if file.endswith('.json'):
            return json.load(in_file)
        elif file.endswith('.yaml') or file.endswith('.yml'):
            return yaml.safe_load(in_file)


def generate_diff(first_file, second_file, format='stylish'):
    first_file_dict = load_file(first_file)
    second_file_dict = load_file(second_file)
    return parser(first_file_dict, second_file_dict)
