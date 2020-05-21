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

# Script
procs = []
for elastic_cross_section in elastic_cross_sections:
    for elastic_inelastic_ratio in elastic_inelastic_ratios:
        f_in = "{}/cross_section_{:.3E}_ratio_{:.3E}.in".format(path, elastic_cross_section, elastic_inelastic_ratio)
        with open(f_in, 'w+') as f:
            f.write(template.format(
                "False" if elastic_inelastic_ratio == 0.0 else "True",
                elastic_cross_section, elastic_inelastic_ratio*elastic_cross_section))
        for repeat in range(repeats):
            f_out = "{}/cross_section_{:.3E}_ratio_{:.3E}_repeat_{:d}.out".format(path, elastic_cross_section, elastic_inelastic_ratio,repeat)
            if os.path.exists(f_out):
                os.remove(f_out)
            procs.append(subprocess.Popen(['python2.7', 'main.py', '--input', f_in, '--output', f_out]))
for proc in procs:
    proc.wait()