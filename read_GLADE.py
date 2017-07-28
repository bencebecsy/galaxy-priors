#!/usr/bin/python
import numpy as np
from timeit import default_timer as timer
#import h5py
import sys

start = timer()

#glade = np.empty(shape=(0,26))
glade = []
print glade


itera=0
num=0
with open("GLADE_2.txt", 'r') as glade_file:
    for line in glade_file:
        L = (map(lambda x: np.nan if x=='null' else x, line.split()))
        #print L
        #columns:(0) PGC number (1) GWGC name (2) HyperLEDA name (3) 2MASS name (4) SDSS-DR12 name
        #        (5) flag1 Q/G (6) RA [deg] (7) dec [deg] (8) dist [Mpc] (9) dist_err [Mpc]
        #        (10) z (11) apparent B mag (12) B_err (13) apparent J mag (14)	J_err (15) apparent H mag
        #        (16) H_err (17) apparent K mag (18) K_err (19) flag2 	0: no measured dist or z 1: measured z 2: measured dist
        #        (20) flag3 0: measured B mag 1: ML estimated B mag (21) B_err_min (22) B_err_max
        #        (23) flag4 0: z from measured dist 1: ML estimated z (24) z_err_min (25) z_err_max
        L = L[0:6] + [float(i) for i in L[6:19]] + [int(L[19])] + [int(L[20])] + [float(L[21])] + [float(L[22])] + [int(L[23])] + [float(L[24])] + [float(L[25])]
        #if (L[11]<5.0):
        #if (L[8]<0.0):
        #if (L[13]>60.0):
        #if (L[15]>60.0):
        if (L[8]>0.0 and L[8]<50.0):
        #if True:
            glade += L
            num += 1
        #print glade
        itera+=1
        if itera%10000==0:
            print itera
        
glade = np.array(glade)
glade = np.reshape(glade, (num,26))

print glade
print glade.shape

outfile = sys.argv[1]

np.save(outfile, glade)

#h5f = h5py.File('gx_list_glade.hdf5', 'w')
#h5f.create_dataset('dataset_1', data=glade)
#h5f.close()


end = timer()
print "Elapsed time: %r seconds" %(end-start)
