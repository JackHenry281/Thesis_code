# -*- coding: utf-8 -*-
from os.path import join as jn
from atmos import Assembly

import os
import numpy as np
from copy import deepcopy

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
    ff = {'ff_tip~':[0], 'ff_tip~all_ev':[], 'ff_tip~vdw_ev':[],
          'ff_srf~':[0], 'ff_srf~all_ev':[], 'ff_srf~vdw_ev':[]}
    ee = {'ee_raw~':[0], 'ee_raw~all':[], 'ee_raw~vdw':[]}
    return z,ff,ee

def read_spectrum(a):
    #Create empty dictionaries to store the spectra as they are built
    z,ff,ee = return_dics()
    #Read in the spectrum data by iterating over the steps
    for dir_step in a['dir_steps'].data:
        # print(jn('PATH', dir_step, 'output.aims'))
        step = Assembly.reader(jn(a['path_spec'], dir_step, 'output.aims'))

        #Extract the energy spectrum
        ee['ee_raw~all'].append(step['energies']['metal_total'   ])
        ee['ee_raw~vdw'].append(step['energies']['vdw_correction'])

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
            ff[f'ff_{group}~all_ev'].append(np.sum(step['forces z    '][a[f'i~{group}']]))
            #Extract the vdw force component
            ff[f'ff_{group}~vdw_ev'].append(np.sum(step['forces~vdw z'][a[f'i~{group}']]))
    return z,ff,ee

def attach_dics(a, z, ff, ee):
    #Iterate over the z dictionary
    for key,value in z .items():
        attach_dic_spec(a, key, value, 'A')
    #Iterate over the ff dictionary
    for key,value in ff.items():
        attach_dic_spec(a, key, value, 'eV/A')
    #Iterate over the ee dictionary
    for key,value in ee.items():
        attach_dic_spec(a, key, value, 'eV')

def attach_dic_spec(a, key, value, unit):
    #Attach the spectrum
    a.attach('arbit', key, value)
    #Add the unit
    a[key].attrs['unit']=unit