#!/usr/bin/env bash
#
# This script creates
#  - a directory for the data
#  - the individual image data files in that directory
#  - the individual numpy arrayfiles in that directory
#  - the HDF5 file that contains all the data
#
# To create the text files, the script uses the `../data-generation/create_text_data.py`
# script.  To create the text and index file for TextIndex, the script uses the
# `index_text_files.py` script.
#
# The scripts takes the following command line arguments:
#  - the name of the directory to write the files in,
#  - the number of text files to create.

# Check the number of arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory> <number of image files>"
    exit 1
fi

# Check that the directory does not exist
if [ -d "$1" ]; then
    echo "Directory $1 already exists"
    exit 1
fi

# Create the directory
mkdir "$1"

workdir=$(pwd)
pushd ../data-generation
# Create the text files
for i in $(seq 1 $2); do
    bash create_image_data.sh \
        $i \
        "$workdir/$1"/img$(printf "%06d" $i).tiff
done
popd

# Convert the TIFF image fils to numpy array files
for file in $(ls $1/*.tiff); do
    python ../data-generation/convert_tiff_to_numpy.py $file
done

# Create the HDF5 file
python ../data-generation/concat_numpy_to_hdf5.py "$1/*.npy" "$1.h5"
