
def parser(first_dict, second_dict):
    results = '{\n'
    for key, value in sorted(first_dict.items()):
        if key in second_dict and value == second_dict[key]:
            results += f"    {key}: {value}\n"
        elif key not in second_dict or value != second_dict[key]:
            results += f"  - {key}: {value}\n"
    for key, value in sorted(second_dict.items()):
        if key not in first_dict or value != first_dict[key]:
            results += f"  + {key}: {value}\n"
    results += '}'
    return results.lower()
