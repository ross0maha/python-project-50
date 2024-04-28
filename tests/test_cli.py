import sys
from gendiff.cli import parse_args


def test_parse_args():
    sys.argv = ['gendiff', '--format', 'plain', 'file1.json', 'file2.json']
    args = parse_args()
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'plain'


# def test_parse_args_help():
#     conslole_output = open('tests/fixtures/help_output.txt', 'r').read()
#     sys.argv = ['gendiff', '-h']
#     args = parse_args()
#     assert args == conslole_output
