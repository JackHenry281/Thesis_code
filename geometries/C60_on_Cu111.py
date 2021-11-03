# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import vars_paths as vp
from os.path import join as jn

import numpy as np
import pandas as pd
from ase.io import read,write

#Paths to geometries
path_in_u = jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_u.in')
path_in_r = jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_r.in')
#Read in geometries
u = read(path_in_u)
r = read(path_in_r)
#Position along the Z direction
pos_u = u.get_positions()
pos_u[:,2] += 10-np.amin(pos_u[:,2])
u.set_positions(pos_u, apply_constraint=False)

pos_r = r.get_positions()
pos_r[:,2] += 10-np.amin(pos_r[:,2])
r.set_positions(pos_r, apply_constraint=False)

#Set the partial charges
u_M = pd.read_csv(jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_u.csv'))['M_charge'][:108].to_numpy()
u.set_initial_charges(u_M)

r_M = pd.read_csv(jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_r.csv'))['M_charge'][:117].to_numpy()
r.set_initial_charges(r_M)

write(jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_u.xyz'), u)
write(jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_r.xyz'), r)




