# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import vars_paths as vp
from os.path import join as jn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import ase
from ase.io import read

''' Genreating the data '''
def calc_angle(path_sys, atom_ref):
    try:
        #Read in the full system
        sys = read(path_sys, format='aims')
        #Extract the C60
        mol = sys[sys.get_atomic_numbers()==6]
        #Offset the system geometry so the centre of mass of the C60 is at (0,0,0)
        sys_pos = sys.get_positions() - np.mean(mol.get_positions(), 0)
        sys.set_positions(sys_pos, apply_constraint=False)
        #Calculate the azimuthal angle of the reference atom to the cartezian y axis, clockwise=negative
        return -np.arctan(sys_pos[atom_ref][0]/sys_pos[atom_ref][1])*180/np.pi
    except FileNotFoundError:
        return np.nan

def calc_energy(path_sys):
    #Read in the output.aims file
    try:
        with open(path_sys, 'r') as file:
            lines = file.readlines()
        #Iterate over the lines in reverse order
        for line in lines[::-1]:
            #Read in the energy and break the loop
            if '| Final zero-broadening corrected energy (caution - metals only) :' in line:
                return np.float64(line.split()[10])
                break
    except FileNotFoundError:
        return np.nan

def calc_Hirsh(path_sys):
    try:
        #Read in the output.aims file
        with open(path_sys, 'r') as file:
            lines = file.readlines()
        #Initiate the charge and counting lists
        H=[None]*60
        n=0
        #Iterate over the lines from bottom to top
        for line in lines[::-1]:
            #Read in the charge
            if '|   Hirshfeld charge' in line:
                H[n]=np.float64(line.split()[4])
                n=n+1
            #Break the loop at the end of the C60 molecule and return the total charge
            if n==60:
                return np.sum(H)
                break
    except FileNotFoundError:
        return np.nan


#Read the rotation data
D_u = ['0D', '15D', '30D', '45D', '60D', '75D', '90D', '105D', '115D']
dic_u_l = {'D_in': [], 'D_out': [], 'E_raw': [], 'E_off': [], 'H_C60': []}
dic_u_t = {'D_in': [], 'D_out': [], 'E_raw': [], 'E_off': [], 'H_C60': []}
atom_ref_u = 99        #Reference atom to calculate the angle for relative to the y axis

#Light settings
for a in D_u:
    #Starting angle
    dic_u_l['D_in' ].append(calc_angle (jn(vp.data_rot_u, a, a+'_light', 'geometry.in'), atom_ref_u))
    #Relaxed angle
    dic_u_l['D_out'].append(calc_angle (jn(vp.data_rot_u, a, a+'_light', 'geometry.in.next_step'), atom_ref_u))
    #Relaxed Energy
    dic_u_l['E_raw'].append(calc_energy(jn(vp.data_rot_u, a, a+'_light', 'output.aims')))
    #Relaxed H charge
    dic_u_l['H_C60'].append(calc_Hirsh (jn(vp.data_rot_u, a, a+'_light', 'output.aims')))
#Offset energy
dic_u_l['E_off'] = np.array(dic_u_l['E_raw']) - np.nanmin(dic_u_l['E_raw'])
#Correct tan function not going above 90D
dic_u_l['D_in' ][7] = dic_u_l['D_in' ][7]+180; dic_u_l['D_in' ][8] = dic_u_l['D_in' ][8]+180;
dic_u_l['D_out'][7] = dic_u_l['D_out'][7]+180; dic_u_l['D_out'][8] = dic_u_l['D_out'][8]+180;
#Save as pandas array
pd_u_l = pd.DataFrame.from_dict(dic_u_l)
pd_u_l.to_csv(jn(vp.path_thesis, 'geometries', 'C60_on_Cu(111)', 'rotation', 'C60_u_light.csv'))

#Tight settings
for a in D_u:
    #Starting angle
    dic_u_t['D_in' ].append(calc_angle (jn(vp.data_rot_u, a, a+'_tight', 'geometry.in'), atom_ref_u))
    #Relaxed angle
    dic_u_t['D_out'].append(calc_angle (jn(vp.data_rot_u, a, a+'_tight', 'geometry.in.next_step'), atom_ref_u))
    #Relaxed Energy
    dic_u_t['E_raw'].append(calc_energy(jn(vp.data_rot_u, a, a+'_tight', 'output.aims')))
    #Relaxed H charge
    dic_u_t['H_C60'].append(calc_Hirsh (jn(vp.data_rot_u, a, a+'_tight', 'output.aims')))
#Offset energy
dic_u_t['E_off'] = np.array(dic_u_t['E_raw']) - np.nanmin(dic_u_t['E_raw'])
#Correct tan function not going above 90D
dic_u_t['D_in' ][7] = dic_u_t['D_in' ][7]+180; dic_u_t['D_in' ][8] = dic_u_t['D_in' ][8]+180;
dic_u_t['D_out'][7] = dic_u_t['D_out'][7]+180; dic_u_t['D_out'][8] = dic_u_t['D_out'][8]+180;
#Save as pandas array
pd_u_t = pd.DataFrame.from_dict(dic_u_t)
pd_u_t.to_csv(jn(vp.path_thesis, 'geometries', 'C60_on_Cu(111)', 'rotation', 'C60_u_tight.csv'))


#Read the rotation data
D_r = ['0D', '15D', '25D', '30D', '60D', '90D', '105D']
dic_r_l = {'D_in': [], 'D_out': [], 'E_raw': [], 'E_off': [], 'H_C60': []}
dic_r_t = {'D_in': [], 'D_out': [], 'E_raw': [], 'E_off': [], 'H_C60': []}
atom_ref_r = 108        #Reference atom to calculate the angle for relative to the y axis

#Light settings
for a in D_r:
    #Starting angle
    dic_r_l['D_in' ].append(calc_angle (jn(vp.data_rot_r, a, a+'_light', 'geometry.in'), atom_ref_r))
    #Relaxed angle
    dic_r_l['D_out'].append(calc_angle (jn(vp.data_rot_r, a, a+'_light', 'geometry.in.next_step'), atom_ref_r))
    #Relaxed Energy
    dic_r_l['E_raw'].append(calc_energy(jn(vp.data_rot_r, a, a+'_light', 'output.aims')))
    #Relaxed H charge
    dic_r_l['H_C60'].append(calc_Hirsh (jn(vp.data_rot_r, a, a+'_light', 'output.aims')))
#Offset energy
dic_r_l['E_off'] = np.array(dic_r_l['E_raw']) - np.nanmin(dic_r_l['E_raw'])
#Correct tan function not going above 90D
dic_r_l['D_in' ][6] = dic_r_l['D_in' ][6]+180; dic_r_l['D_out'][6] = dic_r_l['D_out'][6]+180;
#Save as pandas array
pd_r_l = pd.DataFrame.from_dict(dic_r_l)
pd_r_l.to_csv(jn(vp.path_thesis, 'geometries', 'C60_on_Cu(111)', 'rotation', 'C60_r_light.csv'))

#Tight settings
for a in D_r:
    #Starting angle
    dic_r_t['D_in' ].append(calc_angle (jn(vp.data_rot_r, a, a+'_tight', 'geometry.in'), atom_ref_r))
    #Relaxed angle
    dic_r_t['D_out'].append(calc_angle (jn(vp.data_rot_r, a, a+'_tight', 'geometry.in.next_step'), atom_ref_r))
    #Relaxed Energy
    dic_r_t['E_raw'].append(calc_energy(jn(vp.data_rot_r, a, a+'_tight', 'output.aims')))
    #Relaxed H charge
    dic_r_t['H_C60'].append(calc_Hirsh (jn(vp.data_rot_r, a, a+'_tight', 'output.aims')))
#Offset energy
dic_r_t['E_off'] = np.array(dic_r_t['E_raw']) - np.nanmin(dic_r_t['E_raw'])
#Correct tan function not going above 90D
dic_r_t['D_in' ][6] = dic_r_t['D_in' ][6]+180; dic_r_t['D_out'][6] = dic_r_t['D_out'][6]+180;
#Save as pandas array
pd_r_t = pd.DataFrame.from_dict(dic_r_t)
pd_r_t.to_csv(jn(vp.path_thesis, 'geometries', 'C60_on_Cu(111)', 'rotation', 'C60_r_tight.csv'))





''' Plotting the data '''
plt.rcParams.update({'font.size':22})
def plot_adsorb(ax, D_in, D_out, yspan=[0,1], color='r'):
    shade = ax.fill_between([D_in, D_out, D_out],
                            [yspan[1], yspan[1], yspan[0]],
                            [yspan[1], yspan[0], yspan[0]],
                            color=color, alpha=0.25)
    line = ax.plot([D_in, D_out], [yspan[1], yspan[0]], color=color)
    return shade,line


#Global plot lims
all_xlims = [-10, 125]
E_ylims   = [-0.02, 0.35]

'''Code for C60_r'''
#Set up the figure and subplots
fig0, axs =  plt.subplots(3,1, sharex=True, sharey=False, gridspec_kw={'hspace': 0, 'wspace':0})
fig0.set_size_inches([18,10])
#Set the x and y tick locations
ax = axs[0]
ax.tick_params(axis='x', bottom=False, top=True, labelbottom=False, labeltop=True)
ax.tick_params(axis='y', left=False, labelleft=False)

#Plotting the direct and infered adsorptions
for _n,_i in enumerate(pd_r_l['D_in']):
    shade,line = plot_adsorb(ax, pd_r_l['D_in' ][_n], pd_r_l['D_out'][_n])
#Plot the angles every 15D and set the x ticks and labels
x = np.arange(0,135,15)
ax.set_xticks(x)
R_in  = ax.plot(x, np.linspace(1,1,9), 'ro')
R_out = ax.plot(x, np.linspace(0,0,9), 'ko')
ax.legend((R_in[0],R_out[0],shade,line[0]),
          ('Initial Rotation','Relaxed Rotation',
           'Predicted Relaxation','Direct Relaxation'),
          loc='center right', bbox_to_anchor=(0.03,0.5), fontsize=15)
ax.set_xlim(all_xlims)


#Plotting the energies
ax = axs[1]
#Plot the light data]
ax.plot(pd_r_l['D_out'], pd_r_l['E_off'],
        'o',  color='tab:orange', markersize=10, label='Light Species')
ax.set_ylim(E_ylims)
#Plot the tight data
ax.plot(pd_r_t['D_out'], pd_r_t['E_off'],
        'bx', markersize=12, label='Tight Species')
ax.set_ylabel('Relative\nAdsorption\nEnergy\n/ [eV]')
# ax.set_xlabel('Rotation Angle / [$^{\circ}$]   *Angles from light relaxation', fontsize=16)
ax.legend(loc='lower right')


ax = axs[2]
ax.plot(pd_r_l['D_out'], pd_r_l['H_C60'],
        'o', color='tab:orange', markersize=10, label='C60 light')
ax.plot(pd_r_t['D_out'], pd_r_t['H_C60'],
        'x', color='blue', markersize=10, label='C60 tight')
ax.set_ylabel('Charge Transfer\nto $C_{60,r}$\n/ [e]')
ax.set_xlabel('Rotation Angle / [$^{\circ}$]')
ax.set_ylim([-1.008, -1.042])

fig0.tight_layout()
plt.savefig(jn(vp.path_thesis, 'geometries', 'C60_on_Cu(111)', 'rotation',
               'old_rotations', 'Rotation_data_r.png'))


'''Code for C60_u'''
#Set up the figure and subplots
fig0, axs =  plt.subplots(3,1, sharex=True, sharey=False, gridspec_kw={'hspace': 0, 'wspace':0})
fig0.set_size_inches([18,10])
#Set the x and y tick locations
ax = axs[0]
ax.tick_params(axis='x', bottom=False, top=True, labelbottom=False, labeltop=True)
ax.tick_params(axis='y', left=False, labelleft=False)

#Plotting the direct and infered adsorptions
for _n,_i in enumerate(pd_u_l['D_in']):
    shade,line = plot_adsorb(ax, pd_u_l['D_in'][_n], pd_u_l['D_out'][_n])
#Plot the angles every 15D and set the x ticks and labels
x = np.arange(0,135,15)
ax.set_xticks(x)
R_in  = ax.plot(x, np.linspace(1,1,9), 'ro')
R_out = ax.plot(x, np.linspace(0,0,9), 'ko')
ax.legend((R_in[0],R_out[0],shade,line[0]),
          ('Initial Rotation','Relaxed Rotation',
           'Predicted Relaxation','Direct Relaxation'),
          loc='center right', bbox_to_anchor=(0.03,0.5), fontsize=15)
ax.set_xlim(all_xlims)


#Plotting the energies
ax = axs[1]
#Plot the light data
ax.plot(pd_u_l['D_out'], pd_u_l['E_off'],
        'o',  color='tab:orange', markersize=10, label='Light Species')
ax.set_ylim(E_ylims)
#Plot the tight data
ax.plot(pd_u_t['D_out'], pd_u_t['E_off'],
        'bx', markersize=12, label='Tight Species')
ax.set_ylabel('Relative\nAdsorption\nEnergy\n/ [eV]')
# ax.set_xlabel('Rotation Angle / [$^{\circ}$]   *Angles from light relaxation', fontsize=16)
ax.legend()


ax = axs[2]
ax.plot(pd_u_l['D_out'], pd_u_l['H_C60'],
        'o', color='tab:orange', markersize=10, label='C60 light')
ax.plot(pd_u_t['D_out'], pd_u_t['H_C60'],
        'x', color='blue', markersize=10, label='C60 tight')
ax.set_ylabel('Charge Transfer\nto $C_{60,u}$\n/ [e]')
ax.set_xlabel('Rotation Angle / [$^{\circ}$]')
ax.set_ylim([-0.438,-0.472])


fig0.tight_layout()
plt.savefig(jn(vp.path_thesis, 'geometries', 'C60_on_Cu(111)', 'rotation',
               'old_rotations', 'Rotation_data_u.png'))

