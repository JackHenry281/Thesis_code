# -*- coding: utf-8 -*-
from os.path import join as jn
from os import mkdir,makedirs

import time

''' Admin '''
def get_timestamp():
    '''  '''
    t=['{0:02}'.format(t) for t in list(time.gmtime()[0:6])]
    return ''.join(t[:3])+'-'+''.join(t[3:])




''' Plotting Admin '''
def tight(fig, axs, rect=None):
    '''Set the figure size and axes positions so they are uniform and
        independant of the data plotted. .tight_layout() is used without 
        axis ticks and labels on the plot so they do not affect the white space
        around the axes.'''
    #Try loop to deal with multiple or single axes 
    #Multiple axes
    try:
        for _ax in axs:
            _ax.axis('off')
        if rect:
            fig.tight_layout(rect=rect)
        else:
            fig.tight_layout()
        for _ax in axs:
            _ax.axis('on')
    #Single axis
    except TypeError:
        axs.axis('off')
        if rect:
            fig.tight_layout(rect=rect)
        else:
            fig.tight_layout()
        axs.axis('on')

def admin_duo(axs, title=None, y0=True, xlim=None, ylim=None,
                   labels=['Potential / [eV]', 'Force / [nN]', 'Z / [$\AA$]']):
    #Set title and x label
    axs[0].set_title(title)    
    axs[1].set_xlabel(labels[2])
    
    #Iterate over the axes
    for ax in range(2):
        #Set ylabels
        axs[ax].set_ylabel(labels[ax])

        #Set x and y lims if supplied
        if ylim: axs[ax].set_ylim(ylim)
        if xlim: axs[ax].set_xlim(xlim)
        #sets the global tick params or something? idk i cant remember
        axs[ax].tick_params()
        #Set the dashed black line at y=0
        if y0:
            axs[ax].set_xlim(axs[ax].get_xlim())
            axs[ax].plot(axs[ax].get_xlim(), [0]*2, 'k--', linewidth=0.5)

def new_lims(fig, axs, limits, filetype='.png', o=(0,1,2,3)):
    ''' limits = default: [xlim, ylim, lim_name, save_dir_path] for o=(0,1,2,3)
             o = order the limits values are listed in
    '''
    #If statement to check the format is correct
    if len(limits)==4:
        #Set xy lims
        axs[0].set_xlim(limits[o[0]])
        axs[0].set_ylim(limits[o[1]])
        #Make the directory if it doesnt exist and save the file
        makedirs(limits[o[3]], exist_ok=True)
        fig.savefig(jn(limits[o[3]], limits[o[2]]+filetype))
    else:
        print('Incorrect format for \'limits\' variable, not saving fig')
