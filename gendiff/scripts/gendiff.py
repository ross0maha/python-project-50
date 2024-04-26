import json


def generate_diff(first_file, second_file):
    with open(first_file, 'r') as file_1, open(second_file, 'r') as file_2:
        first_json = json.load(file_1)
        second_json = json.load(file_2)
        results = '{\n'
        for key, value in sorted(first_json.items()):
            if key in second_json and value == second_json[key]:
                results += f"    {key}: {value}\n"
            elif key not in second_json or value != second_json[key]:
                results += f"  - {key}: {value}\n"
        for key, value in sorted(second_json.items()):
            if key not in first_json or value != first_json[key]:
                results += f"  + {key}: {value}\n"
        results += '}'
    return results.lower()
