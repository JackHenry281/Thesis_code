# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import vars_paths as vp

from os.path import join as jn
import numpy as np
import matplotlib.pyplot as plt

import functions_Cu_convergence as f

#Global font size for all plots
plt.rcParams.update({'font.size':22})
fs = (16,8)

path_save =[vp.save_Cu_a, jn(vp.data_Cu_a, 'data_analysed')]
file_types=['.svg']#, '.png']
    
''' Lattice Vector: light  k=25 '''
#Initiate the dictionary by adding the relative path
l_a_k25_6={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_6', 'light_2010_k25', 'data_raw')}
#Read in the data
f.read_lattice_vector(l_a_k25_6, label='k$_{abc}$=25')
f.total_time(l_a_k25_6)
#Add the a value to the label
f.add_amin_label(l_a_k25_6)


''' Lattice Vector: light  k=42 '''
#Initiate the dictionary by adding the relative path
l_a_k42_6={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_6', 'light_2010_k42', 'data_raw')} 
#Read in the data
f.read_lattice_vector(l_a_k42_6, label='k$_{abc}$=42')
f.total_time(l_a_k42_6)
#Add the a value to the label
f.add_amin_label(l_a_k42_6)

#Initiate the dictionary by adding the relative path
l_a_k42_8={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_8', 'sc_accuracy_eev_3',
                     'light_2010_k42', 'data_raw')}
#Read in the data
f.read_lattice_vector(l_a_k42_8, label='k$_{abc}$=42')
f.total_time(l_a_k42_8)
#Add the a value to the label
f.add_amin_label(l_a_k42_8)

''' Lattice Vector: light  k=50 '''
#Initiate the dictionary by adding the relative path
l_a_k50_8={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_8', 'sc_accuracy_eev_3',
                     'light_2010_k50', 'data_raw')} 
#Read in the data
f.read_lattice_vector(l_a_k50_8, label='k$_{abc}$=50')
f.total_time(l_a_k50_8)
#Add the a value to the label
f.add_amin_label(l_a_k50_8)

''' Lattice Vector: tight  k=25 '''
#Initiate the dictionary by adding the relative path
t_a_k25_6={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_6', 'tight_2010_k25', 'data_raw')}
#Read in the data
f.read_lattice_vector(t_a_k25_6, label='k$_{abc}$=25')
f.total_time(t_a_k25_6)
#Add the a value to the label
f.add_amin_label(t_a_k25_6)

''' Lattice Vector: tight  k=42 '''
#Initiate the dictionary by adding the relative path
t_a_k42_6={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_6', 'tight_2010_k42', 'data_raw')}
#Read in the data
f.read_lattice_vector(t_a_k42_6, label='k$_{abc}$=42')
f.total_time(t_a_k42_6)
#Add the a value to the label
f.add_amin_label(t_a_k42_6)

#Initiate the dictionary by adding the relative path
t_a_k42_8={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_8', 'sc_accuracy_eev_3',
                     'tight_2010_k42', 'data_raw')}
#Read in the data
f.read_lattice_vector(t_a_k42_8, label='k$_{abc}$=42')
f.total_time(t_a_k42_8)
#Add the a value to the label
f.add_amin_label(t_a_k42_8)

''' Lattice Vector: tight  k=50 '''
#Initiate the dictionary by adding the relative path
t_a_k50_8_3={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_8', 'sc_accuracy_eev_3',
                     'tight_2010_k50', 'data_raw')} 
#Read in the data
f.read_lattice_vector(t_a_k50_8_3, label='k$_{abc}$=50')
f.total_time(t_a_k50_8_3)
#Add the a value to the label
f.add_amin_label(t_a_k50_8_3)

#Initiate the dictionary by adding the relative path
t_a_k50_8_4={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_8', 'sc_accuracy_eev_4',
                     'tight_2010_k50', 'data_raw')} 
#Read in the data
f.read_lattice_vector(t_a_k50_8_4, label='k$_{abc}$=50')
f.total_time(t_a_k50_8_4)

#Initiate the dictionary by adding the relative path
t_a_k50_6_5={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_6', 'sc_accuracy_eev_5',
                     'tight_2010_k50', 'data_raw')} 
#Read in the data
f.read_lattice_vector(t_a_k50_6_5, label='k$_{abc}$=50')
f.total_time(t_a_k50_6_5)

#Initiate the dictionary by adding the relative path
t_a_k50_8_5={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_8', 'sc_accuracy_eev_5',
                     'tight_2010_k50', 'data_raw')} 
#Read in the data
f.read_lattice_vector(t_a_k50_8_5, label='k$_{abc}$=50')
f.total_time(t_a_k50_8_5)

#Initiate the dictionary by adding the relative path
t_a_k50_10_5={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_10', 'sc_accuracy_eev_5',
                      'tight_2010_k50', 'data_raw')} 
#Read in the data
f.read_lattice_vector(t_a_k50_10_5, label='k$_{abc}$=50')
f.total_time(t_a_k50_10_5)

''' Lattice Vector: tight  k=50, k_shift '''
#Initiate the dictionary by adding the relative path
t_k50_8_3_05={'path':jn(vp.data_Cu_a, 'sc_accuracy_etot_8', 'sc_accuracy_eev_3',
                     'tight_2010_k50_off_0.5', 'data_raw')} 
#Read in the data
f.read_lattice_vector(t_k50_8_3_05, label=None)
f.total_time(t_k50_8_3_05)




''' Plot the light lattice vector data '''
#Gen figure and axis
light = {'fig':plt.figure(figsize=fs),
         'axs':[plt.subplot(1,2,1), plt.subplot(1,2,2)]}

#Label the first axis
light['axs'][0].set_xlabel('Cu Lattice Vector / [$\AA$]')
light['axs'][0].set_ylabel('Relative Energy / [meV]')
light['axs'][0].set_ylim([-15, 300])
#Label the second axis
light['axs'][1].set_xlabel('Cu Unit Vector / [$\AA$]')
light['axs'][1].set_ylabel('Relative Energy / [meV]')
light['axs'][1].set_xlim([3.6299, 3.6331])
light['axs'][1].set_ylim([-0.1e-2, 4e-2])
light['axs'][1].yaxis.tick_right()
light['axs'][1].yaxis.set_label_position('right')

#Plot all the data the dotted lines to both axis
for ax in light['axs']:
    #Data
    ax.plot(l_a_k25_6['dirs_f'], l_a_k25_6['meV' ], '.-', label=l_a_k25_6['lab'])
    ax.plot(l_a_k42_6['dirs_f'], l_a_k42_6['meV' ], '.-', label=l_a_k42_6['lab'])
    ax.plot(l_a_k42_8['dirs_f'], l_a_k42_8['meV' ], 'v-', label=l_a_k42_8['lab'])
    ax.plot(l_a_k50_8['dirs_f'], l_a_k50_8['meV' ], 'v-', label=l_a_k50_8['lab'])

    
    #Black line at y=0
    ax.set_xlim(ax.get_xlim())
    ax.plot(ax.get_xlim(), [0]*2, 'k--', linewidth=0.75)

    #Line at minima
    ax.set_ylim(ax.get_ylim())
    ax.plot([l_a_k25_6['a_min']]*2, ax.get_ylim(), '--', color='tab:blue'  , linewidth=0.75)
    ax.plot([l_a_k42_6['a_min']]*2, ax.get_ylim(), '--', color='tab:orange', linewidth=0.75)
    ax.plot([l_a_k42_8['a_min']]*2, ax.get_ylim(), '--', color='tab:green' , linewidth=0.75)
    ax.plot([l_a_k50_8['a_min']]*2, ax.get_ylim(), '--', color='tab:red'   , linewidth=0.75)
    #Add legend
    ax.legend()

#Add textboxes to label the graphs a and b
light['axs'][0].text(0.05, 0.05, 'A', transform=light['axs'][0].transAxes,
                         fontsize=40, fontweight='bold')
light['axs'][1].text(0.88, 0.05, 'B', transform=light['axs'][1].transAxes,
                         fontsize=40, fontweight='bold')
#Savefig
light['fig'].tight_layout()
for path in [vp.save_Cu_a, jn(vp.data_Cu_a, 'data_analysed')]:
    for filetype in file_types:
        light['fig'].savefig(jn(path, 'a_l'+filetype),
                                dpi=None, transparent=False)



''' Plot the tight lattice vector data '''
#Gen figure and axis
tight = {'fig':plt.figure(figsize=fs),
         'axs':[plt.subplot(1,2,1), plt.subplot(1,2,2)]}

#Label the first axis
tight['axs'][0].set_xlabel('Cu Lattice Vector / [$\AA$]')
tight['axs'][0].set_ylabel('Relative Energy / [meV]')
tight['axs'][0].set_ylim([-15, 300])
#Label the second axis
tight['axs'][1].set_xlabel('Cu Unit Vector / [$\AA$]')
tight['axs'][1].set_ylabel('Relative Energy / [meV]')
tight['axs'][1].set_xlim([3.6299, 3.6331])
tight['axs'][1].set_ylim([-0.1e-2, 4e-2])
tight['axs'][1].yaxis.tick_right()
tight['axs'][1].yaxis.set_label_position('right')

#Plot all the data the dotted lines to both axis
for ax in tight['axs']:
    #Data
    ax.plot(t_a_k25_6['dirs_f'], t_a_k25_6['meV' ], '.-', label=t_a_k25_6['lab'])
    ax.plot(t_a_k42_6['dirs_f'], t_a_k42_6['meV' ], '.-', label=t_a_k42_6['lab'])
    ax.plot(t_a_k42_8['dirs_f'], t_a_k42_8['meV' ], 'v-', label=t_a_k42_8['lab'])
    ax.plot(t_a_k50_8_3['dirs_f'], t_a_k50_8_3['meV' ], 'v-', label=t_a_k50_8_3['lab'])

    
    #Black line at y=0
    ax.set_xlim(ax.get_xlim())
    ax.plot(ax.get_xlim(), [0]*2, 'k--', linewidth=0.75)

    #Line at minima
    ax.set_ylim(ax.get_ylim())
    ax.plot([t_a_k25_6['a_min']]*2, ax.get_ylim(), '--', color='tab:blue'  , linewidth=0.75)
    ax.plot([t_a_k42_6['a_min']]*2, ax.get_ylim(), '--', color='tab:orange', linewidth=0.75)
    ax.plot([t_a_k42_8['a_min']]*2, ax.get_ylim(), '--', color='tab:green' , linewidth=0.75)
    ax.plot([t_a_k50_8_3['a_min']]*2, ax.get_ylim(), '--', color='tab:red'   , linewidth=0.75)
    #Add legend
    ax.legend()

#Add textboxes to label the graphs a and b
tight['axs'][0].text(0.05, 0.05, 'A', transform=tight['axs'][0].transAxes,
                         fontsize=40, fontweight='bold')
tight['axs'][1].text(0.88, 0.05, 'B', transform=tight['axs'][1].transAxes,
                         fontsize=40, fontweight='bold')
#Savefig
tight['fig'].tight_layout()
for path in [vp.save_Cu_a, jn(vp.data_Cu_a, 'data_analysed')]:
    for filetype in file_types:
        tight['fig'].savefig(jn(path, 'a_t'+filetype),
                                dpi=None, transparent=False)



''' Plot the tight lattice vector: etot and  eev'''
#Gen figure and axis
sc_data = {'fig':plt.figure(figsize=fs),
           'axs':[plt.subplot(1,2,1), plt.subplot(1,2,2)]}

#Label the axis and set lims
for ax in sc_data['axs']:
    ax.set_xlabel('Cu Lattice Vector / [$\AA$]')
    ax.set_ylabel('Relative Energy / [meV]')
    
    ax.set_xlim([3.6299, 3.6331])
    ax.set_ylim([-0.1e-2, 4e-2])

#Reposition the y axis on the right
sc_data['axs'][1].yaxis.tick_right()
sc_data['axs'][1].yaxis.set_label_position('right')

#Add subplot titles
sc_data['axs'][0].set_title('sc_accuracy_etot=Variable\nsc_accuracy_eev=$10^{-5}$      ')
sc_data['axs'][1].set_title('sc_accuracy_etot=$10^{-8}$       \nsc_accuracy_eev=Variable')

#Plot all the data the dotted for the second axis
ax=sc_data['axs'][0]
#Data
ax.plot(t_a_k50_10_5['dirs_f'], t_a_k50_10_5['meV' ], 's-', label='sc_accuracy_etot=$10^{-10}$', color='tab:purple')
ax.plot(t_a_k50_8_5 ['dirs_f'], t_a_k50_8_5 ['meV' ], 'v-', label='sc_accuracy_etot=$10^{-8}$' , color='tab:blue')
ax.plot(t_a_k50_6_5 ['dirs_f'], t_a_k50_6_5 ['meV' ], '.-', label='sc_accuracy_etot=$10^{-6}$' , color='tab:olive' )
#Line at minima
ax.plot([t_a_k50_8_5 ['a_min']]*2, ax.get_ylim(), '--', color='tab:blue'  , linewidth=0.75)
ax.plot([t_a_k50_10_5['a_min']]*2, ax.get_ylim(), '--', color='tab:purple', linewidth=0.75)
ax.plot([t_a_k50_6_5 ['a_min']]*2, ax.get_ylim(), '--', color='tab:olive' , linewidth=0.75)


#Plot all the data the dotted for the second axis
ax=sc_data['axs'][1]
#Data
ax.plot(t_a_k50_8_5['dirs_f'], t_a_k50_8_5['meV' ], 'v-', label='sc_accuracy_eev=$10^{-5}$')
ax.plot(t_a_k50_8_4['dirs_f'], t_a_k50_8_4['meV' ], 'v-', label='sc_accuracy_eev=$10^{-4}$', color='tab:gray')
ax.plot(t_a_k50_8_3['dirs_f'], t_a_k50_8_3['meV' ], 'v-', label='sc_accuracy_eev=$10^{-3}$', color='tab:red' )
#Line at minima
ax.plot([t_a_k50_8_5['a_min']]*2, ax.get_ylim(), '--', color='tab:blue'  , linewidth=0.75)
ax.plot([t_a_k50_8_4['a_min']]*2, ax.get_ylim(), '--', color='tab:orange', linewidth=0.75)
ax.plot([t_a_k50_8_3['a_min']]*2, ax.get_ylim(), '--', color='tab:red'   , linewidth=0.75)

#Add legend and line at y=0
for ax in sc_data['axs']:
    #Black line at y=0
    ax.set_xlim(ax.get_xlim())
    ax.plot(ax.get_xlim(), [0]*2, 'k--', linewidth=0.75)
    #Legend
    ax.legend()

#Add textboxes to label the graphs a and b
sc_data['axs'][0].text(0.05, 0.05, 'A', transform=sc_data['axs'][0].transAxes,
                         fontsize=40, fontweight='bold')
sc_data['axs'][1].text(0.88, 0.05, 'B', transform=sc_data['axs'][1].transAxes,
                         fontsize=40, fontweight='bold')
#Savefig
sc_data['fig'].tight_layout()
for path in [vp.save_Cu_a, jn(vp.data_Cu_a, 'data_analysed')]:
    for filetype in file_types:
        sc_data['fig'].savefig(jn(path, 'sc_data'+filetype),
                                dpi=None, transparent=False)


''' Plot the tight lattice vector: etot and eev time data'''
#Gen figure and axis
sc_data_time = {'fig':plt.figure(figsize=fs),
           'axs':[plt.subplot(1,2,1), plt.subplot(1,2,2)]}

#Label the axis and set lims
for ax in sc_data_time['axs']:
    ax.set_xlabel('Cu Lattice Vector / [$\AA$]')
    ax.set_ylabel('Time / [seconds per atom]')
    
    ax.set_xlim([3.6299, 3.6331])
    ax.set_ylim([-100, 2500])

#Reposition the y axis on the right
sc_data_time['axs'][1].yaxis.tick_right()
sc_data_time['axs'][1].yaxis.set_label_position('right')

#Add subplot titles
sc_data_time['axs'][0].set_title('sc_accuracy_etot=Variable\nsc_accuracy_eev=$10^{-5}$      ')
sc_data_time['axs'][1].set_title('sc_accuracy_etot=$10^{-8}$       \nsc_accuracy_eev=Variable')

#Plot all the data the dotted for the second axis
ax=sc_data_time['axs'][0]
#Data
ax.plot(t_a_k50_10_5['dirs_f'], t_a_k50_10_5['tpa'], 's', label='sc_accuracy_etot=$10^{-10}$', color='tab:purple')
ax.plot(t_a_k50_8_5 ['dirs_f'], t_a_k50_8_5 ['tpa'], 'v', label='sc_accuracy_etot=$10^{-8}$' , color='tab:blue'  )
ax.plot(t_a_k50_6_5 ['dirs_f'], t_a_k50_6_5 ['tpa'], '.', label='sc_accuracy_etot=$10^{-6}$' , color='tab:olive' )
#Line of average time
ax.plot(ax.get_xlim(), [np.mean(t_a_k50_10_5['tpa'])]*2, '--', color='tab:purple', linewidth=3)
ax.plot(ax.get_xlim(), [np.mean(t_a_k50_8_5 ['tpa'])]*2, '--', color='tab:blue'  , linewidth=3)
ax.plot(ax.get_xlim(), [np.mean(t_a_k50_6_5 ['tpa'])]*2, '--', color='tab:olive' , linewidth=3)

#Plot all the data the dotted for the second axis
ax=sc_data_time['axs'][1]
#Data
ax.plot(t_a_k50_8_5['dirs_f'], t_a_k50_8_5['tpa'], 'v', label='sc_accuracy_eev=$10^{-5}$', color='tab:blue')
ax.plot(t_a_k50_8_4['dirs_f'], t_a_k50_8_4['tpa'], 'v', label='sc_accuracy_eev=$10^{-4}$', color='tab:gray')
ax.plot(t_a_k50_8_3['dirs_f'], t_a_k50_8_3['tpa'], 'v', label='sc_accuracy_eev=$10^{-3}$', color='tab:red' )
#Line of average time
ax.plot(ax.get_xlim(), [np.mean(t_a_k50_8_5['tpa'])]*2, '--', color='tab:blue', linewidth=3)
ax.plot(ax.get_xlim(), [np.mean(t_a_k50_8_4['tpa'])]*2, '--', color='tab:gray', linewidth=3)
ax.plot(ax.get_xlim(), [np.mean(t_a_k50_8_3['tpa'])]*2, '--', color='tab:red' , linewidth=3)

#Add legend and line at y=0
for ax in sc_data_time['axs']:
    #Black line at y=0
    ax.set_xlim(ax.get_xlim())
    ax.plot(ax.get_xlim(), [0]*2, 'k--', linewidth=0.75)
    #Legend
    ax.legend()

#Add textboxes to label the graphs a and b
sc_data_time['axs'][0].text(0.05, 0.05, 'A', transform=sc_data_time['axs'][0].transAxes,
                         fontsize=40, fontweight='bold')
sc_data_time['axs'][1].text(0.88, 0.05, 'B', transform=sc_data_time['axs'][1].transAxes,
                         fontsize=40, fontweight='bold')
#Savefig
sc_data_time['fig'].tight_layout()
for path in [vp.save_Cu_a, jn(vp.data_Cu_a, 'data_analysed')]:
    for filetype in file_types:
        sc_data_time['fig'].savefig(jn(path, 'sc_data_time'+filetype),
                                dpi=None, transparent=False)



''' Plot the tight lattice vector data '''
#Gen figure and axis
tight = {'fig':plt.figure(figsize=fs),
         'axs':[plt.subplot(1,2,1), plt.subplot(1,2,2)]}

#Label the first axis
tight['axs'][0].set_xlabel('Cu Lattice Vector / [$\AA$]')
tight['axs'][0].set_ylabel('Relative Energy / [meV]')
tight['axs'][0].set_ylim([-15, 300])
#Label the second axis
tight['axs'][1].set_xlabel('Cu Unit Vector / [$\AA$]')
tight['axs'][1].set_ylabel('Relative Energy / [meV]')
tight['axs'][1].set_xlim([3.6299, 3.6331])
tight['axs'][1].set_ylim([-0.1e-2, 4e-2])
tight['axs'][1].yaxis.tick_right()
tight['axs'][1].yaxis.set_label_position('right')

#Plot all the data the dotted lines to both axis
for ax in tight['axs']:
    #Data
    ax.plot(t_a_k50_8_3 ['dirs_f'], t_a_k50_8_3 ['meV' ], '.-', label='$\Gamma$')
    ax.plot(t_k50_8_3_05['dirs_f'], t_k50_8_3_05['meV' ], '.-', label='0.5')
    # ax.plot(t_a_k42_6['dirs_f'], t_a_k42_6['meV' ], '.-', label=t_a_k42_6['lab'])
    # ax.plot(t_a_k42_8['dirs_f'], t_a_k42_8['meV' ], 'v-', label=t_a_k42_8['lab'])
    # ax.plot(t_a_k50_8_3['dirs_f'], t_a_k50_8_3['meV' ], 'v-', label=t_a_k50_8_3['lab'])

    
    #Black line at y=0
    ax.set_xlim(ax.get_xlim())
    ax.plot(ax.get_xlim(), [0]*2, 'k--', linewidth=0.75)

    #Line at minima
    ax.set_ylim(ax.get_ylim())
    ax.plot([t_a_k50_8_3 ['a_min']]*2, ax.get_ylim(), '--', color='tab:blue'  , linewidth=0.75)    
    ax.plot([t_k50_8_3_05['a_min']]*2, ax.get_ylim(), '--', color='tab:orange', linewidth=0.75)
    # ax.plot([t_a_k42_6['a_min']]*2, ax.get_ylim(), '--', color='tab:orange', linewidth=0.75)
    # ax.plot([t_a_k42_8['a_min']]*2, ax.get_ylim(), '--', color='tab:green' , linewidth=0.75)
    # ax.plot([t_a_k50_8_3['a_min']]*2, ax.get_ylim(), '--', color='tab:red'   , linewidth=0.75)
    #Add legend
    ax.legend()

#Add textboxes to label the graphs a and b
tight['axs'][0].text(0.05, 0.05, 'A', transform=tight['axs'][0].transAxes,
                         fontsize=40, fontweight='bold')
tight['axs'][1].text(0.88, 0.05, 'B', transform=tight['axs'][1].transAxes,
                         fontsize=40, fontweight='bold')
#Savefig
tight['fig'].tight_layout()
for path in [vp.save_Cu_a, jn(vp.data_Cu_a, 'data_analysed')]:
    for filetype in file_types:
        tight['fig'].savefig(jn(path, 'k_offset'+filetype),
                                dpi=None, transparent=False)




