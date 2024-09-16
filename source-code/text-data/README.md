# Text indexing

An I/O pattern that has detrimental performance is repeatedly reading
many small to medium size text files.  In this directory, you will find
a number of benchmarks to demonstrate the issue, as well as a number of
solutions to the problem.


## What is it?

### Indexed file

1. `index_text_files.py`: Python script that concatenates all text files
   that fit a given pattern into a single file, and creates an index file
   to facilitate random access to the content of the individual files.
1. `text_index.py`: Python module that implements a `TextIndex` class
   that can be used to access the content of the individual files.
1. `indexed_files.ipynb`: Jupyter notebook that demonstrates the use
   of the `TextIndex` class and benchmarks it against the naive approach.
