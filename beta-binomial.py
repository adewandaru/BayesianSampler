# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:32:45 2018

@author: dewandaru@gmail.com

Bayesian Updating with Beta Priors with example on coin toss case study.

Beta Distribution is a special case of Dirichlet, for binomial.
Beta distribution is conjugate for binomial distribution, so that the posterior 
is also in Beta.

"""

from math import *

p = 0.5 # heads [ to be estimated ]
pi = 0.5 # prior density
T = "HHHTH" # tosses

def heads(s):
    return s.count('H')
def tails(s):
    return s.count('T')
    
print heads(T)
print tails(T)

import numpy as np

""" 
    we have the equivalent of the following function, from 
    from scipy.stats import beta
    beta.pdf(0.5, 1, 1)
    but for pedagogical purpose we'll construct it here by using
    gamma from math.* lib :
"""

def beta1(x, alpha, beta):
    frac = gamma( alpha + beta ) / ( gamma( alpha ) * gamma( beta ))
    power = x ** ( alpha - 1 ) * ( 1 - x ) ** ( beta - 1 )
    return frac*power

xs = np.arange(100) * 0.01

ys = [ beta1(x, 0.5, 0.5) for x in xs ]

import matplotlib.pyplot as plt

# now let's do the update!
_alpha = 0.5
_beta = 0.5

seq = "TTTTTTTTHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
cdelta = 1.0 / len(seq)
clr = 0.9
print str(len(seq)) + " tosses."

plt.axis([0, 1, 0, 7])

for c in seq:

    ys = [ beta1(x, _alpha, _beta) for x in xs ]

    plt.plot( xs, ys, str(clr) )
    
    if (c == "H"):
        _alpha = _alpha + 1;
    else:
        _beta = _beta + 1;
        
    clr = np.clip(clr - cdelta, 0, 1)
    
    












    