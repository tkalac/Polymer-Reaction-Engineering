# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:36:24 2023

@author: Tine
"""

from matplotlib import pyplot as plt
import numpy as np


plt.style.use('classic')
plt.rcParams["font.family"] = "Arial"
plt.rcParams['font.size'] = 11
plt.rcParams['axes.grid'] = True
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

#   Parameters
n=5                             # s^-1
d=0.2                           # m
density_HDPE = 965              # kg/m^3
density_solvent = 680.5         # kg/m^3
viscosity_solvent = 0.0002431   # Pa s
volume_fraction_max=0.5

#   Volume fraction
volume_fraction=np.linspace(0, 0.499, 499)

#   Calculated values
density_dispersion = volume_fraction*(density_HDPE-density_solvent)+density_solvent
viscosity_relative = (1+1.25*(volume_fraction/(1-(volume_fraction/volume_fraction_max))))**2

Re=(n*d**2*density_dispersion)/(viscosity_solvent*viscosity_relative)


### PLOTS ###

fig1, ax1 = plt.subplots()
ax1.plot(volume_fraction, Re, color="black", linewidth=2)
ax1.hlines(y=10**3, xmin=0, xmax=0.5, color='red', linestyles="dashed")

for i in range(len(Re)):
    if Re[i] < 1000:
        ax1.vlines(x=volume_fraction[i], ymin=0, ymax=10**3, color='red', linestyles="dashed")
        ax1.scatter(volume_fraction[i], Re[i])
        ax1.plot([volume_fraction[i], volume_fraction[i]-0.1], [Re[i], Re[i]*0.1], color="blue")
        ax1.text(volume_fraction[i]-0.12, Re[i]*0.05, "$\Phi_{lim}=%f$"%volume_fraction[i])
        break

### Logarithmic scale
ax1.set_yscale('log')

### Figure width and height
fig1.set_figwidth(8)
fig1.set_figheight(5)

### Axis limits
ax1.set_xlim(0, 0.5)

### Labels and legends
ax1.set_title("Reynold's number for dispersion polymerization of HDPE in heptane")
ax1.set_xlabel("Volume fraction")
ax1.set_ylabel("Reynolds number")


fig1.savefig("re_phi.png", dpi=300)