#!/usr/bin/python
import numpy as np
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

infile = sys.argv[1]
outfile = "prob_chist_" + infile[9:-4] + "png"
print outfile

DPI=300

m = hp.read_map(infile)

sorted_m = np.sort(m)[::-1]*4*np.pi/m.size
m_chist = np.cumsum(sorted_m)

print sorted_m, m_chist
area = np.arange(1,(m.size+1)) / float(sorted_m.size) * 4*np.pi *180**2/np.pi**2

plt.plot(area,m_chist, lw=1)
plt.xlabel("Sky area [deg^2]")
plt.ylabel("Probability within sky area")
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.grid()
plt.savefig(outfile, dpi=DPI)
