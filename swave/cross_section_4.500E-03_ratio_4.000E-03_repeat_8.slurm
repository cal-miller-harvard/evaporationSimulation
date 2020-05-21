#!/bin/bash
#SBATCH -n 1 # Number of cores requested
#SBATCH -t 0-01:00 # Runtime in minutes
#SBATCH -p shared # Partition to submit to
#SBATCH --mem-per-cpu 1024 # Memory per cpu in MB (see also ?mem-per-cpu)
#SBATCH --open-mode=append
#SBATCH -o swave/cross_section_4.500E-03_ratio_4.000E-03_repeat_8_job_%j.out # Standard out goes to this file
#SBATCH -e swave/cross_section_4.500E-03_ratio_4.000E-03_repeat_8_job_%j.err # Standard err goes to this filehostname

# module load Anaconda/5.0.1-fasrc02
# module list

python2.7 main.py --input swave/cross_section_4.500E-03_ratio_4.000E-03.in --output swave/cross_section_4.500E-03_ratio_4.000E-03_repeat_8.out

