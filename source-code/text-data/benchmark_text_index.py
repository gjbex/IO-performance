#!/usr/bin/env python
#
# Script to run a benchmark of the text index method.
# The script takes the following command line arguments:
#   - the path to the concatenated text file to read from,
#   - the path to the index file (optinial, if not given, the
#     index file name is that of the text file with a .idx extension),
#   - the number of files to read

import argparse
import random
from text_index import TextIndex


def main():
    parser = argparse.ArgumentParser(description='Benchmark text index method')
    parser.add_argument('text_file', help='Path to the text file to read from')
    parser.add_argument('--index-file', nargs='?', help='Path to the index file')
    parser.add_argument('--nr-reads', type=int, default=10_000, help='Number of files to read')
    parser.add_argument('--cache-size', type=int, default=128, help='Size of the cache')
    args = parser.parse_args()

    index_file = args.index_file
    if not index_file:
        index_file = args.text_file + '.idx'

    text_index = TextIndex(args.text_file, index_file, max_cache_size=args.cache_size)

    total_chars = 0
    for _ in range(args.nr_reads):
        idx = random.randrange(0, len(text_index))
        text = text_index.read_text(idx)
        total_chars += len(text)
    print(f'Total characters read: {total_chars}')


if __name__ == '__main__':
    main()
