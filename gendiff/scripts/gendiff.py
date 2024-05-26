from gendiff.load_data import load_data
from gendiff.tree import get_diff
from gendiff.formatters.formatting import formatting


def generate_diff(first_file, second_file, format='stylish'):
    first_dict = load_data(first_file)
    second_dict = load_data(second_file)
    diff = get_diff(first_dict, second_dict)
    return formatting(diff, format)
