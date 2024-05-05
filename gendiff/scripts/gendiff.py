import json
import yaml
from gendiff.scripts.parser import parser


def generate_diff(first_file, second_file):
    first_dict, second_dict = {}, {}
    with open(first_file, 'r') as file_1, open(second_file, 'r') as file_2:
        if first_file.endswith('.json'):
            first_dict = json.load(file_1)
        elif first_file.endswith('.yaml') or first_file.endswith('.yml'):
            first_dict = yaml.safe_load(file_1)
        if second_file.endswith('.json'):
            second_dict = json.load(file_2)
        elif second_file.endswith('.yaml') or second_file.endswith('.yml'):
            second_dict = yaml.safe_load(file_2)
    return parser(first_dict, second_dict)
