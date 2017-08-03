#!/usr/bin/python
#-------------------------------------------------------------------------------
#
# Code to generate a prior distribution to GW skymaps based on the distribution
# of matter in the local universe.
#
#-------------------------------------------------------------------------------
import numpy as np
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import sys

infile = sys.argv[1]

start = timer()

NSIDE = int(sys.argv[2])
DPI = 100
print "Number of pixels used: %d" %hp.nside2npix(NSIDE)

#-------------------------------------------------------------------------------
#specify magnitude weight exponents
#-------------------------------------------------------------------------------
weighting_mode = sys.argv[3]
alpha_B = float(sys.argv[4])
alpha_J = float(sys.argv[5])
alpha_H = float(sys.argv[6])
alpha_K = float(sys.argv[7])
print "Using weighting mode %s with B J H K exponents of %f %f %f %f."%(weighting_mode, alpha_B, alpha_J, alpha_H, alpha_K)

#somehow we should try to write all info about our prior into the header of the fits file

#-------------------------------------------------------------------------------
#read in galaxy data
#-------------------------------------------------------------------------------
skip_first_n = 0
limit=-1

glade=np.load(infile)
#print glade[skip_first_n:limit]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++Need to check the conventions for coordinates!!!
ra = glade[skip_first_n:limit,6].astype(float)*np.pi/180.0 #in radians
dec = glade[skip_first_n:limit,7].astype(float)*np.pi/180.0 #in radians
dist = glade[skip_first_n:limit,8].astype(float)
dphi = np.ones(ra.size)*1*np.pi/180.0 #+++++++++++++++Just a placeholder. Need to calculate this from some GLADE data.
b = glade[skip_first_n:limit,11].astype(float)
j = glade[skip_first_n:limit,13].astype(float)
h = glade[skip_first_n:limit,15].astype(float)
k = glade[skip_first_n:limit,17].astype(float)
#print ra, dec, dphi
print "Number of galaxies: %d"%dist.size

#-------------------------------------------------------------------------------
#filtering the catalog
#-------------------------------------------------------------------------------
#distance>0 (maybe we should exclude very closeby ones as well)
"""
dist_min = 0.0
ra_filt = ra[dist>dist_min]
dec_filt = dec[dist>dist_min]
dist_filt = dist[dist>dist_min]
dphi_filt = dphi[dist>dist_min]
b_filt = b[dist>dist_min]
j_filt = j[dist>dist_min]
h_filt = h[dist>dist_min]
k_filt = k[dist>dist_min]

#distance<25 Mpc
dist_max = 50.0
ra_filt2 = ra_filt[dist_filt<dist_max]
dec_filt2 = dec_filt[dist_filt<dist_max]
dist_filt2 = dist_filt[dist_filt<dist_max]
dphi_filt2 = dphi_filt[dist_filt<dist_max]
b_filt2 = b_filt[dist_filt<dist_max]
j_filt2 = j_filt[dist_filt<dist_max]
h_filt2 = h_filt[dist_filt<dist_max]
k_filt2 = k_filt[dist_filt<dist_max]

#B magnitude != nan

ra_filt3 = ra_filt2[~np.isnan(b_filt2)]
dec_filt3 = dec_filt2[~np.isnan(b_filt2)]
dist_filt3 = dist_filt2[~np.isnan(b_filt2)]
dphi_filt3 = dphi_filt2[~np.isnan(b_filt2)]
b_filt3 = b_filt2[~np.isnan(b_filt2)]
j_filt3 = j_filt2[~np.isnan(b_filt2)]
h_filt3 = h_filt2[~np.isnan(b_filt2)]
k_filt3 = k_filt2[~np.isnan(b_filt2)]

#finalize
ra = ra_filt3
dec = dec_filt3
dist = dist_filt3
dphi = dphi_filt3
b = b_filt3
j = j_filt3
h = h_filt3
k = k_filt3
"""

#print dist.size
#-------------------------------------------------------------------------------
#add galaxies to the map
#-------------------------------------------------------------------------------
sum_pix = 0
m=np.zeros(hp.nside2npix(NSIDE))
for i in range(ra.size): #maybe do this in numpy as well
    Phi = ra[i] #removed negative sign, because it seems like there's no need for it
    Theta = np.pi/2-dec[i]
    Dphi = dphi[i]
    DM = 5.0*np.log10(dist[i]*1e6) - 5.0 #distance modulus
    B = b[i] - DM
    #print b[i], B
    J = j[i] - DM
    H = h[i] - DM
    K = k[i] - DM
    gal_vector = hp.ang2vec(Theta, Phi)
    pixels = hp.query_disc(NSIDE, gal_vector, 10*Dphi)
    pixels_vector = hp.pix2vec(NSIDE,pixels)
    angle = np.arccos(np.dot(gal_vector,pixels_vector))    
    if weighting_mode=='mag':
        weight = (-B)**alpha_B * (-J)**alpha_J * (-H)**alpha_H * (-K)**alpha_K #power law weights
    elif weighting_mode=='lum':
        lum_B = np.power(10.0, -0.4*B) #not equals to the luminosity, constant prefactor is neglected becase we normalize the whole thing at the end
        lum_J = np.power(10.0, -0.4*J)
        lum_H = np.power(10.0, -0.4*H)
        lum_K = np.power(10.0, -0.4*K)
        weight = (lum_B)**alpha_B * (lum_J)**alpha_J * (lum_H)**alpha_H * (lum_K)**alpha_K
    #print weight
    val = weight*np.exp(-angle**2/(2*Dphi**2))/np.sqrt(2*np.pi*Dphi**4) #^4 instead of ^2 because it is multivariate
    #print val
    m[pixels] += val
    sum_pix += np.sum(val)
    if i%1000==0:
        print i

#-------------------------------------------------------------------------------
#normalization
#-------------------------------------------------------------------------------
m = np.divide(m,sum_pix*4*np.pi/hp.nside2npix(NSIDE))

print "Normalization: %r" %(np.sum(m)*4*np.pi/hp.nside2npix(NSIDE))

#-------------------------------------------------------------------------------
#saving
#-------------------------------------------------------------------------------
min_dist=0.0
max_dist=200.0

outfile = "gx_prior_%.1f-%.1fMpc_NSIDE%d_w-%sB%.1fJ%.1fH%.1fK%.1f.fits"%(min_dist,max_dist,NSIDE,weighting_mode,alpha_B,alpha_J,alpha_H,alpha_K)
hp.write_map(outfile,m)

end = timer()
print "Elapsed time: %r seconds" %(end-start)
