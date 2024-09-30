#!/usr/bin/env -S bash -l
#SBATCH --account=lpt2_sysadmin
#SBATCH --cluster=wice
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=10G
#SBATCH --time=12:00:00
#SBATCH --mail-user=geertjan.bex@uhasselt.be
#SBATCH --mail-type=END,FAIL

# test whehter the conda initialization file exists, if so, source it
[ -e $VSC_HOME/.conda_init] && source $VSC_HOME/.conda_init.sh

# activate the conda environment
mamba activate io_performance

# set data set
data=tmp_large_seq

# set number of reads
nr_reads=200000

(>&2 echo "naive method")
time ./benchmark.py "${data}_files.txt" --nr-reads $nr_reads --method naive

(>&2 echo "text index method")
time ./benchmark.py "$data.txt" --nr-reads $nr_reads --method text_index

(>&2 echo "tar method")
time ./benchmark.py "$data.tar" --nr-reads $nr_reads --method tar

(>&2 echo "zip method")
time ./benchmark.py "$data.zip" --nr-reads $nr_reads --method zip

(>&2 echo "datasets method")
time ./benchmark.py "${data}_dataset" --nr-reads $nr_reads --method dataset
