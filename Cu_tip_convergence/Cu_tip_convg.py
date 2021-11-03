# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
sys.path.append(r'H:\+PhD\+DFT\dft_code\Spectra_V2')
import vars_paths as vp
import func_data_generation_V2 as fdg2

from os.path import join as jn

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# from func_plotting import list_all_files,del_files

#Global font size for all plots
cols = plt.rcParams['axes.prop_cycle'].by_key()['color']
plt.rcParams.update({'font.size':22})
fs = (16,8)

paths_save=[vp.save_ads_1, vp.save_ads_2]
file_types=['.svg']



#Energy of the isolated relaxed molecule
E_mol = -6984853.679867129


#Generate the spectrum csvs
tip_cnv = {'dir_data': vp.data_tip}
tip_cnv['system'] = fdg2.read_spectrum_data_ads(tip_cnv['dir_data'], ['system_full'],
                                                  dir_BCE='BaseCode_energy_system_full')
tip_cnv['tip'   ] = fdg2.read_spectrum_data_ads(tip_cnv['dir_data'], ['tip'],
                                                  dir_BCE='BaseCode_energy_tip')



#Extract the useful convergence data to plot
data_plot = {'layers'      : tip_cnv['system'    ]['h_dir'     ].to_numpy(),
             #Add the adsorption energy from the rleaxed goemetries=
             'r_E_ads'     : tip_cnv['system'    ]['EM_sys_vdW'].to_numpy() -\
                              (tip_cnv['tip'       ]['EM_sys_vdW'].to_numpy()+E_mol),
             #Add the charge transfer
             'r_Q_H_C60'   : tip_cnv['system'    ]['Q_H_C60'   ].to_numpy(),
             'r_Q_H_Cu'    : tip_cnv['system'    ]['Q_H_Cu'    ].to_numpy(),
             'r_Q_M_C60'   : tip_cnv['system'    ]['Q_M_C60'   ].to_numpy(),
             'r_Q_M_Cu'    : tip_cnv['system'    ]['Q_M_Cu'    ].to_numpy(),
             #Add the adsorption height
             'r_h_ads'     : tip_cnv['system'    ]['h_C_min'   ].to_numpy(),  
             'r_h_ads_top' : tip_cnv['system'    ]['h_C_max'   ].to_numpy(),  
             #Add vdW energy
             'r_E_vdW'     : tip_cnv['system'    ]['E_vdW_vdW' ].to_numpy(),             
             #Add the time
             'time'        : tip_cnv['system'    ]['time_step' ].to_numpy(),
             'time_spec'   :(tip_cnv['system'    ]['time_step' ].to_numpy())*2*60,
            }
data_plot = pd.DataFrame.from_dict(data_plot)


"""
''' Plotting Energy Convergence'''
err=0.021
#Gen figure and axis
cnv_E = {'fig':plt.figure(figsize=(16,16)),
         'axs':[plt.subplot(2,2,1), plt.subplot(2,2,3), plt.subplot(2,2,4)]}

#Set y label on right for 3rd plot
cnv_E['axs'][2].yaxis.tick_right()
cnv_E['axs'][2].yaxis.set_label_position('right')
#Move posotion of 1st plot to the centre
ax = cnv_E['axs'][0]
pos1 = ax.get_position() # get the original position 
pos2 = [pos1.x0+0.22, pos1.y0,  pos1.width, pos1.height] 
ax.set_position(pos2) # set a new position

#Plot the data
#Axs 0
cnv_E['axs'][0].plot(data_plot_r['layers'], data_plot_r['r_E_ads_relax'], 'o',
                   label='$C_{60,r}$', markersize=15, color=cols[0])
cnv_E['axs'][0].plot(data_plot_u['layers'], data_plot_u['u_E_ads_relax'], 'x',
                   label='$C_{60,u}$', markersize=15, color=cols[1])

#Axs 1
cnv_E['axs'][1].plot(data_plot_r['layers'], data_plot_r['r_E_ads_relax'], 'o',
                   label='$C_{60,r}$', markersize=15, color=cols[0])

#Axs 2
cnv_E['axs'][2].plot(data_plot_r['layers'],
                     data_plot_r['r_E_ads_relax']-data_plot_r['r_E_ads_relax'][7],
                     'o', label='$C_{60,r}$', markersize=15, color=cols[0])
cnv_E['axs'][2].plot(data_plot_r['layers'],
                     data_plot_r['r_E_vdW']-data_plot_r['r_E_vdW'][7],
                     '*', label='$C_{60,r}$ TS Energy', markersize=15, color='green')

for ax in cnv_E['axs']:
    #Label the aixs
    ax.set_xlabel('Slab Layers')
    ax.set_ylabel('Adsorption Energy / [eV]')
    ax.set_xticks(data_plot_r['layers'])
    ax.set_xlim(ax.get_xlim())
    #Add legend
    ax.legend()
cnv_E['axs'][2].set_ylabel('Relative Energy / [eV]')


#Plot the shaded regions and dashed lines
for ax in [cnv_E['axs'][0], cnv_E['axs'][1]]:
    ax.plot(ax.get_xlim(), [data_plot_r['r_E_ads_relax'][7]]*2, 'r--', linewidth=0.75)
    ax.fill_between(ax.get_xlim(),
        [data_plot_r['r_E_ads_relax'][7]+data_plot_r['r_E_ads_relax'][7]*err]*2,
        [data_plot_r['r_E_ads_relax'][7]-data_plot_r['r_E_ads_relax'][7]*err]*2,
        color='red' , alpha=0.25)


cnv_E['axs'][2].plot(cnv_E['axs'][2].get_xlim(), [0]*2, 'r--', linewidth=0.75)
cnv_E['axs'][2].fill_between(cnv_E['axs'][2].get_xlim(),
    [ data_plot_r['r_E_ads_relax'][7]*err]*2,
    [-data_plot_r['r_E_ads_relax'][7]*err]*2,
    color='red' , alpha=0.25)

# cnv_E['fig'].suptitle('Adsorption Energy')
cnv_E['axs'][0].set_title('Adsorption Energy')
cnv_E['axs'][0].set_ylim([None, 0])

#Add textboxes to label the graphs a and b
cnv_E['axs'][0].text(0.05, 0.90, 'A', transform=cnv_E['axs'][0].transAxes,
                          fontsize=40, fontweight='bold')
cnv_E['axs'][1].text(0.05, 0.05, 'B', transform=cnv_E['axs'][1].transAxes,
                          fontsize=40, fontweight='bold')
cnv_E['axs'][2].text(0.88, 0.05, 'C', transform=cnv_E['axs'][2].transAxes,
                          fontsize=40, fontweight='bold')
#Savefig
# cnv_E['fig'].tight_layout()
for path in paths_save:
    for filetype in file_types:
        cnv_E['fig'].savefig(jn(path, 'convergence_E'+filetype),
                                dpi=None, transparent=False)



''' Plotting Charge Convergence'''
#Gen figure and axis
cnv_Q = {'fig':plt.figure(figsize=fs),
         'axs':[plt.subplot(1,2,1), plt.subplot(1,2,2)]}

#Plot the data
cnv_Q['axs'][0].plot(data_plot_r['layers'], data_plot_r['r_Q_M_C60'], 's',
                   label='Mulliken Transfer into $C_{60,r}$', markersize=15, color=cols[2])
cnv_Q['axs'][0].plot(data_plot_r['layers'],-data_plot_r['r_Q_M_Cu'], '.',
                   label='Mulliken Transfer out of $Cu_{r}$', markersize=15, color=cols[3])

cnv_Q['axs'][1].plot(data_plot_r['layers'], data_plot_r['r_Q_M_C60'], 's',
                   #label='Mulliken Transfer into $C_{60,r}$',
                   markersize=15, color=cols[2])
cnv_Q['axs'][1].plot(data_plot_r['layers'],-data_plot_r['r_Q_M_Cu'], '.',
                   #label='Mulliken Transfer out of $Cu_{r}$',
                   markersize=15, color=cols[3])

cnv_Q['axs'][1].plot(data_plot_r['layers'], data_plot_r['r_Q_H_C60'], 's',
                   label='Hirshfeld Transfer into $C_{60,r}$', markersize=15, color=cols[7])
cnv_Q['axs'][1].plot(data_plot_r['layers'],-data_plot_r['r_Q_H_Cu'], '.',
                   label='Hirshfeld Transfer out of $Cu_{r}$', markersize=15, color=cols[5])

cnv_Q['axs'][0].plot(data_plot_u['layers'], data_plot_u['u_Q_M_C60'], 's',
                   label='Mulliken Transfer into $C_{60,u}$', markersize=15, color=cols[4])
cnv_Q['axs'][0].plot(data_plot_u['layers'],-data_plot_u['u_Q_M_Cu'], 'x',
                   label='Mulliken Transfer out of $Cu_{u}$', markersize=15, color=cols[9])

cnv_Q['fig'].suptitle('Charge Transfer On Adsorption')
for ax in cnv_Q['axs']:
    #Label the aixs
    ax.set_xlabel('Slab Layers')
    ax.set_ylabel('Charge Transfer / [$e$]')
    ax.set_xticks(data_plot_r['layers'])

    ax.set_xlim(ax.get_xlim())

    ax.plot(ax.get_xlim(), [-1.01]*2, '--', color='k', linewidth=0.75)
    ax.fill_between(ax.get_xlim(), [-1.02]*2, [-1.00]*2, color='gray' , alpha=0.25)

    #Add legend
    ax.legend()

cnv_Q['axs'][1].set_ylim([-1.06, -0.99])
cnv_Q['axs'][1].yaxis.tick_right()
cnv_Q['axs'][1].yaxis.set_label_position('right')

#Add textboxes to label the graphs a and b
cnv_Q['axs'][0].text(0.05, 0.90, 'A', transform=cnv_Q['axs'][0].transAxes,
                          fontsize=40, fontweight='bold')
cnv_Q['axs'][1].text(0.88, 0.05, 'B', transform=cnv_Q['axs'][1].transAxes,
                          fontsize=40, fontweight='bold')
#Savefig
cnv_Q['fig'].tight_layout()
for path in paths_save:
    for filetype in file_types:
        cnv_Q['fig'].savefig(jn(path, 'convergence_Q_M'+filetype),
                                dpi=None, transparent=False)


# ''' Plotting Adsorption Height and vdW Energy Convergence'''
# #Gen figure and axis
# cnv_h = {'fig':plt.figure(figsize=fs),
#           'axs':[plt.subplot(1,2,1), plt.subplot(1,2,2)]}

# #Plot the data
# cnv_h['axs'][0].plot(data_plot_r['layers'],
#                       (data_plot_r['r_h_ads']-np.amin(data_plot_r['r_h_ads']))*100, 'o',
#                     label='$C_{60,r}$', markersize=15, color=cols[0])
# cnv_h['axs'][0].plot(data_plot_r['layers'],
#                       (data_plot_r['r_h_ads_top']-np.amin(data_plot_r['r_h_ads_top']))*100, 'x',
#                     label='$C_{60,r}$', markersize=15, color='red')

# # cnv_h['axs'][1].plot(data_plot_r['layers'],
# #                       (data_plot_r['r_E_vdW']-np.amin(data_plot_r['r_E_vdW'])), 'o',
# #                     label='$C_{60,r}$', markersize=15, color=cols[0])

# cnv_h['axs'][1].plot(data_plot_r['layers'], data_plot_r['r_E_ads_relax']-
#                      np.amax(data_plot_r['r_E_ads_relax']), 'o',
#                     label='$C_{60,r}$ System Energy', markersize=15, color=cols[0])
# cnv_h['axs'][1].plot(data_plot_r['layers'], data_plot_r['r_E_vdW']-
#                      np.amax(data_plot_r['r_E_vdW']), 'x',
#                     label='$C_{60,r}$ vdW Energy', markersize=15, color='red')

# for ax in cnv_h['axs']:
#     #Label the aixs
#     ax.set_xlabel('Slab Layers')
#     ax.set_ylabel('Relative Adsorption Height / [pm]')
#     ax.set_xticks(data_plot_r['layers'])
#     #Add legend
#     ax.legend()

# #Position y axis
# ax.set_ylabel('Relative Attractive vdW Energy / [eV]')
# cnv_h['axs'][1].yaxis.tick_right()
# cnv_h['axs'][1].yaxis.set_label_position('right')

# #Add textboxes to label the graphs a and b
# cnv_h['axs'][0].text(0.05, 0.05, 'A', transform=cnv_h['axs'][0].transAxes,
#                           fontsize=40, fontweight='bold')
# cnv_h['axs'][1].text(0.88, 0.05, 'B', transform=cnv_h['axs'][1].transAxes,
#                           fontsize=40, fontweight='bold')
# #Savefig
# cnv_h['fig'].tight_layout()
# for path in paths_save:
#     for filetype in file_types:
#         cnv_h['fig'].savefig(jn(path, 'convergence_height'+filetype),
#                                 dpi=None, transparent=False)




''' Plotting Time'''
#Gen figure and axis
cnv_t = {'fig':plt.figure(figsize=fs),
         'axs':[plt.subplot(1,2,1), plt.subplot(1,2,2)]}

#Plot the data
cnv_t['axs'][0].plot(data_plot_r['layers'], data_plot_r['time'], 's',
                   label='$C_{60,r}$ Adsorption', markersize=15, color=cols[2])

cnv_t['axs'][1].plot(data_plot_r['layers'], data_plot_r['time'], 's',
                    #label='Mulliken Transfer into $C_{60,r}$',
                    markersize=15, color=cols[2])
cnv_t['axs'][1].plot(data_plot_r['layers'], data_plot_r['time_spec'], '*',
                    label='$C{60,r}$ Force Spectrum',
                    markersize=15, color=cols[3])

# cnv_t['fig'].suptitle('Charge Transfer On Adsorption')
for ax in cnv_t['axs']:
    #Label the aixs
    ax.set_xlabel('Slab Layers')
    ax.set_ylabel('Time / [CPU-hours]')
    ax.set_xticks(data_plot_r['layers'])

    ax.set_xlim(ax.get_xlim())

    ax.plot(ax.get_xlim(), [-1.01]*2, '--', color='k', linewidth=0.75)
    ax.fill_between(ax.get_xlim(), [-1.02]*2, [-1.00]*2, color='gray' , alpha=0.25)

    #Add legend
    ax.legend()


cnv_t['axs'][1].yaxis.tick_right()
cnv_t['axs'][1].yaxis.set_label_position('right')
cnv_t['axs'][1].set_ylim([-5000, 100000])

#Add textboxes to label the graphs a and b
cnv_t['axs'][0].text(0.05, 0.80, 'A', transform=cnv_t['axs'][0].transAxes,
                          fontsize=40, fontweight='bold')
cnv_t['axs'][1].text(0.05, 0.90, 'B', transform=cnv_t['axs'][1].transAxes,
                          fontsize=40, fontweight='bold')
#Savefig
cnv_t['fig'].tight_layout()
for path in paths_save:
    for filetype in file_types:
        cnv_t['fig'].savefig(jn(path, 'convergence_t'+filetype),
                                dpi=None, transparent=False)


"""

