# Image data

Image data can be preprocessed to numpy arrays, that can all be stored in
a single dataset of an HDF5 file.


## What is it?

1. `create_data.sh`: Bash script to create the dataset.  It will generate
   TIFF files, convert those to numpy array files, and finally store the
   data in an HDF5 file.
1. `h5.ipynb`: Jupyter notebook illustrating how to load image data from an
   HDF5 file.
1. `datasets.ipynb`: Jupyter notebook illustrating how to load images from a
   Huggingface dataset.
