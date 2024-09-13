# Data generation

This directory contains a number of scripts to create data for benchmarking and
conversion.


## What is it?

1. `create_csv_data.py`: script to create one or more CSV files with a column
   of timestamps and any number of columns with random double precision data.
   The number of rows can also be specified.
1. `convert_csv_to_parquet.py`: script to convert a CSV file to a Parquet file.
   The script uses polars lazy API to deal with very large files.


## How to use?

### `create_csv_data.py`

To generate a CSV file with 1000 rows and 10 columns with random double
precision data, run

```bash
$ python create_csv_data.py data  --rows 1000 --cols 10
```

### `convert_csv_to_parquet.py`

To convert a CSV file to a Parquet file, run

```bash
$ python convert_csv_to_parquet.py data.csv
```
