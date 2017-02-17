# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
import MDAnalysis as mda
import numpy as np 
import pytim
from pytim import *
from pytim.datafiles import *

u         = mda.Universe(WATER_GRO)
oxygens   = u.select_atoms("name OW") 
radii     = pytim_data.vdwradii(G43A1_TOP)

interface = pytim.ITIM(u,alpha=2.,max_layers=1,multiproc=True)
stats     = observables.LayerTriangulation(u,interface,return_triangulation=False)
interface.assign_layers()
print stats.compute()


bins, avg = profile.profile(binwidth=0.2)
np.savetxt('intrdist.dat',list(zip(bins,avg)))

#subset=oxygens[::100]
#print subset
#tri, index = pytim.distance_from_planar_set(subset,layer)
#print tri
#print index,len(index)
#
#pytim.lap()
#
#import matplotlib.pyplot as plt
#plt.triplot(layer.positions[:,0], layer.positions[:,1],tri.simplices.copy())
#plt.plot(subset.positions[:,0], subset.positions[:,1], 'o')
#plt.triplot(layer.positions[:,0], layer.positions[:,1],tri.simplices[index].copy(),lw=4)
#plt.show()
    


