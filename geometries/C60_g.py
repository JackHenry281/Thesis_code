# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import vars_paths as vp
from os.path import join as jn

import os
import ase.io
import numpy as np
from ase.build import fcc111

#Read in the C60_g and set the junction separation to 4AA
C60_g = ase.io.read(jn(vp.save_geo, 'AFM_systems', 'C60_g', 'C60_g.in'))
#Position correctly
pos_g = C60_g.get_positions()
#Offset atoms with Z>0.1 so that the minimum Z of those atoms is 4AA
pos_g[:,2][pos_g[:,2]>0.1] += 4-np.amin(pos_g[:,2][pos_g[:,2]>0.1])
C60_g.set_positions(pos_g, apply_constraint=False)

#Save the geometry
ase.io.write(jn(vp.save_geo, 'AFM_systems', 'C60_g', 'C60_g.in'), C60_g)
