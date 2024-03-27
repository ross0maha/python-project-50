#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file', type=argparse.FileType('r'))
parser.add_argument('second_file', type=argparse.FileType('r'))
args = parser.parse_args()
print(args.accumulate(args.integers))


def main():
    print(f">> Entry function {main.__name__}")


if __name__ == "__main__":
    main()
