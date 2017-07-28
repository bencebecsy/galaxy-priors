#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import json

DPI=300

with open("gx_list_glade.json", 'r') as json_file:
    glade = json.load(json_file)
    
glade = np.array(glade)

#filter
filt = range(glade.shape[0])
#print glade.shape[0]

#columns:(0) PGC number (1) GWGC name (2) HyperLEDA name (3) 2MASS name (4) SDSS-DR12 name
        #        (5) flag1 Q/G (6) RA [deg] (7) dec [deg] (8) dist [Mpc] (9) dist_err [Mpc]
        #        (10) z (11) apparent B mag (12) B_err (13) apparent J mag (14)	J_err (15) apparent H mag
        #        (16) H_err (17) apparent K mag (18) K_err (19) flag2 	0: no measured dist or z 1: measured z 2: measured dist
        #        (20) flag3 0: measured B mag 1: ML estimated B mag (21) B_err_min (22) B_err_max
        #        (23) flag4 0: z from measured dist 1: ML estimated z (24) z_err_min (25) z_err_max


ra = glade[filt,6].astype(float)
dec = glade[filt,7].astype(float)
dist = glade[filt,8].astype(float)
b = glade[filt,11].astype(float)
j = glade[filt,13].astype(float)
h = glade[filt,15].astype(float)
k = glade[filt,17].astype(float)

print dist.dtype

#################################
#DISTANCE
#################################
dist = dist[~np.isnan(dist)]
print dist.size
plt.figure(0)
plt.hist(dist, bins=100)
plt.title("Mean=%.3f, RMS=%.3f, Number of points=%d"%(np.mean(dist), np.sqrt(np.mean(dist**2)), dist.size))
plt.xlabel("Distance [Mpc]")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_dist_linlog.png', dpi=DPI)

#log-log plot
plt.figure(7)
plt.hist(dist, bins=np.logspace(0 ,np.log10(np.amax(dist)), 100))
plt.title("Mean=%.3f, RMS=%.3f, Number of points=%d"%(np.mean(dist), np.sqrt(np.mean(dist**2)), dist.size))
plt.xlabel("Distance [Mpc]")
plt.ylabel("#")
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.savefig('glade_hist_dist_loglog.png', dpi=DPI)

plt.figure(8)
plt.hist(dist, bins=100, range=(dist.min(),100.0))
plt.title("Mean=%.3f, RMS=%.3f, Number of points=%d"%(np.mean(dist), np.sqrt(np.mean(dist**2)), dist.size))
plt.xlabel("Distance [Mpc]")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_dist_linlog_zoom.png', dpi=DPI)

#################################
#RA
#################################
ra = ra[~np.isnan(ra)]
print ra.size
plt.figure(1)
plt.hist(ra, bins=100)
plt.title("Mean=%.3f, RMS=%.3f, Number of points=%d"%(np.mean(ra), np.sqrt(np.mean(ra**2)), ra.size))
plt.xlabel("RA [deg]")
plt.ylabel("#")
#plt.gca().set_yscale('log')
plt.savefig('glade_hist_ra.png', dpi=DPI)

#################################
#DEC
#################################
dec = dec[~np.isnan(dec)]
print dec.size
plt.figure(2)
plt.hist(dec, bins=100)
plt.title("Mean=%.3f, RMS=%.3f, Number of points=%d"%(np.mean(dec), np.sqrt(np.mean(dec**2)), dec.size))
plt.xlabel("Dec [deg]")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_dec.png', dpi=DPI)

#################################
#B MAGNITUDE (lambda_middle = 365 nm)
#################################
b = b[~np.isnan(b)]
print b.size
plt.figure(3)
plt.hist(b, bins=100)
plt.title("Mean=%.3f, RMS=%.3f, Number of points=%d"%(np.mean(b), np.sqrt(np.mean(b**2)), b.size))
plt.xlabel("Apparent B magnitude")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_b.png', dpi=DPI)

#################################
#J MAGNITUDE (lambda_middle = 1220 nm)
#################################
j = j[~np.isnan(j)]
print j.size
plt.figure(4)
plt.hist(j, bins=100)
plt.title("Mean=%.3f, RMS=%.3f, Number of points=%d"%(np.mean(j), np.sqrt(np.mean(j**2)), j.size))
plt.xlabel("Apparent J magnitude")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_j.png', dpi=DPI)

#################################
#H MAGNITUDE (lambda_middle = 1630 nm)
#################################
h = h[~np.isnan(h)]
print h.size
plt.figure(5)
plt.hist(h, bins=100)
plt.title("Mean=%.3f, RMS=%.3f, Number of points=%d"%(np.mean(h), np.sqrt(np.mean(h**2)), h.size))
plt.xlabel("Apparent H magnitude")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_h.png', dpi=DPI)

#################################
#K MAGNITUDE (lambda_middle = 2190 nm)
#################################
k = k[~np.isnan(k)]
print k.size
plt.figure(6)
plt.hist(k, bins=100)
plt.title("Mean=%.3f, RMS=%.3f, Number of points=%d"%(np.mean(k), np.sqrt(np.mean(k**2)), k.size))
plt.xlabel("Apparent K magnitude")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_k.png', dpi=DPI)
