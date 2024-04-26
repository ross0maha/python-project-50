#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    args = parse_args()
    res = generate_diff(args.first_file, args.second_file)
    print(res)
