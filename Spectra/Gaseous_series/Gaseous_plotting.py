# -*- coding: utf-8 -*-
import sys
sys.path.append(r'H:\+PhD\+DFT\dft_code\Thesis_Plots')
import vars_paths as vp
sys.path.append(vp.path_functions_atmos)
from functions_process  import check_field_key
# import functions_raw as fr
# import functions_process as fp
import functions_plotting as fplt

from os.path import join as jn
from os import listdir,mkdir

from atmos import Assembly
from joblib import Parallel, delayed
import time
import matplotlib.pyplot as plt

#Get timestamp for the plots folder
timestamp = fplt.get_timestamp()

#Define paths
path_data_pro  = jn(vp.path_H2O_g, 'Plots_atmos', 'Data_processed')
path_plots     = jn(vp.path_H2O_g, 'Plots_atmos', f'Data_plotted_{timestamp}')

path_single    = jn(path_plots, 'Spectra_single')
path_multi     = jn(path_plots, 'Spectra_multi' )

#Iterate over the contence of the directory and extract the names of .nc files
file_systems = [x for x in listdir(path_data_pro) if x.endswith('.nc')]

#General matplotlib setup stuff
fs=20
filetype='.png'
plt.rcParams['font.size']=fs #Set the global fontsize
plt_cols = plt.rcParams['axes.prop_cycle'].by_key()['color'] #Get the default plt colorus
rect = (0.15,0.05,0.99,0.96)

#Global xylim parameters to iterate over
#format: [[xlim, ylim], [...], [...]]
limits_xy  = [[( 2.5, 7.5), ( -0.4,0.1  )],
              [( 7.5,20.1), (-0.02,0.01)],
              [( 4  ,20.1), (-0.1,0.1)],
              ]

def plot_single_spectrum(paths, field_energy, field_force, Z_key='zscale~tip_base'):
    plt.rcParams['font.size']=fs
    #Check the supplied paramaters
    field_energy=check_field_key(field_energy)
    field_force =check_field_key(field_force )
    
    #Read in the data
    system = Assembly.load(jn(paths['dir_data'], paths['file_data']))
    
    #Save paths correponding to the global xylim parameters
    #format: [[filename, path_save], [...], [...]]
    # limits_same_spec = [['minima', jn(paths['dir_save'], paths['spec_type'], paths['file_data'][:-3])],
    #                     ['tail'  , jn(paths['dir_save'], paths['spec_type'], paths['file_data'][:-3])],
    #                     ['taill' , jn(paths['dir_save'], paths['spec_type'], paths['file_data'][:-3])],
    #                     ]
    # limits_comp_spec = [[paths['file_data'][:-3], jn(paths['dir_save'], paths['spec_type'], '+minima')],
    #                     [paths['file_data'][:-3], jn(paths['dir_save'], paths['spec_type'], '+tail'  )],
    #                     [paths['file_data'][:-3], jn(paths['dir_save'], paths['spec_type'], '+taill' )],
    #                     ]
    limit_types = ['minima', 'tail', 'taill']
    
    '''Set up the plot'''
    fig, axs = plt.subplots(2, 1, sharex=True, sharey=True,
                    gridspec_kw={'hspace': 0, 'wspace':0}, figsize=(8,12))
    #Position the axes in the same place on the figure for every plot
    fplt.tight(fig, axs, rect=rect)
    
    #Plot the data
    for interaction in ['all', 'dft', 'vdw']:
        #Plot the energy
        axs[0].plot(system[Z_key], system[field_energy+interaction], label=interaction)
        #Plot the force
        axs[1].plot(system[Z_key], system[field_force+interaction ], label=interaction)

    #Add the legend
    axs[0].legend(loc='upper right')
    #Add the Title, axis labels, limits
    fplt.admin_duo(axs, title=paths['spec_type']+': '+paths['file_data'])
    #Save the fig in the correct directory with the correct name and limits
    #Iterate over the different xy limits
    for _l in range(len(limits_xy)):
        #Save all the plots for a single spectrum in 1 directory
        fplt.new_lims(fig, axs, limits_xy[_l]+
                      [limit_types[_l], jn(paths['dir_save'], paths['spec_type'],
                                           paths['file_data'][:-3])], filetype)
        #Save plots for different spectra with the same XY lims in 1 directory
        fplt.new_lims(fig, axs, limits_xy[_l]+
                      [paths['file_data'][:-3], jn(paths['dir_save'],
                       paths['spec_type'], '+'+limit_types[_l])], filetype)
    #Close the figure for RAM saving and to stop warning
    plt.close(fig)

def plot_parallel(file_system):
    print(f'System: {file_system}')
    #Make the file paths
    dic_paths = {'dir_data'  : path_data_pro,
                  'dir_save'  : path_single  , 
                  'file_data' : file_system  }
    
    '''Plot the system energy'''
    plot_single_spectrum(dic_paths|{'spec_type' : 'system_energy'},
                          'ee~', 'ef~', Z_key='zscale~tip_base_offset_junc')
    
    '''Plot the FHI forces'''
    plot_single_spectrum(dic_paths|{'spec_type' : 'FHI_tip'},
                          'fe_tip~', 'ff_tip~', Z_key='zscale~tip_base_offset_junc')
    plot_single_spectrum(dic_paths|{'spec_type' : 'FHI_srf'},
                          'fe_srf~', 'ff_srf~', Z_key='zscale~tip_base_offset_junc')
    plot_single_spectrum(dic_paths|{'spec_type' : 'FHI_tip_offset'},
                          'fe_tip_offset~', 'ff_tip_offset~', Z_key='zscale~tip_base_offset_junc')
    plot_single_spectrum(dic_paths|{'spec_type' : 'FHI_srf_offset'},
                          'fe_srf_offset~', 'ff_srf_offset~', Z_key='zscale~tip_base_offset_junc')

'''Call the functions'''
startTime = time.time()
Parallel(n_jobs=3)(delayed(plot_parallel)(file_system) for file_system in file_systems)
endTime = time.time()
print('Execution Time: {0:.1f} mins'.format((endTime-startTime)/60))

# for file_system in file_systems:
#     print(f'System: {file_system}')
#     #Make the file paths
#     dic_paths = {'dir_data'  : path_data_pro,
#                  'dir_save'  : path_single  , 
#                  'file_data' : file_system  }
    
#     '''Plot the system energy'''
#     plot_single_spectrum(dic_paths|{'spec_type' : 'system_energy'},
#                          'ee~', 'ef~', Z_key='zscale~tip_base_offset_junc')
    
#     '''Plot the FHI forces'''
#     plot_single_spectrum(dic_paths|{'spec_type' : 'FHI_tip'},
#                          'fe_tip~', 'ff_tip~', Z_key='zscale~tip_base_offset_junc')
#     plot_single_spectrum(dic_paths|{'spec_type' : 'FHI_srf'},
#                          'fe_srf~', 'ff_srf~', Z_key='zscale~tip_base_offset_junc')
#     plot_single_spectrum(dic_paths|{'spec_type' : 'FHI_tip_offset'},
#                          'fe_tip_offset~', 'ff_tip_offset~', Z_key='zscale~tip_base_offset_junc')
#     plot_single_spectrum(dic_paths|{'spec_type' : 'FHI_srf_offset'},
#                          'fe_srf_offset~', 'ff_srf_offset~', Z_key='zscale~tip_base_offset_junc')