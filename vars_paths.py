# -*- coding: utf-8 -*-
from os.path import join as jn

#Folder with all the code
path_code=r'H:\+PhD\+DFT\dft_code\Thesis_Plots' 
#Thesis folder containing the plots
path_thesis=r'H:\OneDrive - University of Leeds\PhD\Thesis\pyjmlh_Thesis_LyX\classicthesis-LyX-v4.6\gfx'

#Path to atmos functions
path_functions_atmos=jn(path_code, 'Spectra', 'functions_atmos')

#Absolute path to the +DFT folder where all DFT data is stored
data_DFT=r'H:\+PhD\+DFT'
data_ArcC=jn(data_DFT, 'Arc4.d', 'C60_on_Cu(111)')
#Relative paths to the Cu bulk convergence data
data_Cu_a=jn(data_DFT, 'Arc4.d', 'C60_on_Cu(111)', 'Cu_lattice_vector')
data_Cu_k=jn(data_DFT, 'Arc4.d', 'C60_on_Cu(111)', 'Cu_k_points')
#Relative paths to the C60 adsorption on Cu(111) data
data_ads_r=jn(data_DFT, 'C60_on_Cu(111)', 'C60_r_Cu(111)', 'C60_r_Cu(111)_fcc',
              'C60_r_slab_convergence', 'Slab_Layer_Convergence')
data_ads_u=jn(data_DFT, 'C60_on_Cu(111)', 'C60_u_Cu(111)',
              'C60_u_slab_convergence', 'Slab_Layer_Convergence')
data_rot_r=jn(data_DFT, 'C60_on_Cu(111)', 'C60_r_Cu(111)', 'C60_r_Cu(111)_fcc',
              'C60_r_Cu(111)x(4,4,7)', 'Rotations')
data_rot_u=jn(data_DFT, 'C60_on_Cu(111)', 'C60_u_Cu(111)',
              'C60_u_Cu(111)x(4,4,6)_fcc', 'Rotations')

#Relative path to tip convergence data
data_tip  =jn(data_DFT, 'C60_on_Cu(111)', 'Tip_Convergence',
              'Tip_Layers_Convergence')

#Paths to saves
#Paths to the Cu bulk convergence data
save_Cu_a=jn(path_thesis, 'Cu_lattice_vector')
save_Cu_k=jn(path_thesis, 'Cu_kpoints')

save_geo=jn(path_thesis, 'geometries')

#Paths to the C60 adsorption on Cu(111) data
save_ads_1=jn(data_DFT, 'C60_on_Cu(111)', '+Thesis_Plots', 'Convergence_Adsorption')
save_ads_2=jn(path_thesis, 'Adsorption_Convergence')


#Paths to gaseous H2O simulation series
path_H2O_g=jn(data_DFT, 'H20@C60', 'H2O@C60_g')

#Path to the C60 faces plots
path_face=jn(path_thesis, 'geometries', 'C60_Face')
