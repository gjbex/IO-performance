#!/usr/bin/env python
#
# Script to run a benchmark of the text index method.
# The script takes the following command line arguments:
#   - the path to the dataset directory
#   - the number of files to read

import argparse
from datasets import Dataset
import random


def run(dataset_dir, nr_reads):
    dataset = Dataset.load_from_disk(dataset_dir, keep_in_memory=True)

    total_chars = 0
    for _ in range(nr_reads):
        idx = random.randrange(0, len(dataset))
        text = dataset[idx]['text']
        total_chars += len(text)
    return total_chars

def main():
    parser = argparse.ArgumentParser(description='Benchmark text index method')
    parser.add_argument('dataset_dir', help='Path to the text file to read from')
    parser.add_argument('--nr-reads', type=int, help='Number of files to read')
    args = parser.parse_args()

    total_chars = run(args.dataset_dir, args.nr_reads)
    print(f'Total characters read: {total_chars}')


if __name__ == '__main__':
    main()
