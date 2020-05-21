import numpy as np
from matplotlib import pyplot as plt
import subprocess
import os

# Parameters
elastic_cross_sections = np.linspace(0.0,0.005,11)
elastic_inelastic_ratios = [0.0, 1.0/50, 1.0/100, 1.0/150, 1.0/200, 1.0/250]
repeats = 1
path = "swave"
template = """
Name: Rb Cross Dimensional Thermalization

TMax: 1000

N: 1000
M: 87
T: 200
tau: 0.002

Inelastic: {}
ElasticCoeff: {:.6f}
ReactiveCoeff: {:.6f}
Collision: swave

Trap: harmonic

Bound: 250

NonEquilibrium: 2.0

Depth: 20
"""
slurm_template = """#!/bin/bash
#SBATCH -n 1 # Number of cores requested
#SBATCH -t 0-01:00 # Runtime in minutes
#SBATCH -p shared # Partition to submit to
#SBATCH --mem-per-cpu 1024 # Memory per cpu in MB (see also ?mem-per-cpu)
#SBATCH --open-mode=append
#SBATCH -o {}_job_%j.out # Standard out goes to this file
#SBATCH -e {}_job_%j.err # Standard err goes to this filehostname

# module load Anaconda/5.0.1-fasrc02
# module list

python2.7 --input {} --output {}

"""

# Script
procs = []
for elastic_cross_section in elastic_cross_sections:
    for elastic_inelastic_ratio in elastic_inelastic_ratios:
        fbase = "{}/cross_section_{:.3E}_ratio_{:.3E}".format(path, elastic_cross_section, elastic_inelastic_ratio)
        f_in = fbase+".in"
        with open(f_in, 'w+') as f:
            f.write(template.format(
                "False" if elastic_inelastic_ratio == 0.0 else "True",
                elastic_cross_section, elastic_inelastic_ratio*elastic_cross_section))
        for repeat in range(repeats):
            f_out = fbase+"_repeat_{:d}.out".format(repeat)
            if os.path.exists(f_out):
                os.remove(f_out)
            f_slurm  = fbase+"_repeat_{:d}.slurm".format(repeat)
            f_slurm_log  = fbase+"_repeat_{:d}".format(repeat)
            with open(f_slurm, 'w+') as f:
                f.write(slurm_template.format(f_slurm_log, f_slurm_log, f_in, f_out))
            procs.append(subprocess.Popen(['sbatch', f_slurm]))
for proc in procs:
    proc.wait()