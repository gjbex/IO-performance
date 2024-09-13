# Data generation

This directory contains a number of scripts to create data for benchmarking and
conversion.


## What is it?

1. `create_csv_data.py`: script to create one or more CSV files with a column
   of timestamps and any number of columns with random double precision data.
   The number of rows can also be specified.
1. `convert_csv_to_parquet.py`: script to convert a CSV file to a Parquet file.
   The script uses polars lazy API to deal with very large files.
1. `concat_csv_to_parquet.py`: script to concatenate a CSV file to a Parquet
   file.  The script uses polars lazy API to deal with very large files.  Note
   that a temporary file is created to store the concatenated data.
1. `create_text_data.py`: script to generate text data with given
   characteristics.


## How to use?

### `create_csv_data.py`

To generate a CSV file with 1000 rows and 10 columns with random double
precision data, run

```bash $ python create_csv_data.py data  --rows 1000 --cols 10 ```

### `convert_csv_to_parquet.py`

To convert a CSV file to a Parquet file, run

```bash $ python convert_csv_to_parquet.py data.csv ```

### `concat_csv_to_parquet.py`

To concatenate a CSV file to a Parquet file, run

```bash
$ python concat_csv_to_parquet.py data.csv data.parquet
```


### `create_text_data.py`

To generate a text file with 1000 lines of 80 characters each, run

```bash
$ python create_text_data.py --output data.txt --words 1000 --max-words-per-line 80
```
