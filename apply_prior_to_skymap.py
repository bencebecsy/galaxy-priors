#!/usr/bin/python
import numpy as np
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
from detector_cache import detectors
import triangulate
from ligo.gracedb.rest import GraceDb
gdb = GraceDb()


graceid = sys.argv[1]
prior_name = sys.argv[2]

print graceid
fitsname = 'bayestar.fits.gz'
local_file_name = 'bayestar.fits.gz'
with open(local_file_name, 'w') as lf:
    lf.write(gdb.files(graceid, fitsname).read())

post = hp.read_map(local_file_name)
prior = hp.read_map(prior_name)
new_nside = hp.npix2nside(max(len(post), len(prior))) #shouldn't it be just the nside of post?
post = hp.ud_grade(post, new_nside, power=-2)
prior = hp.ud_grade(prior, new_nside, power=-2)


#-----------------------------------------------------------------------------
#Antenna patterns
#-----------------------------------------------------------------------------
npix = hp.nside2npix(new_nside)
theta, phi = hp.pix2ang(new_nside, np.arange(npix))
ant = np.zeros((npix,), dtype=float)

### add the antenna response for each detector in quadrature
for name in 'H L'.split(): ### only include the 2 LIGOs for now
    fp, fx = detectors[name].antenna_patterns(theta, phi, np.zeros_like(theta))
    ant += np.abs(fp)**2 + np.abs(fx)**2

ant = ant**(3./2) ### scale the result so it corresponds to a uniform-in-volume cumulative distribution

gps = 1180922494.4922
ant = triangulate.rotateMapE2C(ant, gps)



#-----------------------------------------------------------------------------
#Applying the prior
#-----------------------------------------------------------------------------
#new_post = post*prior
#new_post = post*prior / ant
new_post = ant
#NORMALIZATION
outfile = "newprior_" + local_file_name
hp.write_map(outfile,new_post)
