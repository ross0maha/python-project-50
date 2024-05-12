def normalize_values(file):
    correct_val = {None: "null", True: "true", False: "false"}

    for key, val in file.items():
        if isinstance(val, dict):
            normalize_values(val)
        elif isinstance(val, (bool, type(None))):
            file[key] = correct_val[val]
    return file
