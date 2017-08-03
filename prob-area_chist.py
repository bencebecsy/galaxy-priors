#!/usr/bin/python
import numpy as np
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

infiles = sys.argv[1:]

DPI=300

for infile in infiles:
    outfile = "prob_chist_" + infile[9:-27] + ".png"
    #print outfile

    m = hp.read_map(infile)
    sorted_m = np.sort(m)[::-1]*4*np.pi/m.size
    m_chist = np.cumsum(sorted_m)
    #print sorted_m, m_chist
    area = np.arange(1,(m.size+1)) / float(sorted_m.size) * 4*np.pi *180**2/np.pi**2

    plt.plot(area,m_chist, lw=1, label=infile[-26:-5])

plt.xlabel("Sky area [deg^2]")
plt.ylabel("Probability within sky area")
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.grid()
plt.legend()
plt.savefig(outfile, dpi=DPI)
