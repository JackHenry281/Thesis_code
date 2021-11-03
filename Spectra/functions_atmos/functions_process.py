# -*- coding: utf-8 -*-
import sys
sys.path.append(r'H:\+PhD\+DFT\dft_code\Thesis_Plots')
import vars_paths as vp
from os.path import join as jn
from atmos import Assembly
from atmos.helpers.constants import eV_angstroem2nN

import numpy as np
from scipy import integrate

''' Admin '''
def check_field_key(field):
    #Check for ~ and add if nessessary
    if field[-1]!='~':
        print(f'WARNING: ~ not in field name {field}.\n    Changed {field} to {field}~')
        print('This change is not required, but recommended')        
        return field+'~'
    #Return unchanged field if its adequate
    else:
        return field

def get_data_field(a, field):
    #Check for ~ and add if nessessary
    field = check_field_key(field)
    #Get all the quantities belonging to a particular data field
    #1) Check if the quantity key .startswith() the field
    #2) Check the quantity key is longer than the field key
    #3) If True for both, 
    return [x for x in a.quantities if all([x.startswith(field), len(x)>len(field)])]

''' Attach Data '''
def attach_field(a, field, value=[0]):
    #Check for ~ and add if nessessary
    field = check_field_key(field)
    #Attach the empty field
    a.attach('arbit', field, value)

def attach_force(a, key_Z, key_Uz, key_name):
    #Calculate the change in Z
    dz = (a[key_Z ].data-np.roll(a[key_Z ].data, -1))[:-1]
    #Calculate the change in energy
    dU = (a[key_Uz].data-np.roll(a[key_Uz].data, -1))[:-1]
    # F_eV = -dU/dz
    #Calculate the force (differential )in nN and attach
    a.attach('arbit', key_name, np.append(-(dU/dz)*eV_angstroem2nN, np.nan)) #unit:nN
    #Add the unit
    a[key_name].attrs['unit']='nN'

def attach_potential(a, key_Z, key_Fz, key_name):
    #Input=eV/A, Output=eV
    #Flip z and Fz so we intrgate from Z=Zmax towards the surface
    #Preform the cumulative (definate) integral using the trapeze rule
    a.attach('arbit', key_name,
                    np.flip(integrate.cumtrapz(y=-np.flip(a[key_Fz].data),
                                               x= np.flip(a[key_Z ].data),
                                                   initial=0)))
    a[key_name].attrs['unit']='eV'

def eVA_to_nN(a, key):
    #Convert from eV/A to nN
    a.attach('arbit', key[:-3], a[key]*eV_angstroem2nN)
    #Add the unit
    a[key].attrs['unit']='nN'

def process_z_scale(a):
    #Calculate the junction separation offset
    a.attach('arbit', 'zscale~junc', a['zscale~tip_junc'].data-
                                     a['zscale~srf_junc'].data)
    #Calculate the tip base height offset by the starting junction separation
    a.attach('arbit', 'zscale~tip_base_offset_junc',
                  a['zscale~tip_base']-np.amax(a['zscale~tip_base'])+
                  a['zscale~junc'][-1])

def crop_spectrum(a, i_end):
    #if statement to check the format of the inputs
    if not i_end: #Skip if given False
        pass
    elif i_end>=0: #Print error if given an integer greater than 1
        print('Error: i_end needs to be <0 or False')
    else: #Crop the data if given a negaive integer
        #Iterate over the different data fields which need to be cropped
        for field in ['zscale~', 'ee~', 'ef~', 'ee_raw~', 'ff_tip~', 'fe_tip~', 'ff_srf~',
                      'fe_srf~']:
            #Iterate over the keys in each data field
            for key in get_data_field(a, field):
                a[key] = a[key][:i_end]

def process_system_energy(a, offset_index=-1, zscale='zscale~tip_base'):
    #Calculate the dft energy
    a.attach('arbit', 'ee_raw~dft', a['ee_raw~all'].data-
                                    a['ee_raw~vdw'].data)
    #Create the offset energy field
    attach_field(a, 'ee~')
    #Create the system energy force field
    attach_field(a, 'ef~', value=[zscale])
    #Calculate and attach the offset system energies and forces
    for key in get_data_field(a, 'ee_raw~'):
        #Offset system energy
        a.attach('arbit', f'ee~{key[7:]}', a[key]-a[key][offset_index])
        #System energy forces
        attach_force(a, zscale, key, f'ef~{key[7:]}')

def process_FHI_forces_raw(a, zscale='zscale~tip_base'):
    #Create the FHI-aims forces energy fields
    attach_field(a, 'fe_tip~', [zscale])
    attach_field(a, 'fe_srf~', [zscale])
    #Calculate the dft forces
    a.attach('arbit', 'ff_tip~dft_ev', a['ff_tip~all_ev'].data-a['ff_tip~vdw_ev'].data)
    a.attach('arbit', 'ff_srf~dft_ev', a['ff_srf~all_ev'].data-a['ff_srf~vdw_ev'].data)
    #Iterate over the forces stored in units eV/A
    for key in get_data_field(a,'ff_tip~')+get_data_field(a,'ff_srf~'):
        #Convert the FHI-aims forces from eV/A to nN
        eVA_to_nN(a, key)
        #Calculate and attach the potentials via integration
        attach_potential(a, zscale, key, f'fe{key[2:-3]}')

def process_FHI_forces_offset(a, i_start, offset_type='dft', zscale='zscale~tip_base'):
    #Checking input formatsp
    if i_start>0:
        print('WARNING: It is recomended i_start<0 as dft datasets often'+
              'start at the same height but end at different heights')
    #Iterate over the tip and sample forces
    for field in ['tip', 'srf']:
        #Attach the offset FHI-aims forces datafield
        a.attach('arbit', f'ff_{field}_offset~', [offset_type])
        #Iterate over the total and dft forces
        for key in ['all', 'dft']:
            #Iterate over the nn and ev units:
                for unit in ['', '_ev']:
                    #Attach the offset data. Offset by an average of the last
                    #points. Number of points is specified by i_start
                    a.attach('arbit', f'ff_{field}_offset~{key}{unit}',
                                a[f'ff_{field}~{key}{unit}'        ].data-
                        np.mean(a[f'ff_{field}~{offset_type}{unit}'].data[i_start:]))
        #Create the offset FHI-aims forces energy fields via integration
        attach_field(a, f'fe_{field}_offset~', value=[zscale])
        #Iterate over the keys in the datafield
        for key in get_data_field(a,f'ff_{field}_offset~'):
            #Only integrate the forces given in ev
            if key.endswith('_ev'):
                #Calculate and attach the potentials
                attach_potential(a, zscale, key, f'fe{key[2:-3]}')
        #Copy over the vdw data to make the names consistant for automated plotting
        a.attach('arbit', f'ff_{field}_offset~vdw'   , a[f'ff_{field}~vdw'   ])
        a.attach('arbit', f'ff_{field}_offset~vdw_ev', a[f'ff_{field}~vdw_ev'])
        a.attach('arbit', f'fe_{field}_offset~vdw'   , a[f'fe_{field}~vdw'   ])

def process_minima(a, field):
    #Add ~ to the field if it was omitted
    field=check_field_key(field)
    #Create the field and attach the minima index as the value
    # print(f'{field[:-1]}_min~')
    # print(f'{field}all')
    # print(np.argmin(a[f'{field}all'].data))
    # print(np.  amin(a[f'{field}all'].data))
    
    a.attach('arbit', f'{field[:-1]}_min~', np.argmin(a[f'{field}all'].data))
    

    
    
    
    