#!/usr/bin/env python
#
# Script to run a benchmark of the naive image reading method.
# The script takes the following command line arguments:
#   - the path glob pattern to the image files to read from,
#   - the number of files to read

import argparse
import pathlib
import random
import skimage.io as io

def brightness(img):
    return img.sum()/(img.shape[0]*img.shape[1]*img.shape[2]*255)

def main():
    parser = argparse.ArgumentParser(description='Benchmark image index method')
    parser.add_argument('file_pattern', help='File glob pattern for the image files to read')
    parser.add_argument('--nr-reads', type=int, help='Number of files to read')
    args = parser.parse_args()

    files = list(pathlib.Path().glob(args.file_pattern))
    avg_brightness = 0.0
    for _ in range(args.nr_reads):
        idx = random.randrange(0, len(files))
        img = io.imread(files[idx])
        avg_brightness += brightness(img)
    avg_brightness /= args.nr_reads
    print(f'Average brightness: {avg_brightness:.2f}')


if __name__ == '__main__':
    main()
