#!/usr/bin/python
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

DPI=300

infile=sys.argv[1]

glade = np.load(infile)

#filter
filt = range(glade.shape[0])
#print glade.shape[0]

#columns:(0) PGC number (1) GWGC name (2) HyperLEDA name (3) 2MASS name (4) SDSS-DR12 name
        #        (5) flag1 Q/G (6) RA [deg] (7) dec [deg] (8) dist [Mpc] (9) dist_err [Mpc]
        #        (10) z (11) apparent B mag (12) B_err (13) apparent J mag (14)	J_err (15) apparent H mag
        #        (16) H_err (17) apparent K mag (18) K_err (19) flag2 	0: no measured dist or z 1: measured z 2: measured dist
        #        (20) flag3 0: measured B mag 1: ML estimated B mag (21) B_err_min (22) B_err_max
        #        (23) flag4 0: z from measured dist 1: ML estimated z (24) z_err_min (25) z_err_max

pcg = glade[filt,0]
dist = glade[filt,8].astype(float)

print pcg.size, dist.size
print pcg


gwgc_file = sys.argv[2]


gwgc_pcg = []
gwgc_dist = []
gwgc_de = []
with open(gwgc_file, "r") as gf:
    lines = gf.readlines()
    for line in lines:
        l = line.split("|")
        gwgc_pcg.append(l[0])
        gwgc_dist.append(l[14])
        gwgc_de.append(l[15])

gwgc_dist = np.array(gwgc_dist).astype(float)

x = [] #GLADE dist
y = [] #GWGC dist
print len(gwgc_pcg)
for i,ID in enumerate(gwgc_pcg):
    if i%1000==0:
        print i
    if ID in pcg:
        x.append(dist[np.where(pcg==ID)])
        y.append(gwgc_dist[gwgc_pcg.index(ID)])






#################################
#PLOT
#################################
plt.figure(0)
plt.plot(x,y,'.',ms=1.0)
#plt.title("Mean=%.3f, RMS=%.3f, Number of points=%d"%(np.mean(dist), np.sqrt(np.mean(dist**2)), dist.size))
plt.xlabel("GLADE distance [Mpc]")
plt.ylabel("GWGC distance [Mpc]")
#plt.gca().set_yscale('log', nonposy='clip')
plt.savefig('distance_comaparision.png', dpi=DPI)
