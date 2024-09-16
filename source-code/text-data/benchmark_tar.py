#!/usr/bin/env python
#
# Script to run a benchmark of the text index method.
# The script takes the following command line arguments:
#   - the path to the zip files that holds all the text files to read from,
#   - the number of files to read

import argparse
import random
import tarfile


def main():
    parser = argparse.ArgumentParser(description='Benchmark text index method')
    parser.add_argument('tar_file', help='Path to the tar file to read from')
    parser.add_argument('--nr-reads', type=int, help='Number of files to read')
    args = parser.parse_args()

    with tarfile.TarFile(args.tar_file, 'r') as tar_file:
        names = tar_file.getnames()
        total_chars = 0
        for _ in range(args.nr_reads):
            name = random.choice(names)
            with tar_file.extractfile(name) as file:
                text = file.read()
                total_chars += len(text)
    print(f'Total characters read: {total_chars}')


if __name__ == '__main__':
    main()
