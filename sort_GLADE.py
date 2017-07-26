import numpy as np
from timeit import default_timer as timer

start = timer()

#use columns: 7: RA, 8:dec, 9:dist, 12:B, 14:J, 16:H, 18:K (all magnitudes are appearent)
#glade = np.genfromtxt("GLADE_2.txt",usecols=(5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21), max_rows=100000)
glade = np.genfromtxt("GLADE_2.txt",usecols=(6,7,8,11,13,15,17))


glade_sorted = glade[glade[:,2].argsort()]

#print glade_sorted

np.save("gx_list_glade", glade_sorted)

#typical runtime is few minutes (2-5)

end = timer()
print "Elapsed time: %r seconds" %(end-start)
