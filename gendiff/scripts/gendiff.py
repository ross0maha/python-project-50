#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
parser.add_argument('-F', '--format', help='set format of output')
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()


def main():
    print(f">> Entry function {main.__name__}")
    print(f'args: {args}')
    print(f'args.first_file: {args.first_file}')
    print(f'args.second_file: {args.second_file}')
    print(f'args.format: {args.format}')


if __name__ == "__main__":
    main()
