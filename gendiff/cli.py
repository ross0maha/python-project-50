import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='first file')
    parser.add_argument('second_file', help='second file')
    parser.add_argument('-F', '--format',
                        help='set format of output')
# default='stylish', choices=['plain', 'json', 'stylish'])
    return parser.parse_args()
