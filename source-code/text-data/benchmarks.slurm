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

source $VSC_HOME/.conda_init.sh
mamba activate io_performance

# set data set
data=tmp_large_seq

# set number of reads
nr_reads=200000

(>&2 echo "naive method")
time ./benchmark_naive.py "${data}_files.txt" --nr-reads $nr_reads

(>&2 echo "text index method")
time ./benchmark_text_index.py "$data.txt" --index-file "$data.txt.idx" --nr-reads $nr_reads

(>&2 echo "tar method")
time ./benchmark_tar.py "$data.tar" --nr-reads $nr_reads

(>&2 echo "zip method")
time ./benchmark_zip.py "$data.zip" --nr-reads $nr_reads


(>&2 echo "datasets method")
time ./benchmark_arrow.py "${data}_dataset" --nr-reads $nr_reads
