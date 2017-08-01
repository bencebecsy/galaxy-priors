#!/usr/bin/python
import numpy as np
import sys

infile = sys.argv[1]
targeting_file = sys.argv[2]

glade = np.load(infile)

#columns:(0) PGC number (1) GWGC name (2) HyperLEDA name (3) 2MASS name (4) SDSS-DR12 name
        #        (5) flag1 Q/G (6) RA [deg] (7) dec [deg] (8) dist [Mpc] (9) dist_err [Mpc]
        #        (10) z (11) apparent B mag (12) B_err (13) apparent J mag (14)	J_err (15) apparent H mag
        #        (16) H_err (17) apparent K mag (18) K_err (19) flag2 	0: no measured dist or z 1: measured z 2: measured dist
        #        (20) flag3 0: measured B mag 1: ML estimated B mag (21) B_err_min (22) B_err_max
        #        (23) flag4 0: z from measured dist 1: ML estimated z (24) z_err_min (25) z_err_max

name1 = glade[:,0].astype(str)
name2 = glade[:,1].astype(str)
name3 = glade[:,2].astype(str)
name4 = glade[:,3].astype(str)
name5 = glade[:,4].astype(str)
ra = glade[:,6].astype(float)
dec = glade[:,7].astype(float)
dist = glade[:,8].astype(float)
b = glade[:,11].astype(float)



old_gxs = []
outfile = "targeting" + targeting_file[8:]
outfile_old = outfile[:-4] + "_old" + outfile[-4:]
outfile_diff = outfile[:-4] + "_diff" + outfile[-4:]
with open(outfile_old) as of_o:
    lines = of_o.readlines()[:-1]
    for line in lines:
        if line != "--------------------------------------------------------\n" and line !=' \n':
            if line.split()[0]!="Pixel":
                old_gxs.append(line.split()[1])

print old_gxs

out = open(outfile, "w")
out_diff = open(outfile_diff, 'w')


with open(targeting_file) as targ_file:
    #skyID  theta   DEC     step   phi     R.A    step  probability    cumulative
    #ending = -158
    ending = -159
    lines = targ_file.readlines()[68:ending]
    print lines
    for i, line in enumerate(lines):
        l = np.array(line.strip().split()).astype(float)
        ra_cent = l[5]
        ra_step = l[6]
        dec_cent = l[2]
        dec_step = l[3]
        
        mask = (ra>ra_cent-ra_step/2)*(ra<ra_cent+ra_step/2)*(dec>dec_cent-dec_step/2)*(dec<dec_cent+dec_step/2)
        if name1[mask].size!=0:
            out.write("--------------------------------------------------------\n")
            out_diff.write("--------------------------------------------------------\n")
            out.write("Pixel %d R.A.: %f decl: %f\n"%(i+1, ra_cent, dec_cent))
            out_diff.write("Pixel %d R.A.: %f decl: %f\n"%(i+1, ra_cent, dec_cent))
            for i in range(name1[mask].size):
                out.write("%s %s %s %s %s %f %f\n"%(name1[mask][i],name2[mask][i],name3[mask][i],name4[mask][i],name5[mask][i],ra[mask][i],dec[mask][i]))
                if name2[mask][i] not in old_gxs:
                    out_diff.write("%s %s %s %s %s %f %f\n"%(name1[mask][i],name2[mask][i],name3[mask][i],name4[mask][i],name5[mask][i],ra[mask][i],dec[mask][i]))
                else:
                    old_gxs = filter(lambda x: x!=name2[mask][i], old_gxs)
            out.write("--------------------------------------------------------\n")
            out_diff.write("--------------------------------------------------------\n")
            out.write("\n")
            out_diff.write("\n")

out_diff.write("Not found in GLADE:%r\n"%old_gxs)

        

out_diff.close()
out.close()
