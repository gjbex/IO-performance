#!/usr/bin/env python
#
# Script to run a benchmark of the given method.
# The script takes the following command line arguments:
#  - the path to the data file or directory
#  - the number of files to read
# - the method to use, this can be either 'naive', 'text_index', 'tar', 'zip',
#   or 'dataset'

import argparse
import importlib.util

def main():
    parser = argparse.ArgumentParser(description='Benchmark text index method')
    parser.add_argument('path', help='Path to the data file or directory')
    parser.add_argument('--nr-reads', type=int, help='Number of files to read')
    parser.add_argument('--method', help='Method to use',
                        choices=['naive', 'text_index', 'tar', 'zip', 'dataset'])
    args = parser.parse_args()

    benchmark_module = importlib.import_module(f'benchmark_{args.method}')
    total_bytes_read = benchmark_module.run(args.path, args.nr_reads)
    print(f'Total bytes read: {total_bytes_read}')


if __name__ == '__main__':
    main()
