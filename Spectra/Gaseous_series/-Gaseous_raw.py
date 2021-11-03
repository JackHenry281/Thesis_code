# -*- coding: utf-8 -*-
import sys
sys.path.append(r'H:\+PhD\+DFT\dft_code\Thesis_Plots')
import vars_paths as vp
from os.path import join as jn
from atmos import Assembly

import os
import numpy as np
from copy import deepcopy
import time

def step_paths(path_spectrum):
    #Iterate over the contence of the directory. If it is a dir, and ends in .s, then add a path
    return [x for x in os.listdir(path_spectrum)
            if all([os.path.isdir(jn(path_spectrum,x)), x[-2:]=='.s'])]

def read_steps(series):
    #Iterate over the relative rotations
    for rotation in series:
        #Iterate over the steps in the spectra for this rotation
        for path_step in rotation[2]:
            print(path_step)
            rotation[3].append(Assembly.reader(jn(path_step, 'output.aims')))

def calc_angle(a, atoms, ref_atom):
    #Copy the atomic positions
    pos = deepcopy(a["positions"].data)
    #Offset the positions
    pos += [-np.mean(pos[atoms,0]), -np.mean(pos[atoms,1]), -np.mean(pos[atoms,2])]
    #Calculate the angle and return the value
    return -np.arctan(pos[ref_atom,0] / pos[ref_atom,1]) * 180 / np.pi

def return_dics():
    z = {'zscale~':[0], 'zscale~tip_base':[], 'zscale~tip_junc':[],
         'zscale~srf_base':[], 'zscale~srf_junc':[]}
    ff = {'ff_tip~':[0], 'ff_tip~all':[], 'ff_tip~vdw':[],
          'ff_srf~':[0], 'ff_srf~all':[], 'ff_srf~vdw':[]}
    ee = {'ee~':[0], 'ee~all':[], 'ee~vdw':[]}
    return z,ff,ee

def read_spectrum(a):
    #Create empty dictionaries to store the spectra as they are built
    z,ff,ee = return_dics()
    #Read in the spectrum data by iterating over the steps
    for dir_step in a['dir_steps'].data:
        print(jn('PATH', dir_step, 'output.aims'))
        step = Assembly.reader(jn(a['path_spec'], dir_step, 'output.aims'))

        #Extract the energy spectrum
        ee['ee~all'].append(step['energies']['metal_total'   ])
        ee['ee~vdw'].append(step['energies']['vdw_correction'])

        #Create the tip_base Z scale
        z['zscale~tip_base'].append(np.mean(step['positions z'][a['i~tip_base']]))
        #Create the tip_apex Z scale
        z['zscale~tip_junc'].append(np.min (step['positions z'][a['i~tip_junc']]))
        #Create the srf_apex Z scale
        z['zscale~srf_base'].append(np.mean(step['positions z'][a['i~srf_base']]))
        #Create the srf_apex Z scale
        z['zscale~srf_junc'].append(np.max (step['positions z'][a['i~srf_junc']]))

        #Iterate over the tip and surface
        for group in ['tip', 'srf']:
            #Extract the total force
            ff[f'ff_{group}~all'].append(np.sum(step['forces z    '][a[f'i~{group}']]))
            #Extract the vdw force component
            ff[f'ff_{group}~vdw'].append(np.sum(step['forces~vdw z'][a[f'i~{group}']]))
    return z,ff,ee

def spectrum_CC_CH(D, sim):
    #Define the path to this rotation of this spectrum series
    path_spec = jn(vp.path_H2O_g, 'H2O@C60_g_mirrored', '{0}{1}D'.format(sim,D))
    print(f'PATH={path_spec}')
    
    #Read in the parent assembly
    a = Assembly.reader(jn(path_spec, '04.00.s', 'output.aims'))
    #Add the path to the specific spectrum
    a.attach('scalar', 'path_spec', path_spec)
    #Add the paths to the steps in the spectrum
    a.attach('arbit', 'dir_steps', step_paths(a['path_spec']))
    
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
    a.attach('scalar', 'angle~tip', calc_angle(a, a['i~tip_base'], 57))
    if any([D==120, D==150]):
        a['angle~tip']=a['angle~tip']+180
    #Angle of the sample
    a.attach('scalar', 'angle~srf', calc_angle(a, a['i~srf_base'], 63))
    #Relative angle between the tip and sample
    a.attach('scalar', 'angle~rel', a['angle~tip']-a['angle~srf'])
    #Relative angle between the tip and sample, offset to reflect the symnmetry of the system
    a.attach('scalar', 'angle~rel_mir', a['angle~rel']-90)
    
    #Read in the spectrum step data
    z,ff,ee = read_spectrum(a)
    #Join the dictionaries
    dic_all = z | ff | ee
    #Attach all the spectra
    for key,value in dic_all.items():
        a.attach('arbit', key, value)
    
    #Write out the .nc file
    a.save(jn(vp.path_H2O_g, 'Plots_atmos', 'Data_raw',
                      '{0}{1}D.nc'.format(sim,D)))

def spectrum_HH(D, sim):
    #Define the path to this rotation of this spectrum series
    path_spec = jn(vp.path_H2O_g, 'H2O@C60_g_mirrored', '{0}{1}D'.format(sim,D))
    print(f'PATH={path_spec}')
    
    #Read in the parent assembly
    a = Assembly.reader(jn(path_spec, '04.00.s', 'output.aims'))
    #Add the path to the specific spectrum
    a.attach('scalar', 'path_spec', path_spec)
    #Add the paths to the steps in the spectrum
    a.attach('arbit', 'dir_steps', step_paths(a['path_spec']))
    
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
    a.attach('scalar', 'angle~tip', calc_angle(a, a['i~tip_base'], 57))
    if any([D==120, D==150]):
        a['angle~tip']=a['angle~tip']+180
    #Angle of the sample
    a.attach('scalar', 'angle~srf', calc_angle(a, a['i~srf_base'], 66))
    #Relative angle between the tip and sample
    a.attach('scalar', 'angle~rel', a['angle~tip']-a['angle~srf'])
    #Relative angle between the tip and sample, offset to reflect the symnmetry of the system
    a.attach('scalar', 'angle~rel_mir', a['angle~rel']-90)
    
    #Read in the spectrum step data
    z,ff,ee = read_spectrum(a)
    #Join the dictionaries
    dic_all = z | ff | ee
    #Attach all the spectra
    for key,value in dic_all.items():
        a.attach('arbit', key, value)
    
    #Write out the .nc file
    a.save(jn(vp.path_H2O_g, 'Plots_atmos', 'Data_raw',
                      '{0}{1}D.nc'.format(sim,D)))

def spectrum_HH_Rotx(D, sim):
    #Define the path to this rotation of this spectrum series
    path_spec = jn(vp.path_H2O_g, 'H2O@C60_g_Rotx', '{0}{1}D'.format(sim,D))
    print(f'PATH={path_spec}')
    
    #Read in the parent assembly
    a = Assembly.reader(jn(path_spec, '04.00.s', 'output.aims'))
    #Add the path to the specific spectrum
    a.attach('scalar', 'path_spec', path_spec)
    #Add the paths to the steps in the spectrum
    a.attach('arbit', 'dir_steps', step_paths(a['path_spec']))
    
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
    a.attach('scalar', 'angle~tip', calc_angle(a, a['i~tip_base'], 0))
    if any([D==120, D==150]):
        a['angle~tip']=a['angle~tip']+180
    #Angle of the sample
    a.attach('scalar', 'angle~srf', calc_angle(a, a['i~srf_base'], 66))
    #Relative angle between the tip and sample
    a.attach('scalar', 'angle~rel', a['angle~tip']-a['angle~srf'])
    #Relative angle between the tip and sample, offset to reflect the symnmetry of the system
    a.attach('scalar', 'angle~rel_mir', a['angle~rel']-90)
    
    #Read in the spectrum step data
    z,ff,ee = read_spectrum(a)
    #Join the dictionaries
    dic_all = z | ff | ee
    #Attach all the spectra
    for key,value in dic_all.items():
        a.attach('arbit', key, value)
    
    #Write out the .nc file
    a.save(jn(vp.path_H2O_g, 'Plots_atmos', 'Data_raw',
                      '{0}{1}D.nc'.format(sim,D)))


startTime = time.time()
#Iterate over the angles
for D in list(range(0,180,30)):
    print(f'\n#####\nAngle: {D}')
    #Call the correct function for each system
    spectrum_CC_CH  (D, 'system_mirror_C60_g_'    )
    spectrum_CC_CH  (D, 'system_mirror_tip_C60_g_')
    spectrum_HH     (D, 'system_mirror_H2O@C60_'  )
    spectrum_HH_Rotx(D, 'system_Rotx_'            )

endTime = time.time()
print('Execution Time: {0:.1f} mins'.format((endTime-startTime)/60))
