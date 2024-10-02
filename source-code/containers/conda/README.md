# Container with conda environment

This Apptainer recipe builds a container with a conda environment.  It can
be used to benchmark the startup time of a container and module load for the
script with the traditional module approach on HPC systems.


## What is it?

1. `conda.recipe`: Apptainer recipe to build a container with a conda
   environment.
1. `environment.yml`: conda environment definition.
1. `import_modules.py`: Python script that imports a number of modules.
