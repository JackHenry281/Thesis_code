# -*- coding: utf-8 -*-
import sys
sys.path.append(r'H:\+PhD\+DFT\dft_code\Thesis_Plots')
import vars_paths as vp
sys.path.append(vp.path_functions_atmos)
import functions_raw as fr
# import functions_process as fp
# import functions_plotting as fplt

from os.path import join as jn
from atmos import Assembly
from joblib import Parallel, delayed
import time

# import os
# import multiprocessing
# import numpy as np
# from copy import deepcopy


def spectrum_CC(D):
    sim='system_mirror_C60_g_'
    #Define the path to this rotation of this spectrum series
    path_spec = jn(vp.path_H2O_g, 'H2O@C60_g_mirrored', '{0}{1}D'.format(sim,D))
    print(f'PATH={path_spec}')
    
    #Read in the parent assembly
    a = Assembly.reader(jn(path_spec, '04.00.s', 'output.aims'))
    #Add the path to the specific spectrum
    a.attach('scalar', 'path_spec', path_spec)
    #Add the paths to the steps in the spectrum
    a.attach('arbit', 'dir_steps', fr.step_paths(a['path_spec']))
    
    #Initiate the atomic indices branch
    a.attach('arbit', 'i~', [0])
    #Attach the atomic indices
    a.attach('arbit', 'i~tip'     , range( 0 , 60))
    a.attach('arbit', 'i~tip_base', range( 54, 60))
    a.attach('arbit', 'i~tip_junc', range(  0,  6))
    a.attach('arbit', 'i~srf'     , range( 60,120))
    a.attach('arbit', 'i~srf_base', range(114,120))
    a.attach('arbit', 'i~srf_junc', range( 60, 66))
    
    #Attach the angles
    a.attach('arbit', 'angle~', [0])
    #Angle given by directory system
    a.attach('scalar', 'angle~dir', D)
    #Angle of tip, if statment correts the tan function repeating every 180D
    a.attach('scalar', 'angle~tip', fr.calc_angle(a, a['i~tip_base'], 57))
    if any([D==120, D==150]):
        a['angle~tip']=a['angle~tip']+180
    #Angle of the sample
    a.attach('scalar', 'angle~srf', fr.calc_angle(a, a['i~srf_base'], 63))
    #Relative angle between the tip and sample
    a.attach('scalar', 'angle~rel', a['angle~tip']-a['angle~srf'])
    #Relative angle between the tip and sample, offset to reflect the symnmetry of the system
    a.attach('scalar', 'angle~rel_mir', a['angle~rel']-90)
    
    #Read in the spectrum step data
    z,ff,ee = fr.read_spectrum(a)
    #Attach all the spectra
    fr.attach_dics(a,z,ff,ee)
    
    #Write out the .nc file
    a.save(jn(vp.path_H2O_g, 'Plots_atmos', 'Data_raw',
                      '{0}{1}D.nc'.format(sim,D)))

def spectrum_CH(D):
    sim='system_mirror_tip_C60_g_'
    #Define the path to this rotation of this spectrum series
    path_spec = jn(vp.path_H2O_g, 'H2O@C60_g_mirrored', '{0}{1}D'.format(sim,D))
    print(f'PATH={path_spec}')
    
    #Read in the parent assembly
    a = Assembly.reader(jn(path_spec, '04.00.s', 'output.aims'))
    #Add the path to the specific spectrum
    a.attach('scalar', 'path_spec', path_spec)
    #Add the paths to the steps in the spectrum
    a.attach('arbit', 'dir_steps', fr.step_paths(a['path_spec']))
    
    #Initiate the atomic indices branch
    a.attach('arbit', 'i~', [0])
    #Attach the atomic indices
    a.attach('arbit', 'i~tip'     , range( 0 , 60))
    a.attach('arbit', 'i~tip_base', range( 54, 60))
    a.attach('arbit', 'i~tip_junc', range(  0,  6))
    a.attach('arbit', 'i~srf'     , range( 60,120))
    a.attach('arbit', 'i~srf_base', range(114,120))
    a.attach('arbit', 'i~srf_junc', range( 60, 66))
    
    #Attach the angles
    a.attach('arbit', 'angle~', [0])
    #Angle given by directory system
    a.attach('scalar', 'angle~dir', D)
    #Angle of tip, if statment correts the tan function repeating every 180D
    a.attach('scalar', 'angle~tip', fr.calc_angle(a, a['i~tip_base'], 57))
    if any([D==120, D==150]):
        a['angle~tip']=a['angle~tip']+180
    #Angle of the sample
    a.attach('scalar', 'angle~srf', fr.calc_angle(a, a['i~srf_base'], 63))
    #Relative angle between the tip and sample
    a.attach('scalar', 'angle~rel', a['angle~tip']-a['angle~srf'])
    #Relative angle between the tip and sample, offset to reflect the symnmetry of the system
    a.attach('scalar', 'angle~rel_mir', a['angle~rel']-90)
    
    #Read in the spectrum step data
    z,ff,ee = fr.read_spectrum(a)
    #Attach all the spectra
    fr.attach_dics(a,z,ff,ee)
    
    #Write out the .nc file
    a.save(jn(vp.path_H2O_g, 'Plots_atmos', 'Data_raw',
                      '{0}{1}D.nc'.format(sim,D)))

def spectrum_HH(D):
    sim='system_mirror_H2O@C60_'
    #Define the path to this rotation of this spectrum series
    path_spec = jn(vp.path_H2O_g, 'H2O@C60_g_mirrored', '{0}{1}D'.format(sim,D))
    print(f'PATH={path_spec}')
    
    #Read in the parent assembly
    a = Assembly.reader(jn(path_spec, '04.00.s', 'output.aims'))
    #Add the path to the specific spectrum
    a.attach('scalar', 'path_spec', path_spec)
    #Add the paths to the steps in the spectrum
    a.attach('arbit', 'dir_steps', fr.step_paths(a['path_spec']))
    
    #Initiate the atomic indices branch
    a.attach('arbit', 'i~', [0])
    #Attach the atomic indices
    a.attach('arbit', 'i~tip'     , range( 0 , 63))
    a.attach('arbit', 'i~tip_base', range( 54, 60))
    a.attach('arbit', 'i~tip_junc', range(  0,  6))
    a.attach('arbit', 'i~srf'     , range( 63,126))
    a.attach('arbit', 'i~srf_base', range(117,123))
    a.attach('arbit', 'i~srf_junc', range( 63, 69))
    
    #Attach the angles
    a.attach('arbit', 'angle~', [0])
    #Angle given by directory system
    a.attach('scalar', 'angle~dir', D)
    #Angle of tip, if statment correts the tan function repeating every 180D
    a.attach('scalar', 'angle~tip', fr.calc_angle(a, a['i~tip_base'], 57))
    if any([D==120, D==150]):
        a['angle~tip']=a['angle~tip']+180
    #Angle of the sample
    a.attach('scalar', 'angle~srf', fr.calc_angle(a, a['i~srf_base'], 66))
    #Relative angle between the tip and sample
    a.attach('scalar', 'angle~rel', a['angle~tip']-a['angle~srf'])
    #Relative angle between the tip and sample, offset to reflect the symnmetry of the system
    a.attach('scalar', 'angle~rel_mir', a['angle~rel']-90)
    
    #Read in the spectrum step data
    z,ff,ee = fr.read_spectrum(a)
    #Attach all the spectra
    fr.attach_dics(a,z,ff,ee)
    
    #Write out the .nc file
    a.save(jn(vp.path_H2O_g, 'Plots_atmos', 'Data_raw',
                      '{0}{1}D.nc'.format(sim,D)))

def spectrum_HH_Rotx(D):
    sim='system_Rotx_'
    #Define the path to this rotation of this spectrum series
    path_spec = jn(vp.path_H2O_g, 'H2O@C60_g_Rotx', '{0}{1}D'.format(sim,D))
    print(f'PATH={path_spec}')
    
    #Read in the parent assembly
    a = Assembly.reader(jn(path_spec, '04.00.s', 'output.aims'))
    #Add the path to the specific spectrum
    a.attach('scalar', 'path_spec', path_spec)
    #Add the paths to the steps in the spectrum
    a.attach('arbit', 'dir_steps', fr.step_paths(a['path_spec']))
    
    #Initiate the atomic indices branch
    a.attach('arbit', 'i~', [0])
    #Attach the atomic indices
    a.attach('arbit', 'i~tip'     , range(  0, 63))
    a.attach('arbit', 'i~tip_base', range(  0,  6))
    a.attach('arbit', 'i~tip_junc', range( 54, 60))
    a.attach('arbit', 'i~srf'     , range( 63,126))
    a.attach('arbit', 'i~srf_base', range(117,123))
    a.attach('arbit', 'i~srf_junc', range( 63, 69))
    
    #Attach the angles
    a.attach('arbit', 'angle~', [0])
    #Angle given by directory system
    a.attach('scalar', 'angle~dir', D)
    #Angle of tip, if statment correts the tan function repeating every 180D
    a.attach('scalar', 'angle~tip', fr.calc_angle(a, a['i~tip_base'], 0))
    if any([D==120, D==150]):
        a['angle~tip']=a['angle~tip']+180
    #Angle of the sample
    a.attach('scalar', 'angle~srf', fr.calc_angle(a, a['i~srf_base'], 66))
    #Relative angle between the tip and sample
    a.attach('scalar', 'angle~rel', a['angle~tip']-a['angle~srf'])
    #Relative angle between the tip and sample, offset to reflect the symnmetry of the system
    a.attach('scalar', 'angle~rel_mir', a['angle~rel']-90)
    
    #Read in the spectrum step data
    z,ff,ee = fr.read_spectrum(a)
    #Attach all the spectra
    fr.attach_dics(a,z,ff,ee)
    
    #Write out the .nc file
    a.save(jn(vp.path_H2O_g, 'Plots_atmos', 'Data_raw',
                      '{0}{1}D.nc'.format(sim,D)))


'''Read in the data'''
#Make the directory, kill the code if it already exists to avoid data overwrite
# os.mkdir(jn(vp.path_H2O_g, 'Plots_atmos', 'Data_raw'))

'''Read the data in parallel'''
startTime = time.time()
print('CC')  
Parallel(n_jobs=3)(delayed(spectrum_CC     )(D) for D in range(0,180,30))
print('CH')
Parallel(n_jobs=3)(delayed(spectrum_CH     )(D) for D in range(0,180,30))
print('HH')
Parallel(n_jobs=3)(delayed(spectrum_HH     )(D) for D in range(0,180,30))
print('HH_R')
Parallel(n_jobs=3)(delayed(spectrum_HH_Rotx)(D) for D in range(0,180,30))
endTime = time.time()
print('Execution Time: {0:.1f} mins'.format((endTime-startTime)/60))

# startTime = time.time()
# #leave 1 or 2 CPUs free so as to ruin my PC
# cpus=multiprocessing.cpu_count()-1
# print('CC')
# with multiprocessing.Pool(cpus) as pool:
#     pool.map(spectrum_CC  , range(0,180,30))
# print('CH')
# with multiprocessing.Pool(cpus) as pool:
#     pool.map(spectrum_CH  , range(0,180,30))
# print('HH')
# with multiprocessing.Pool(cpus) as pool:
#     pool.map(spectrum_HH  , range(0,180,30))
# print('HH_R')
# with multiprocessing.Pool(cpus) as pool:
#     pool.map(spectrum_HH_R, range(0,180,30))
# endTime = time.time()
# print('Execution Time: {0:.1f} mins'.format((endTime-startTime)/60))



