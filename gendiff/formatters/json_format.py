import json
from gendiff.formatters.normalize import normalize_values


def format(diff):
    diff = normalize_values(diff)
    return json.dumps(diff, indent=4)
