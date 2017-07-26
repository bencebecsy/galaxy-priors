#!/usr/bin/python
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

DPI=300

m = hp.read_map("skymap_prior.fits")
hp.mollview(m, title="Mollview image RING")
#hp.mollview(m, coord=['C','G'], title="Mollview image RING")
hp.graticule()
plt.savefig('skymap_prior.png', dpi=DPI)
