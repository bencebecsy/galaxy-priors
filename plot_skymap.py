#!/usr/bin/python
import numpy as np
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

infile = sys.argv[1]
outfile = infile[:-4] + "png"
print outfile

DPI=300



m = hp.read_map(infile)
hp.mollview(m, title="Mollview image RING")
#hp.mollview(m, coord=['C','G'], title="Mollview image RING")
hp.graticule()
plt.savefig(outfile, dpi=DPI)
