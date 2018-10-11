# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:32:45 2018

@author: dewandaru@gmail.com

Bayesian Updating with Dirichlet Priors with example on three faced dice case study.

Dirichlet distribution is conjugate for multinomial distribution, so that the posterior 
is also in Dirichlet.

"""

from math import *
from drawnow import drawnow, figure

p = 0.5 # heads [ to be estimated ]
pi = 0.5 # prior density
T = "123123" # tosses


import numpy as np

""" 
    Dirichlet distribution is a very generic PDF and takes K (as many as needed)
    alphas parameter (α1, ..., αK > 0) and also x number of parameters of the same
    number. However for visualization it is hard to do for dimensions more than 3.
    In our case we define a specific K=3 for the generic stuff in it.
    
"""

def dirichlet3(x1, x2, x3, a1, a2, a3): # specific dirichlet for 3 variables (needs to be vectorized)
    return dirichlet([x1, x2, x3], [a1, a2, a3])

def dirichlet(xs, alphas): # generic dirichlet.
    gamma_v = np.vectorize(gamma)  # just vectorization to make it work nice with numpy array.
    comp1 = gamma( np.sum(alphas) ) / np.prod( gamma_v ( alphas ) )
    comp2 = np.prod ( xs ** ( np.array( alphas ) - 1.0) )
    return comp1 * comp2

def plot(i, c, xs, ys, zs, ds, _alpha1, _alpha2, _alpha3):
    
    
    fig = plt.figure()
    
    ax = fig.gca(projection='3d')
    
    # Customize the z axis.
    ax.set_zlim(0, 1.01)
    
    ax.view_init(30, 30)
    
    ax.zaxis.set_major_locator(LinearLocator(10))
    
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    
    color_dimension = ds # change to desired fourth dimension
    
    minn, maxx = 0, 20
    
    norm = colors.Normalize(minn, maxx)
    
    m = plt.cm.ScalarMappable(norm=norm, cmap='jet')
    
    m.set_array([])
    
    fcolors = m.to_rgba(color_dimension)
    #ax.set_title(r"iter#" + str(i) + ": Rolled " + c +".$\alpha_1$= " + str(_alpha1) + "," + str(_alpha2) + "," + str(_alpha3) )
    ax.set_title(r'iter#%d rolled %s. $\alpha_1,\alpha_2,\alpha_3$=%d,%d,%d' % ( i,c,_alpha1, _alpha2, _alpha3 ) )
   
    
    # Plot the surface.
    surf = ax.plot_surface(xs, ys, zs, 
                           linewidth=0, antialiased=False,
                           rstride=1, cstride=1,
                           facecolors = fcolors)
    

from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

from matplotlib import *

from matplotlib.ticker import LinearLocator, FormatStrFormatter

import numpy as np


xs = np.arange(100) * 0.01

ys = np.arange(100) * 0.01

xs, ys = np.meshgrid(xs, ys)

#zs = np.clip( 1 - xs - ys, 0, 100 ) # clipping to make sure the values of x + y + z = 1 within the simplex (triangular shape only)

zs = 1 - xs - ys

 # clip it / mask it 
outside = (zs <= 0)

xs[outside] = np.nan

ys[outside] = np.nan

zs[outside] = np.nan

dv = np.vectorize(dirichlet3)

# now let's do the update!
 
_alpha1 = 1
_alpha2 = 1
_alpha3 = 1

seq = "12331121211112121" # >>> Input String Sequence Dice Rolls here. "123" means first roll is 1, then 2, then 3.
cdelta = 1.0 / len(seq)

print str(len(seq)) + " dice rolls."
i = 0 

for c in seq:
    i = i + 1
    ds = dv(xs, ys, zs, _alpha1, _alpha2, _alpha3)
    
    if (c == "1"):
        _alpha1 = _alpha1 + 1
    elif (c == "2"):
        _alpha2 = _alpha2 + 1
    else: # "3"
        _alpha3 = _alpha3 + 1

    plot(i, c, xs, ys, zs, ds, _alpha1, _alpha2, _alpha3)
    
    

    
    
    
    
    
    

    
    
    
    
    












    