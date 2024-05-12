from gendiff.tree import get_diff
from gendiff.formatters.stylish_format import format


def parser(first_dict, second_dict):
    return format(get_diff(first_dict, second_dict))
