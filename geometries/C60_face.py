# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import vars_paths as vp
from os.path import join as jn
from ase.io import read,write


#Read in the C60 molecule
# C60_hex = read(jn(vp.path_face, 'C60_hex.in'))

#Rotate the C60
C60_bond1 = read(jn(vp.path_face, 'C60_hex.in'))
C60_bond1.rotate(21, 'y')
write(jn(vp.path_face, 'C60_bond1.in'), C60_bond1)

#Rotate the C60
C60_bond2 = read(jn(vp.path_face, 'C60_hex.in'))
C60_bond2.rotate(62.5, 'y')
write(jn(vp.path_face, 'C60_bond2.in'), C60_bond2)

#Rotate the C60
C60_pent = read(jn(vp.path_face, 'C60_hex.in'))
C60_pent.rotate(79, 'y')
write(jn(vp.path_face, 'C60_pent.in'), C60_pent)




