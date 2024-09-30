#!/usr/bin/env python
#
# Script to run a benchmark of the naive text reading method.
# The script takes the following command line arguments:
#   - the file containing the list of files to read
#   - the number of files to read

import argparse
import pathlib
import random

def run(file_list, nr_reads):
    with open(file_list, 'r') as file:
        files = [name.strip() for name in file.readlines()]
    total_chars = 0
    for _ in range(nr_reads):
        idx = random.randrange(0, len(files))
        with open(files[idx], 'r') as file:
            text = file.read()
            total_chars += len(text)
    return total_chars

def main():
    parser = argparse.ArgumentParser(description='Benchmark text index method')
    parser.add_argument('file', help='File containing the list of files to read')
    parser.add_argument('--nr-reads', type=int, help='Number of files to read')
    args = parser.parse_args()

    total_chars = run(args.file, args.nr_reads)
    print(f'Total characters read: {total_chars}')


if __name__ == '__main__':
    main()
