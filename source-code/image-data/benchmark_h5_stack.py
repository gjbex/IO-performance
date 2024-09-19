#!/usr/bin/env python
#
# Script to run a benchmark of reading image files from an HDF5 file.
# The script takes the following command line arguments:
#   - the name of the HDF5 file to read from,
#   - the number of files to read

import argparse
import h5py
import pathlib
import random

def brightness(img):
    return img.sum()/(img.shape[0]*img.shape[1]*img.shape[2]*255)

def main():
    parser = argparse.ArgumentParser(description='Benchmark image index method')
    parser.add_argument('h5_file', help='HRDF5 file to read')
    parser.add_argument('--dataset', default='data', help='Dataset to read')
    parser.add_argument('--nr-reads', type=int, help='Number of files to read')
    args = parser.parse_args()

    avg_brightness = 0.0
    dataset = args.dataset
    with h5py.File(args.h5_file, 'r') as h5_file:
        nr_images = h5_file[dataset].shape[0]//4
        for _ in range(args.nr_reads):
            idx = 4*random.randrange(0, nr_images)
            img = h5_file[dataset][:, :, idx:idx + 4]
            # print(img.shape, idx)
            avg_brightness += brightness(img)
    avg_brightness /= args.nr_reads
    print(f'Average brightness: {avg_brightness:.2f}')


if __name__ == '__main__':
    main()
