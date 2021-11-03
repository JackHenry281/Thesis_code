# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import vars_paths as vp
from os.path import join as jn

import ase.io
import numpy as np

#Read in the C60 on Cu(111) geometries
C60_r = ase.io.read(jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_r.in'))
#Position correctly
pos_r = C60_r.get_positions()
pos_r[:,2] += -np.amax(pos_r[:,2]) + 49
C60_r.set_positions(pos_r, apply_constraint=False)

C60_u = ase.io.read(jn(vp.save_geo, 'C60_on_Cu(111)', 'C60_u.in'))
#Position correctly
pos_u = C60_u.get_positions()
pos_u[:,2] += -np.amax(pos_u[:,2]) + 49
C60_u.set_positions(pos_u, apply_constraint=False)

''' Make the systems'''
tip = ase.io.read(jn(vp.save_geo, 'AFM_systems', 'Tip_CO', 'Tip_CO.in'))
tip_pos = tip.get_positions() - tip.get_positions()[-1]
tip.set_positions(tip_pos, apply_constraint=False)

#C60_u system
u = tip.copy()
u_pos = u.get_positions()
u_pos += np.array([np.mean(pos_u[:,0][48:54]), np.mean(pos_u[:,1][48:54]), 53])
u.set_positions(u_pos, apply_constraint=False)
ase.io.write(jn(vp.save_geo, 'AFM_systems', 'Tip_CO', 'Tip_CO_u_AFM_system.in'), u+C60_u)

#C60_r system
r = tip.copy()
r_pos = r.get_positions()
r_pos += np.array([np.mean(pos_r[:,0][57:63]), np.mean(pos_r[:,1][57:63]), 53])
r.set_positions(u_pos, apply_constraint=False)
ase.io.write(jn(vp.save_geo, 'AFM_systems', 'Tip_CO', 'Tip_CO_r_AFM_system.in'), r+C60_r)



