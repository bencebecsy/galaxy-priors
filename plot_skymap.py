#!/usr/bin/python
import numpy as np
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

infile = sys.argv[1]
outfile = infile[:-4] + "png"
print outfile

DPI=300



m = hp.read_map(infile)
hp.mollview(m, title="Mollview image RING")

if sys.srgv[2]=='1':
    #galactic center
    hp.projscatter((17.0+45.0/60+40/3600)/24*360, -29.0-28.0/3600, lonlat=True, marker='x', label="GC")
    #Virgo cluster
    hp.projscatter((12.0+27.0/60)/24*360, 12.0+43.0/60, lonlat=True, marker='x', label="VC")
    #LMC
    hp.projscatter((5.0+23.0/60+34.5/3600)/24*360, -69.0-45.0/60-22.0/3600, lonlat=True, marker='x', label="LMC")
    #SMC
    hp.projscatter((0.0+52.0/60+44.8/3600)/24*360, -72.0-49.0/60-43.0/3600, lonlat=True, marker='x', label="SMC")
    #Andromeda
    hp.projscatter((0.0+42.0/60+44.3/3600)/24*360, 41.0+16.0/60+9.0/3600, lonlat=True, marker='x', label="And")
    #Coma cluster
    hp.projscatter((12.0+59.0/60+48.7/3600)/24*360, 27.0+58.0/60+50.0/3600, lonlat=True, marker='x', label="ComaC")
    #Leo cluster
    hp.projscatter((11.0+44.0/60+36.5/3600)/24*360, 19.0+45.0/60+32.0/3600, lonlat=True, marker='x', label="LeoC")
    #Norma cluster
    hp.projscatter((16.0+15.0/60+32.8/3600)/24*360, -60.0-54.0/60-30.0/3600, lonlat=True, marker='x', label="NormC")
    #centaurus cluster
    hp.projscatter((12.0+48.0/60+51.8/3600)/24*360, -41.0-18.0/60-21.0/3600, lonlat=True, marker='x', label="CentC")
    #Perseus cluster
    hp.projscatter((3.0+18.0/60)/24*360, 41.0+30.0/60, lonlat=True, marker='x', label="PersC")
    #Taurus void
    hp.projscatter((3.0+30.0/60)/24*360, 20.0, lonlat=True, marker='x', label="TauV")

plt.legend()
hp.graticule()
plt.savefig(outfile, dpi=DPI)
