import numpy as np
import matplotlib.pyplot as plt

DPI=300

glade=np.load("gx_list_glade.npy")

#filter
filt = range(glade.shape[0])
#print glade.shape[0]

ra = glade[filt,0]
dec = glade[filt,1]
dist = glade[filt,2]
b = glade[filt,3]
j = glade[filt,4]
h = glade[filt,5]
k = glade[filt,6]


#################################
#DISTANCE
#################################
print dist[~np.isnan(dist)].size
plt.figure(0)
plt.hist(dist[~np.isnan(dist)], bins=100)
plt.xlabel("Distance [Mpc]")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_dist_linlog.png', dpi=DPI)

#log-log plot
plt.figure(7)
plt.hist(dist[~np.isnan(dist)], bins=np.logspace(0 ,np.log10(np.amax(dist[~np.isnan(dist)])), 100))
plt.xlabel("Distance [Mpc]")
plt.ylabel("#")
plt.gca().set_xscale('log')
plt.gca().set_yscale('log')
plt.savefig('glade_hist_dist_loglog.png', dpi=DPI)

plt.figure(8)
plt.hist(dist[~np.isnan(dist)], bins=100, range=(dist[~np.isnan(dist)].min(),100.0))
plt.xlabel("Distance [Mpc]")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_dist_linlog_zoom.png', dpi=DPI)

#################################
#RA
#################################
print ra[~np.isnan(ra)].size
plt.figure(1)
plt.hist(ra[~np.isnan(ra)], bins=100)
plt.xlabel("RA [deg]")
plt.ylabel("#")
#plt.gca().set_yscale('log')
plt.savefig('glade_hist_ra.png', dpi=DPI)

#################################
#DEC
#################################
print dec[~np.isnan(dec)].size
plt.figure(2)
plt.hist(dec[~np.isnan(dec)], bins=100)
plt.xlabel("Dec [deg]")
plt.ylabel("#")
#plt.gca().set_yscale('log')
plt.savefig('glade_hist_dec.png', dpi=DPI)

#################################
#B MAGNITUDE (lambda_middle = 365 nm)
#################################
print b[~np.isnan(b)].size
plt.figure(3)
plt.hist(b[~np.isnan(b)], bins=100)
plt.xlabel("Apparent B magnitude")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_b.png', dpi=DPI)

#################################
#J MAGNITUDE (lambda_middle = 1220 nm)
#################################
print j[~np.isnan(j)].size
plt.figure(4)
plt.hist(j[~np.isnan(j)], bins=100)
plt.xlabel("Apparent J magnitude")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_j.png', dpi=DPI)

#################################
#H MAGNITUDE (lambda_middle = 1630 nm)
#################################
print h[~np.isnan(h)].size
plt.figure(5)
plt.hist(h[~np.isnan(h)], bins=100)
plt.xlabel("Apparent H magnitude")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_h.png', dpi=DPI)

#################################
#K MAGNITUDE (lambda_middle = 2190 nm)
#################################
print k[~np.isnan(k)].size
plt.figure(6)
plt.hist(k[~np.isnan(k)], bins=100)
plt.xlabel("Apparent K magnitude")
plt.ylabel("#")
plt.gca().set_yscale('log')
plt.savefig('glade_hist_k.png', dpi=DPI)
