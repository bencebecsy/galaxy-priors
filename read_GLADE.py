#!/usr/bin/python
import numpy as np
from timeit import default_timer as timer
#import h5py

start = timer()

#glade = np.empty(shape=(0,26))
glade = []
print glade

dt1=0
dt2=0
dt3=0

itera=0
num=0
with open("GLADE_2.txt", 'r') as glade_file:
    for line in glade_file:
        time1 = timer()
        L = (map(lambda x: np.nan if x=='null' else x, line.split()))
        time2=timer()
        #print L
        #columns:(0) PGC number (1) GWGC name (2) HyperLEDA name (3) 2MASS name (4) SDSS-DR12 name
        #        (5) flag1 Q/G (6) RA [deg] (7) dec [deg] (8) dist [Mpc] (9) dist_err [Mpc]
        #        (10) z (11) apparent B mag (12) B_err (13) apparent J mag (14)	J_err (15) apparent H mag
        #        (16) H_err (17) apparent K mag (18) K_err (19) flag2 	0: no measured dist or z 1: measured z 2: measured dist
        #        (20) flag3 0: measured B mag 1: ML estimated B mag (21) B_err_min (22) B_err_max
        #        (23) flag4 0: z from measured dist 1: ML estimated z (24) z_err_min (25) z_err_max
        L = L[0:6] + [float(i) for i in L[6:19]] + [int(L[19])] + [int(L[20])] + [float(L[21])] + [float(L[22])] + [int(L[23])] + [float(L[24])] + [float(L[25])]
        #L = L[0:6] + [float(i) for i in L[6:19]] + [int(L[19])] # shorter version to save memory (last 6 column lesf out)
        time3=timer()
        #if (L[8]>0.0 and L[8]<100.0):
        #if (L[8]<100.0 and L[8]>0.0):
        if True:
            glade += L
            num += 1
        time4=timer()
        #print glade
        itera+=1
        dt1+=time2-time1
        dt2+=time3-time2
        dt3+=time4-time3
        if itera%10000==0:
            print itera
            print dt1, dt2, dt3
        
glade = np.array(glade)
glade = np.reshape(glade, (num,26))

print glade
print glade.shape

np.save("gx_list_glade.npy", glade)

#h5f = h5py.File('gx_list_glade.hdf5', 'w')
#h5f.create_dataset('dataset_1', data=glade)
#h5f.close()


end = timer()
print "Elapsed time: %r seconds" %(end-start)
