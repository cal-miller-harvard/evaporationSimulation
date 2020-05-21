import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

path = "swave/analysis.txt"

rows = []
with open(path, 'r') as f:
    for i, line in enumerate(f):
        if "Number of collisions to thermalize:" in line:
            ntherm = np.mean([float(i) for i in re.findall(r'\d+.\d+', line)])
            rows.append(np.array([cross_section, ratio, ntherm]))
        elif "cross_section" in line:
            s = line.split("_")
            ratio = float(s[-3])
            cross_section = float(s[-5])

data = np.vstack(rows)
pts = np.unique(data[:,[0,1]],axis=0)
npts = pts.shape[0]
means = np.empty(npts)
stds = np.empty(npts)
for i, pt in enumerate(pts):
    matches = (data[:,[0,1]] == pt).all(axis=1)
    means[i] = np.mean(data[matches,2])
    stds[i] = np.std(data[matches,2])

for ratio in np.unique(pts[:,1]):
    matches = pts[:,1] == ratio
    plt.errorbar(pts[matches,0],means[matches],yerr=stds[matches],label= "{:.1f}".format(1/ratio) if ratio != 0 else "Inf")
    plt.xlabel("Cross section (um)")
    plt.ylabel("Collision to thermalize")
plt.legend(title="elastic to inelastic ratio",loc='upper left')
plt.xlim(0,0.0061)
plt.ylim(0,4.0)
# plt.show()
plt.savefig("swave.pdf")
