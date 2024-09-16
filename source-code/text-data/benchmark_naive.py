#!/usr/bin/env python
#
# Script to run a benchmark of the naive text reading method.
# The script takes the following command line arguments:
#   - the path glob pattern to the text files to read from,
#   - the number of files to read

import argparse
import pathlib
import random


def main():
    parser = argparse.ArgumentParser(description='Benchmark text index method')
    parser.add_argument('file_pattern', help='File glob pattern for the text files to read')
    parser.add_argument('--nr-reads', type=int, help='Number of files to read')
    args = parser.parse_args()

    files = list(pathlib.Path().glob(args.file_pattern))
    total_chars = 0
    for _ in range(args.nr_reads):
        idx = random.randrange(0, len(files))
        with open(files[idx], 'r') as file:
            text = file.read()
            total_chars += len(text)
    print(f'Total characters read: {total_chars}')


if __name__ == '__main__':
    main()
