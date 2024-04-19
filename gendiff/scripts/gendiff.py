#!/usr/bin/env python3
from gendiff.cli import parse_args


def main():
    args = parse_args()
    print(f">> Entry function: {main.__name__}")
    print(f'args: {args}')
    print(f'args.first_file: {args.first_file}')
    print(f'args.second_file: {args.second_file}')
    print(f'args.format: {args.format}')


if __name__ == "__main__":
    main()
