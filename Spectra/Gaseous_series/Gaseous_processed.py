# -*- coding: utf-8 -*-
import sys
sys.path.append(r'H:\+PhD\+DFT\dft_code\Thesis_Plots')
import vars_paths as vp
sys.path.append(vp.path_functions_atmos)
# import functions_raw as fr
import functions_process as fp
# import functions_plotting as fplt

from os.path import join as jn
from os import listdir,mkdir

from atmos import Assembly

path_data_raw = jn(vp.path_H2O_g, 'Plots_atmos', 'Data_raw')
path_data_pro = jn(vp.path_H2O_g, 'Plots_atmos', 'Data_processed')

#Make the folder to save the data as. Code is killed if the folder exists
# mkdir(path_data_pro)

#Iterate over the contence of the directory and extract the names of .nc files
file_systems = [x for x in listdir(path_data_raw) if x.endswith('.nc')]

#Iterate over the systems saved as .nc files
for file_system in file_systems:
    print(file_system)
    '''Read in the Assembly'''
    system = Assembly.load(jn(path_data_raw, file_system))
    '''Crop the spectrum if needed'''
    #If statement means only data which needs cropping is cropped (Rotx simulations)
    if 'Rotx' in file_system:
        print(f'Rotx: {file_system}')
        fp.crop_spectrum(system, -5)
    '''Z Scale'''
    fp.process_z_scale(system)
    '''System Energy'''
    fp.process_system_energy(system)
    '''FHI-aims Forces'''
    fp.process_FHI_forces_raw(system)
    if 'Rotx' in file_system:
        fp.process_FHI_forces_offset(system, -4)
    else:
        fp.process_FHI_forces_offset(system, -9)

    # '''Minima Data'''
    # for field in ['ee~', 'ef~', ]:
    #     fp.process_minima(system, 'ff_tip~')
    '''Save the processed Assembly as a .nc'''
    system.save(jn(path_data_pro, file_system))
