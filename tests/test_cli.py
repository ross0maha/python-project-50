import sys
import pytest
from gendiff.cli import parse_args


def test_parse_args():
    sys.argv = ['gendiff', '--format', 'plain', 'file1.json', 'file2.json']
    args = parse_args()
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'plain'


def test_parse_args_help(capsys):
    with open('tests/fixtures/help_output.txt', 'r') as f:
        help_text = f.read()
    sys.argv = ['gendiff', '-h']
    with pytest.raises(SystemExit):
        parse_args()
    out, err = capsys.readouterr()
    assert out == help_text


def test_parse_args_empty(capsys):
    with open('tests/fixtures/cli_out.txt', 'r') as f:
        cli_out = f.read()
    sys.argv = ['gendiff']
    with pytest.raises(SystemExit):
        parse_args()
    out, err = capsys.readouterr()
    assert err == cli_out
