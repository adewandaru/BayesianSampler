# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 06:40:02 2018
EM algorithm toy example: 1 Dimensional.

@author: dewandaru@gmail.com

"""



import matplotlib.pyplot as plt
import numpy as np


"""
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()
"""

mu1 = 3
sigma = 1
t1 = np.random.normal(mu1, sigma, 1000)
#plt.plot(t)

plt.hist(t1, bins=100)

mu2 = 7
t2 = np.random.normal(mu2, sigma, 1000)
plt.hist(t2, bins=100)

'''
 EM algorithm is iterative between calculating :
 1. Expectation membership p(cluster|x) and
 then 
 2. Finding parameter which Maximizing the *likelihood* / 
 [moving cluster center's mu and sigma]
'''

mu = [0, 10]
sigma = [1, 1]
'''
Expectation step: calculate "responsibility" of each cluster to each datapoints.
a.k.a which 
p_c1 = P(c1|x) = ...
p_c2 = P(c2|x) = ...
'''
p_c1 = 
p_c2 = 

'''
Maximization of Likelihood
adjust mu and sigma 
'''
mu = 
sigma = 

def p_x_given_c(x, mu, sigma):
    ''' just a typical normal pdf '''
    return np.exp( -(x-mu)**2 / (2*sigma**2) ) / np.sqrt( 2*math.pi*sigma**2 )   

def p_c_given_x(mu, sigma, x, prior_c):
    ''' 
    calculate responisibility p(c|x) for each datapoint. where c is the cluster.
                   p(x|c) p(c)              p(x|c) p(c)                     p(x|c) p(c)
    p(c|x) =  --------------------- = ------------------------- =  -----------------------------
                      p(x)                  sum(c) p(x,c)             p(x|c)p(c) + p(x|c')p(c')  
    '''
    pxc = P_x_given_c(x, mu, sigma)
    return pxc*prior 
     
    
