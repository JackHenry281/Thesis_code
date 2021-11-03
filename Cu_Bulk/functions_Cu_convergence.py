from os.path import join as jn
from os import walk as oswalk
import numpy as np
from scipy.optimize import curve_fit


def dir_names_lattice_vector(dic_data):
    dic_data['dirs']=[y for y in [x for x in oswalk(dic_data['path'])][0][1] if len(y.split('.')[-1])==4]

def dir_names_k_points(dic_data):
    dic_data['dirs']=[y for y in [x for x in oswalk(dic_data['path'])][0][1]]

def read_energy(dic_data):
    dic_data['meV' ]=[]
    for _n,_dir in enumerate(dic_data['dirs']):
        for _line in reversed(list(open(jn(dic_data['path'], _dir, 'output.aims')))):
            if '| Final zero-broadening corrected energy (caution - metals only) :' in _line:
                dic_data['meV' ].append(_line.split()[-2])
    
def read_k_points(dic_data, markers):
    #Read in direcrory names
    dir_names_k_points(dic_data)
    #Read in the energy data in eV
    read_energy(dic_data)
    #Convet the dirs and eV into np.arrays of float64 and eV into meV
    dic_data['dirs_i'] = np.asarray(dic_data['dirs'], dtype=np.int)
    #Define the zero energy as k=50
    dic_data['meV' ] = np.asarray(dic_data['meV' ], dtype=np.float64)*1000-\
                        float(dic_data['meV' ][45])*1000
    #Add markers
    dic_data['ms']=markers

def read_lattice_vector(dic_data, label=None):
    #Read in direcrory names
    dir_names_lattice_vector(dic_data)
    #Read in the energy data in eV
    read_energy(dic_data)
    #Convet the dirs and eV into np.arrays of float64 and eV into meV
    dic_data['dirs_f'] = np.asarray(dic_data['dirs'], dtype=np.float64)
    #Define the zero energy as the minimum energy
    dic_data['meV' ] = np.asarray(dic_data['meV' ], dtype=np.float64)*1000-\
    np.amin(np.asarray(dic_data['meV' ], dtype=np.float64))*1000
    #Calculate the energy minima lattice constant
    dic_data['a_min']=dic_data['dirs_f'][int(np.argmin(dic_data['meV']))]
    #Add lab
    dic_data['lab']=label

def total_time(dic_data):
    #Read in the time data
    dic_data['time']=np.array([])
    dic_data['tpa' ]=np.array([])
    #Iterate over simulation directories
    for _n,_dir in enumerate(dic_data['dirs']):
        _time=np.array([])
        #Iterate over lines in the output.aims file
        for _line in list(open(jn(dic_data['path'], _dir, 'output.aims'))):
            #Extract all the timestamps (scf cycles + file start and end)
            if 'Date     :' in _line:
                _time=np.append(_time, np.float64(_line.split()[-1]))
        #Take file start time from file end time and assign to the dictionary
        dic_data['time'] = np.append(dic_data['time'],  _time[-1]-_time[0])
        dic_data['tpa' ] = np.append(dic_data['tpa' ], (_time[-1]-_time[0])/4)

def sort_data(dic_data):
    #Join the data into 1 np array
    a = np.stack([dic_data['dirs_i'], dic_data['meV'], dic_data['time']])
    #Sort the data by k-points
    dic_data['sort'] = a[:, a[0, :].argsort()]

def add_amin_label(dic_data):
    dic_data['lab']=dic_data['lab']+', a={0:6.5} $\AA$'.format(dic_data['a_min'])




''' Curve fitting time data '''
def fit_n_dic(dic_data, c=1):  
    #Fit the data
    dic_data['fitted'],dic_data['fit'],dic_data['fit_acc'] =\
        fit_cube(dic_data['sort'][0,:], dic_data['sort'][2,:])
    
def fit_quad(x, y):
    #This function is the equation for the fit. 
    def quad(x, m):
        return m*np.square(x) + 32

    #Perform the curve fit
    #p0 is the initial guess values (a,b,d,c)
    #bounds is the minimum and maxmimum allowed values for each variable
    #   ((a0,b0,d0,c0),(a1,b1,d1,c1))
    Fpopt, Fpcov = curve_fit(quad, x, y)#, 
                             #p0     =  (-0.15, 95, 0.0125, -2), 
                             #bounds = ((-0.3,90,0,-100),(0,110,0.02,100)))
    return quad(x, *Fpopt), Fpopt, Fpcov

def fit_cube(x, y):
    #This function is the equation for the fit. 
    def cube(x, m, c):
        return m*np.power(x,3) + c

    #Perform the curve fit
    #p0 is the initial guess values (a,b,d,c)
    #bounds is the minimum and maxmimum allowed values for each variable
    #   ((a0,b0,d0,c0),(a1,b1,d1,c1))
    Fpopt, Fpcov = curve_fit(cube, x, y, 
                             p0     =  (0.1, 32))
                             #bounds = ((-0.3,90,0,-100),(0,110,0.02,100)))
    return cube(x, *Fpopt), Fpopt, Fpcov

def fit_n(x, y):
    #This function is the equation for the fit. 
    def cube(x, m, n):
        return m*np.power(x,n) + 32

    #Perform the curve fit
    #p0 is the initial guess values (a,b,d,c)
    #bounds is the minimum and maxmimum allowed values for each variable
    #   ((a0,b0,d0,c0),(a1,b1,d1,c1))
    Fpopt, Fpcov = curve_fit(cube, x, y)#, 
                             #p0     =  (-0.15, 95, 0.0125, -2), 
                             #bounds = ((-0.3,90,0,-100),(0,110,0.02,100)))
    return cube(x, *Fpopt), Fpopt, Fpcov

def fit_exp(x, y):
    #This function is the equation for the fit. 
    def exp(x, A,B):
        return A*np.exp(B*x) + 32

    #Perform the curve fit
    #p0 is the initial guess values (a,b,d,c)
    #bounds is the minimum and maxmimum allowed values for each variable
    #   ((a0,b0,d0,c0),(a1,b1,d1,c1))
    Fpopt, Fpcov = curve_fit(exp, x, y)#, 
                             #p0     =  (-0.15, 95, 0.0125, -2), 
                             #bounds = ((-0.3,90,0,-100),(0,110,0.02,100)))
    return exp(x, *Fpopt), Fpopt, Fpcov
