# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import vars_paths as vp
from os.path import join as jn

from ase.io import read,write
import numpy as np

'''H2O@C60 on Cu(111), H2O@C60 tip '''
C60_u = read(jn(vp.save_geo, 'AFM_systems', 'H2O@C60', 'Tip_H2O@C60', 'C60_u', 'C60_u.in'))
#Position correctly
pos_u = C60_u.get_positions()
pos_u[:,2] += -np.amin(pos_u[:,2]) + 35.3
C60_u.set_positions(pos_u, apply_constraint=False)
#Save geometry
write(jn(vp.save_geo, 'AFM_systems', 'H2O@C60', 'Tip_H2O@C60', 'C60_u.in'), C60_u)

'''H2O@C60 on Cu(111), C60 tip '''
C60_u = read(jn(vp.save_geo, 'AFM_systems', 'H2O@C60', 'Tip_C60', 'C60_u', 'C60_u.in'))
#Position correctly
pos_u = C60_u.get_positions()
pos_u[:,2] += -np.amin(pos_u[:,2]) + 35.3
C60_u.set_positions(pos_u, apply_constraint=False)
#Save geometry
write(jn(vp.save_geo, 'AFM_systems', 'H2O@C60', 'Tip_C60', 'C60_u', 'C60_u.in'), C60_u)

'''H2O@C60 on Cu(111), Cu tip '''
C60_u = read(jn(vp.save_geo, 'AFM_systems', 'H2O@C60', 'Tip_Cu', 'C60_u', 'C60_u.in'))
#Position correctly
pos_u = C60_u.get_positions()
pos_u[:,2] += -np.amin(pos_u[:,2]) + 37.3
C60_u.set_positions(pos_u, apply_constraint=False)
#Save geometry
write(jn(vp.save_geo, 'AFM_systems', 'H2O@C60', 'Tip_Cu', 'C60_u', 'C60_u.in'), C60_u)
