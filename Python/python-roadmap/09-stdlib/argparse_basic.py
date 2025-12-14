# argparse_basic.py
# Basic usage of argparse for CLI arguments

import argparse

parser = argparse.ArgumentParser(description="Simple CLI example")
parser.add_argument("--name", required=True, help="Your name")
parser.add_argument("--age", type=int, help="Your age")

args = parser.parse_args()

print(f"Name: {args.name}")
if args.age:
    print(f"Age: {args.age}")
