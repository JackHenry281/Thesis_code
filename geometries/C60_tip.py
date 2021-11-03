# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import vars_paths as vp
from os.path import join as jn

import os
import ase.io
import numpy as np
from ase.build import fcc111

#Read in the C60 on Cu(111) geometries
C60_r = ase.io.read(jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_r.in'))
#Position correctly
pos_r = C60_r.get_positions()
pos_r[:,2] += -np.amax(pos_r[:,2]) + 48
C60_r.set_positions(pos_r, apply_constraint=False)

C60_u = ase.io.read(jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_u.in'))
#Position correctly
pos_u = C60_u.get_positions()
pos_u[:,2] += -np.amax(pos_u[:,2]) + 48
C60_u.set_positions(pos_u, apply_constraint=False)


''' Make the reflected tip '''
# #Edit the C60_r system positions to make the tip
# t1 = ase.io.read(jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_r.in'))
# pos_t = t1.get_positions()
# pos_t[:,2] = -(pos_t[:,2]-np.amax(pos_t[:,2]))+np.amax(pos_t[:,2])+4
# t1.set_positions(pos_t, apply_constraint=False)

# #Set the cell Z unit vector to be 100
# cell = t1.get_cell()
# cell[2,2] = 100
# t1.set_cell(cell)

# #Save the geometry
# ase.io.write(jn(vp.save_geo, 'AFM_systems', 'Tip_C60_reflect.in'), t1+C60_r)

''' Make the rotated tip '''
#Edit the C60_r system positions to make the tip
t2 = ase.io.read(jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_r.in'))
t2.rotate(180, 'x')
t2.rotate(60, 'z')
pos_t = t2.get_positions()
pos_t[:,2] += -np.amin(pos_t[:,2]) + 52
t2.set_positions(pos_t, apply_constraint=False)

#Set the cell Z unit vector to be 100
cell = t2.get_cell()
cell[2,2] = 100
t2.set_cell(cell)

#Save the geometry
ase.io.write(jn(vp.save_geo, 'AFM_systems', 'Tip_C60', 'Tip_C60.in'), t2)
ase.io.write(jn(vp.save_geo, 'AFM_systems', 'Tip_C60', 'Tip_C60_r_AFM_system.in'), t2+C60_r)
ase.io.write(jn(vp.save_geo, 'AFM_systems', 'Tip_C60', 'Tip_C60_u_AFM_system.in'), t2+C60_u)

