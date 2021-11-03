# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
import vars_paths as vp

from os.path import join as jn
import numpy as np
import matplotlib.pyplot as plt

import functions_Cu_convergence as f

#Global font size for all plots
plt.rcParams.update({'font.size':16})

path_save =[vp.save_Cu_k, jn(vp.data_Cu_k, 'data_analysed')]
file_types=['.svg']

''' Functions'''
def plot_k_points(dic_data):
    #Genertae the figure anx axes
    dic_data['fig']=plt.figure(figsize=(24,9))
    dic_data['axs'] = [plt.subplot(1,3,1), plt.subplot(1,3,2), plt.subplot(1,3,3),]
    
    #Add axis labels and set ylims
    dic_data['axs'][0].set_xlabel('k-points in a,b, and c Directions')
    dic_data['axs'][0].set_ylabel('Relative Energy / [meV]')
    dic_data['axs'][0].set_ylim([-50, 800])
    
    dic_data['axs'][1].set_xlabel('k-points in a,b, and c Directions')
    dic_data['axs'][1].set_ylabel('Relative Energy / [meV]')
    dic_data['axs'][1].set_ylim([-0.5, 1])
    dic_data['axs'][1].yaxis.tick_right()
    dic_data['axs'][1].yaxis.set_label_position('right')
    
    dic_data['axs'][2].set_xlabel('k-points in a,b, and c Directions')
    dic_data['axs'][2].set_ylabel('Relative Energy / [meV]')
    dic_data['axs'][2].set_ylim([-0.06, 0.06])
    dic_data['axs'][2].yaxis.tick_right()
    dic_data['axs'][2].yaxis.set_label_position('right')

    #Add the dotted lines to both axis
    for ax in dic_data['axs']:
        #Plot the data
        ax.plot(dic_data['dirs_i'], dic_data['meV' ], dic_data['ms'])
        
        #Black line at y=0
        ax.set_xlim(ax.get_xlim())
        ax.plot(ax.get_xlim(), [0]*2, 'k--', linewidth=0.75)
        #Line at minima
        ax.set_ylim(ax.get_ylim())
        ax.plot([24]*2, ax.get_ylim(),  '--', color='gray' , linewidth=0.75, label='$k_{abc}$=25')
        ax.plot([42]*2, ax.get_ylim(), 'r--',                linewidth=0.75, label='$k_{abc}$=42')
        ax.plot([50]*2, ax.get_ylim(),  '--', color='green', linewidth=0.75, label='$k_{abc}$=50')    
        ax.legend()

    #Add shaded regions
    dic_data['axs'][1].fill_between(ax.get_xlim(), [-0.6 ]*2, [0.6 ]*2, color='gray' , alpha=0.25)
    dic_data['axs'][1].fill_between(ax.get_xlim(), [-0.05]*2, [0.05]*2, color='red'  , alpha=0.25)
    dic_data['axs'][2].fill_between(ax.get_xlim(), [-0.02]*2, [0.02]*2, color='green', alpha=0.25)

def plot_l_t(dic_plot, dic_light, dic_tight):
    #Add axis labels and set ylims
    dic_plot['axs'][0].set_xlabel('k-points in a,b, and c Directions')
    dic_plot['axs'][0].set_ylabel('Relative Energy / [meV]')
    dic_plot['axs'][0].set_ylim([-50, 800])
    
    dic_plot['axs'][1].set_xlabel('k-points in a,b, and c Directions')
    dic_plot['axs'][1].set_ylabel('Relative Energy / [meV]')
    dic_plot['axs'][1].set_ylim([-0.5, 1])
    # l_t_a6315['axs'][1].yaxis.tick_right()
    # l_t_a6315['axs'][1].yaxis.set_label_position('right')
    
    dic_plot['axs'][2].set_xlabel('k-points in a,b, and c Directions')
    dic_plot['axs'][2].set_ylabel('Relative Energy / [meV]')
    dic_plot['axs'][2].set_ylim([-0.06, 0.06])
    # l_t_a6315['axs'][2].yaxis.tick_right()
    # l_t_a6315['axs'][2].yaxis.set_label_position('right')
    
    #Add the dotted lines to both axis
    for ax in dic_plot['axs']:
        #Plot the data
        ax.plot(dic_light['dirs'], dic_light['meV' ], dic_light['ms'], label='light')
        ax.plot(dic_tight['dirs'], dic_tight['meV' ], dic_tight['ms'], label='tight')
        
        #Black line at y=0
        ax.set_xlim(ax.get_xlim())
        ax.plot(ax.get_xlim(), [0]*2, 'k--', linewidth=0.75)
        #Line at minima
        ax.set_ylim(ax.get_ylim())
        ax.plot([24]*2, ax.get_ylim(),  '--', color='gray' , linewidth=0.75, label='$k_{abc}$=25')
        ax.plot([42]*2, ax.get_ylim(), 'r--',                linewidth=0.75, label='$k_{abc}$=42')
        ax.plot([50]*2, ax.get_ylim(),  '--', color='green', linewidth=0.75, label='$k_{abc}$=50')    
    
    dic_plot['axs'][0].legend(loc='upper center')
    dic_plot['axs'][1].legend(loc='lower left')
    dic_plot['axs'][2].legend(loc='lower left')
    
    #Add shaded regions
    dic_plot['axs'][1].fill_between(ax.get_xlim(), [-0.6 ]*2, [0.6 ]*2, color='gray' , alpha=0.25)
    dic_plot['axs'][1].fill_between(ax.get_xlim(), [-0.05]*2, [0.05]*2, color='red'  , alpha=0.25)
    dic_plot['axs'][2].fill_between(ax.get_xlim(), [-0.02]*2, [0.02]*2, color='green', alpha=0.25)
        
    #Add textboxes to label the graphs 1 and 2
    dic_plot['axs'][0].text(0.9, 0.9, 'A', transform=dic_plot['axs'][0].transAxes,
                             fontsize=40, fontweight='bold')
    dic_plot['axs'][1].text(0.9, 0.9, 'B', transform=dic_plot['axs'][1].transAxes,
                             fontsize=40, fontweight='bold')
    dic_plot['axs'][2].text(0.9, 0.9, 'C', transform=dic_plot['axs'][2].transAxes,
                             fontsize=40, fontweight='bold')


''' K Points: light  a=3.6315 AA '''
#Initiate the dictionary by adding the relative path
l_k_a6315 = {'path':jn(vp.data_Cu_k, 'a=3.6315', 'light_2010', 'data_raw')}
#Read in the data
f.read_k_points(l_k_a6315, markers='rx')
f.total_time(l_k_a6315)
f.sort_data(l_k_a6315)
# f.fit_n_dic(l_k_a6315)
# #Plot the k points
# plot_k_points(l_k_a6315)
# #Add figure title
# l_k_a6315['fig'].suptitle('K Point Sampling System Convergence:     a=3.6315 $\AA$     with     2010 light species defaults\n$\pm$0.05 meV at $K_{abc}$=25      $\pm$0.6 meV at $K_{abc}$=42      $\pm$0.02 meV at $K_{abc}$=50')
# #Save the plot
# l_k_a6315['fig'].tight_layout()
# for path in path_save:
#     for filetype in file_types:
#         l_k_a6315['fig'].savefig(jn(path, 'a6315_light'+filetype),
#                                dpi=None, transparent=False)

''' K Points: tight  a=3.6315 AA '''
#Initiate the dictionary by adding the relative path
t_k_a6315 = {'path':jn(vp.data_Cu_k, 'a=3.6315', 'tight_2010', 'data_raw')}
#Read in the data
f.read_k_points(t_k_a6315, markers='b.')
f.total_time(t_k_a6315)
f.sort_data(t_k_a6315)
# f.fit_n_dic(t_k_a6315)
# #Plot the k points
# plot_k_points(t_k_a6315)
# #Add figure title
# t_k_a6315['fig'].suptitle('K Point Sampling System Convergence:     a=3.6315 $\AA$     with     2010 tight species defaults\n$\pm$0.05 meV at $K_{abc}$=25      $\pm$0.6 meV at $K_{abc}$=42      $\pm$0.02 meV at $K_{abc}$=50')
# #Save the plot
# t_k_a6315['fig'].tight_layout()
# for path in path_save:
#     for filetype in file_types:
#         t_k_a6315['fig'].savefig(jn(path, 'a6315_tight'+filetype),
#                                 dpi=None, transparent=False)


''' K Points: light  a=3.6310 AA '''
#Initiate the dictionary by adding the relative path
l_k_a6310 = {'path':jn(vp.data_Cu_k, 'a=3.6310', 'light_2010', 'data_raw')}
#Read in the data
f.read_k_points(l_k_a6310, markers='mx')
f.total_time(l_k_a6310)
f.sort_data(l_k_a6310)
# f.fit_n_dic(l_k_a6310, c=2.3)
# #Plot the k points
# plot_k_points(l_k_a6310)
# #Add figure title
# l_k_a6310['fig'].suptitle('K Point Sampling System Convergence:     a=3.6310 $\AA$     with     2010 light species defaults\n$\pm$0.05 meV at $K_{abc}$=25      $\pm$0.6 meV at $K_{abc}$=42      $\pm$0.02 meV at $K_{abc}$=50')
# #Save the plot
# l_k_a6310['fig'].tight_layout()
# for path in path_save:
#     for filetype in file_types:
#         l_k_a6310['fig'].savefig(jn(path, 'a6310_light'+filetype),
#                                dpi=None, transparent=False)

''' K Points: tight  a=3.6310 AA '''
#Initiate the dictionary by adding the relative path
t_k_a6310 = {'path':jn(vp.data_Cu_k, 'a=3.6310', 'tight_2010', 'data_raw')}
#Read in the data
f.read_k_points(t_k_a6310, markers='g.')
f.total_time(t_k_a6310)
f.sort_data(t_k_a6310)
# f.fit_n_dic(t_k_a6310, c=33)
# #Plot the k points
# plot_k_points(t_k_a6310)
# #Add figure title
# t_k_a6310['fig'].suptitle('K Point Sampling System Convergence:     a=3.6310 $\AA$     with     2010 tight species defaults\n$\pm$0.05 meV at $K_{abc}$=25      $\pm$0.6 meV at $K_{abc}$=42      $\pm$0.02 meV at $K_{abc}$=50')
# #Save the plot
# t_k_a6310['fig'].tight_layout()
# for path in path_save:
#     for filetype in file_types:
#         t_k_a6310['fig'].savefig(jn(path, 'a6310_tight'+filetype),
#                                 dpi=None, transparent=False)


''' Plot light and tight data on the same figure for each a value'''
# #Make figure
# a6315 = {'fig':plt.figure(figsize=(24,9)),
#          'axs':[plt.subplot(1,3,1), plt.subplot(1,3,2), plt.subplot(1,3,3)]}
# #Plot data
# plot_l_t(a6315, l_k_a6315, t_k_a6315)
# #Add the figure title
# a6315['fig'].suptitle('K Point Sampling System Convergence:     a=3.6315 $\AA$\n$\pm$0.6 meV at $K_{abc}$=25      $\pm$0.05 meV at $K_{abc}$=42      $\pm$0.02 meV at $K_{abc}$=50')
# #Save figure
# a6315['fig'].tight_layout()
# for path in path_save:
#     for filetype in file_types:
#         a6315['fig'].savefig(jn(path, 'a6315_l_t'+filetype),
#                                dpi=None, transparent=False)

# #Make figure
# a6310 = {'fig':plt.figure(figsize=(24,9)),
#          'axs':[plt.subplot(1,3,1), plt.subplot(1,3,2), plt.subplot(1,3,3)]}
# #Plot data
# plot_l_t(a6310, l_k_a6310, t_k_a6310)
# #Add the figure title
# a6310['fig'].suptitle('K Point Sampling System Convergence:     a=3.6310 $\AA$\n$\pm$0.6 meV at $K_{abc}$=25      $\pm$0.05 meV at $K_{abc}$=42      $\pm$0.02 meV at $K_{abc}$=50')
# #Save figure
# a6310['fig'].tight_layout()
# for path in path_save:
#     for filetype in file_types:
#         a6310['fig'].savefig(jn(path, 'a6310_l_t'+filetype),
#                                dpi=None, transparent=False)



''' Plot all data on the same figure '''
l_t_a = {'fig':plt.figure(figsize=(11,14))}
l_t_a['gs' ] = l_t_a['fig'].add_gridspec(3, 2, hspace=0, wspace=0)
l_t_a['axs'] = l_t_a['gs' ].subplots(sharex=True)

#Add y axis in correct place and label
for axy in range(3):
    #Right axes
    l_t_a['axs'][axy][0].set_ylabel('Relative Energy / [meV]')    
    
    #Left axes
    l_t_a['axs'][axy][1].yaxis.tick_right()
    l_t_a['axs'][axy][1].yaxis.set_label_position('right')
    l_t_a['axs'][axy][1].set_ylabel('Relative Energy / [meV]')

for axx in range(2):
    l_t_a['axs'][0][axx].set_ylim([  -50,  800])
    l_t_a['axs'][1][axx].set_ylim([ -0.5,    1])
    l_t_a['axs'][2][axx].set_ylim([-0.06, 0.06])

#Add the data and dotted lines to both axis
for axy in range(3):
    #Plot the data
    l_t_a['axs'][axy][0].plot(l_k_a6315['dirs_i'], l_k_a6315['meV' ], l_k_a6315['ms'], label='light')
    l_t_a['axs'][axy][0].plot(t_k_a6315['dirs_i'], t_k_a6315['meV' ], t_k_a6315['ms'], label='tight')
    l_t_a['axs'][axy][1].plot(l_k_a6310['dirs_i'], l_k_a6310['meV' ], l_k_a6310['ms'], label='light')
    l_t_a['axs'][axy][1].plot(t_k_a6310['dirs_i'], t_k_a6310['meV' ], t_k_a6310['ms'], label='tight')

    for axx in range(2):
        ax = l_t_a['axs'][axy][axx]        
        #Black line at y=0
        ax.set_xlim(ax.get_xlim())
        ax.plot(ax.get_xlim(), [0]*2, 'k--', linewidth=0.75)
        #Line at minima
        ax.set_ylim(ax.get_ylim())
        ax.plot([24]*2, ax.get_ylim(),  '--', color='gray' , linewidth=0.75, label='$k_{abc}$=25')
        ax.plot([42]*2, ax.get_ylim(), 'r--',                linewidth=0.75, label='$k_{abc}$=42')
        ax.plot([50]*2, ax.get_ylim(),  '--', color='green', linewidth=0.75, label='$k_{abc}$=50')
        #Make the xticks more sparse
        ax.set_xticks([1]+list(range(5,61,5)))
        

for axx in range(2):
    #Add shaded regions
    l_t_a['axs'][1][axx].fill_between(ax.get_xlim(), [-0.6 ]*2, [0.6 ]*2, color='gray' , alpha=0.25)
    l_t_a['axs'][1][axx].fill_between(ax.get_xlim(), [-0.05]*2, [0.05]*2, color='red'  , alpha=0.25)
    l_t_a['axs'][2][axx].fill_between(ax.get_xlim(), [-0.02]*2, [0.02]*2, color='green', alpha=0.25)
    #Add legends to top plots
    l_t_a['axs'][0][axx].legend(loc='upper center')

#Label x axes
l_t_a['axs'][2][0].set_xlabel('$k_{abc}$ for a=3.6315 $\AA$')
l_t_a['axs'][2][1].set_xlabel('$k_{abc}$ for a=3.6310 $\AA$')



l_t_a['fig'].suptitle('K Point Sampling System Convergence:\n$\pm$0.6 meV at $K_{abc}$=25      $\pm$0.05 meV at $K_{abc}$=42      $\pm$0.02 meV at $K_{abc}$=50')

#Add textboxes to label the graphs
l_t_a['axs'][0][0].text(0.9, 0.9, 'A', transform=l_t_a['axs'][0][0].transAxes,
                          fontsize=30, fontweight='bold')
l_t_a['axs'][1][0].text(0.9, 0.9, 'B', transform=l_t_a['axs'][1][0].transAxes,
                          fontsize=30, fontweight='bold')
l_t_a['axs'][2][0].text(0.9, 0.9, 'C', transform=l_t_a['axs'][2][0].transAxes,
                          fontsize=30, fontweight='bold')

l_t_a['axs'][0][1].text(0.9, 0.9, 'D', transform=l_t_a['axs'][0][1].transAxes,
                          fontsize=30, fontweight='bold')
l_t_a['axs'][1][1].text(0.9, 0.9, 'E', transform=l_t_a['axs'][1][1].transAxes,
                          fontsize=30, fontweight='bold')
l_t_a['axs'][2][1].text(0.9, 0.9, 'F', transform=l_t_a['axs'][2][1].transAxes,
                          fontsize=30, fontweight='bold')

l_t_a['fig'].tight_layout()
for path in [vp.save_Cu_k, jn(vp.data_Cu_k, 'data_analysed')]:
    for filetype in file_types:
        l_t_a['fig'].savefig(jn(path, 'a_l_t'+filetype),
                                dpi=None, transparent=False)





''' Plot k points time data'''
plt.rcParams.update({'font.size':22})
#Gen figure and axis
sc_data_time = {'fig':plt.figure(figsize=(16,8)),
                'axs':[plt.subplot(1,2,1), plt.subplot(1,2,2)]}

#Reposition the y axis on the right
sc_data_time['axs'][1].yaxis.tick_right()
sc_data_time['axs'][1].yaxis.set_label_position('right')

#Label x axes
sc_data_time['axs'][0].set_xlabel('$k_{abc}$ for a=3.6315 $\AA$')
sc_data_time['axs'][1].set_xlabel('$k_{abc}$ for a=3.6310 $\AA$')

#Plot all the data the dotted for the second axis
sc_data_time['axs'][0].plot(l_k_a6315['dirs_i'], l_k_a6315['tpa'], l_k_a6315['ms'], label='light')
sc_data_time['axs'][0].plot(t_k_a6315['dirs_i'], t_k_a6315['tpa'], t_k_a6315['ms'], label='tight')

#Plot all the data the dotted for the second axis
sc_data_time['axs'][1].plot(l_k_a6310['dirs_i'], l_k_a6310['tpa'], l_k_a6310['ms'], label='light')
sc_data_time['axs'][1].plot(t_k_a6310['dirs_i'], t_k_a6310['tpa'], t_k_a6310['ms'], label='tight')
# sc_data_time['axs'][1].plot(l_k_a6310['sort'][0,:], l_k_a6310['fitted'], 'm', linewidth=0.75)
# sc_data_time['axs'][1].plot(t_k_a6310['sort'][0,:], t_k_a6310['fitted'], 'g', linewidth=0.75)

# sc_data_time['axs'][1].plot(t_k_a6310['dirs_i'], f.fit_cube(t_k_a6310['dirs_i'], t_k_a6310['meV'])[0], 'r', linewidth=0.75)


#Add legend and line at y=0
for ax in sc_data_time['axs']:
    #Set y axis labels
    ax.set_ylabel('Time / [seconds per atom]')
    #Set y axis limits
    ax.set_ylim([-10, 600])

    #plot dotted lines at k=25,42,50
    ax.plot([24]*2, ax.get_ylim(),  '--', color='gray' , linewidth=0.75, label='$k_{abc}$=25')
    ax.plot([42]*2, ax.get_ylim(), 'r--',                linewidth=0.75, label='$k_{abc}$=42')
    ax.plot([50]*2, ax.get_ylim(),  '--', color='green', linewidth=0.75, label='$k_{abc}$=50')  

    #Make the xticks more sparse
    ax.set_xlim(ax.get_xlim())
    ax.set_xticks([1]+list(range(5,61,5)))
    #Black line at y=0
    ax.plot(ax.get_xlim(), [0]*2, 'k--', linewidth=0.75)
    #Legend
    ax.legend()

#Add textboxes to label the graphs a and b
sc_data_time['axs'][0].text(0.88, 0.05, 'A', transform=sc_data_time['axs'][0].transAxes,
                         fontsize=40, fontweight='bold')
sc_data_time['axs'][1].text(0.88, 0.05, 'B', transform=sc_data_time['axs'][1].transAxes,
                         fontsize=40, fontweight='bold')
#Savefig
sc_data_time['fig'].tight_layout()
for path in [vp.save_Cu_k, jn(vp.data_Cu_k, 'data_analysed')]:
    for filetype in file_types:
        sc_data_time['fig'].savefig(jn(path, 'sc_data_time'+filetype),
                                dpi=None, transparent=False)






''' K points from Cu Bulk to Cu(111)-(4x4) '''
plt.rcParams.update({'font.size':26})
#Calculate thart and end indices
I_max=52
end_r=2.8

#Round start to integer
I = np.linspace(1,I_max,I_max).astype(int)
I_end = np.unique(np.around(np.linspace(1,I_max,I_max)*(3.631/10.2700188900),0).astype(int))
# I_end=I_end[1:]
I_start=[]
for i_end in I_end:
    I_start.append([I[np.around(np.linspace(1,I_max,I_max)*(3.631/10.2700188900),0).astype(int)==i_end][ 0],
                    I[np.around(np.linspace(1,I_max,I_max)*(3.631/10.2700188900),0).astype(int)==i_end][-1]])
I_start = np.asarray(I_start, dtype=int)
I_start=I_start[1:,:]
I_start[0][0]=1
I_end=I_end[1:]

kp={}
kp['fig'] = plt.figure(figsize=(17,6))
kp['axs'] = [plt.subplot(1,1,1)]
kp['axs'].append(kp['axs'][0].twiny())

#Label the bottom X axis
kp['axs'][0].set_xlabel('\nCu(111)-(4x4) System $k_{ab}$ Points')
kp['axs'][0].set_xticks(I_end*end_r)
kp['axs'][0].set_xlim([I[0]-1,I[-1]+1])
kp['axs'][0].set_xticklabels(I_end)
#Label the top X axis
kp['axs'][1].set_xlabel('Cu FCC Bravais Lattice $k_{abc}$ Points\n')
kp['axs'][1].set_xticks(I[1::2])
kp['axs'][1].set_xlim([I[0]-1,I[-1]+1])
#Remove y axis ticks and labels
kp['axs'][0].set_ylim([-0.01,1.01])
kp['axs'][0].set_ylim([0,1])
kp['axs'][0].set_yticklabels([])
kp['axs'][0].set_yticks([])

#Plot the dots
kp['axs'][0].plot(I    , np.linspace(1,1,I_max), 'ro', markersize=20)
kp['axs'][0].plot(I_end*end_r, np.linspace(0,0,len(I_end)), 'bo', markersize=20)

#Plot the shaded regions
for i_end in I_end:
    kp['axs'][0].fill_between([I_start[i_end-1][0], i_end*end_r, I_start[i_end-1][-1]],
                              [1,0,1], [1,1,1], color='red' , alpha=0.25)

kp['axs'][0].spines['top'   ].set_visible(False)
kp['axs'][0].spines['right' ].set_visible(False)
kp['axs'][0].spines['bottom'].set_visible(False)
kp['axs'][0].spines['left'  ].set_visible(False)
kp['axs'][1].spines['top'   ].set_visible(False)
kp['axs'][1].spines['right' ].set_visible(False)
kp['axs'][1].spines['bottom'].set_visible(False)
kp['axs'][1].spines['left'  ].set_visible(False)

kp['fig'].tight_layout()

kp['fig'].tight_layout()
for path in [vp.save_Cu_k, jn(vp.data_Cu_k, 'data_analysed')]:
    for filetype in file_types:
        kp['fig'].savefig(jn(path, 'k_convert'+filetype),
                               dpi=None, transparent=False)












