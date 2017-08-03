#!/bin/sh


generate_skymap_prior.py gx_list_200Mpc_filtered.npy 64 lum 1 0 0 0
plot_skymap.py gx_prior_0.0-200.0Mpc_NSIDE64_w-lumB1.0J0.0H0.0K0.0.fits 1
prob-area_chist.py gx_prior_0.0-200.0Mpc_NSIDE64_w-lumB1.0J0.0H0.0K0.0.fits

#generate_skymap_prior.py gx_list_200Mpc_filtered.npy 64 lum 0 1 0 0
#plot_skymap.py gx_prior_0.0-200.0Mpc_NSIDE64_w-lumB0.0J1.0H0.0K0.0.fits 0
#prob-area_chist.py gx_prior_0.0-200.0Mpc_NSIDE64_w-lumB0.0J1.0H0.0K0.0.fts

#generate_skymap_prior.py gx_list_200Mpc_filtered.npy 64 lum 0 0 1 0
#plot_skymap.py gx_prior_0.0-200.0Mpc_NSIDE64_w-lumB0.0J0.0H1.0K0.0.fits 0
#prob-area_chist.py gx_prior_0.0-200.0Mpc_NSIDE64_w-lumB0.0J0.0H1.0K0.0.fits

#generate_skymap_prior.py gx_list_200Mpc_filtered.npy 64 lum 0 0 0 1
#plot_skymap.py gx_prior_0.0-200.0Mpc_NSIDE64_w-lumB0.0J0.0H0.0K1.0.fits 0
#prob-area_chist.py gx_prior_0.0-200.0Mpc_NSIDE64_w-lumB0.0J0.0H0.0K1.0.fits

#generate_skymap_prior.py gx_list_200Mpc_filtered.npy 64 lum 1 1 1 1
#plot_skymap.py gx_prior_0.0-200.0Mpc_NSIDE64_w-lumB1.0J1.0H1.0K1.0.fits 0
#prob-area_chist.py gx_prior_0.0-200.0Mpc_NSIDE64_w-lumB1.0J1.0H1.0K1.0.fits



all_png_to_public.sh
