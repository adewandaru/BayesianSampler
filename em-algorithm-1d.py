# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 06:40:02 2018
EM algorithm toy example: 1 Dimensional.

@author: dewandaru@gmail.com

"""



import matplotlib.pyplot as plt
import numpy as np
import math


# This is the training data.
mu1 = 3
sigma = 1
t1 = np.random.normal(mu1, sigma, 1000)
#plt.plot(t)
plt.hist(t1, bins=100)

mu2 = 7
t2 = np.random.normal(mu2, sigma, 1000)
plt.hist(t2, bins=100)

x = np.concatenate([t1,t2])
np.random.shuffle(x)

plt.gcf.clear()


'''
 EM algorithm is iterative between calculating :
 1. Expectation membership p(cluster|x) and
 then 
 2. Finding parameter which Maximizing the *likelihood* / 
 [moving cluster center's mu and sigma]
'''

mu = [0, 10]
sigma = [1, 1]



def prior(pcx):
    return pcx.mean()

def p_x_given_c(x, mu, sigma_squared):
    ''' just a typical normal pdf '''
    return np.exp( -(x-mu)**2 / (2 * sigma_squared) ) / np.sqrt( 2 * math.pi * sigma_squared )   

def p_c_given_x(x, mu1, sigma1, mu2, sigma2, prior):
    ''' 
    calculate responsibility p(c|x) for each datapoint. where c is the cluster.
                   p(x|c) p(c)              p(x|c) p(c)                  p(x|c) p(c) [prior]
    p(c|x) =  --------------------- = ------------------------- =  -------------------------------
                      p(x)                  sum(c) p(x,c)             p(x|c) p(c) + p(x|c') p(c')  
    '''
    nom = p_x_given_c(x, mu1, sigma1) * prior
    evidence = nom + p_x_given_c(x, mu2, sigma2 ) * (1-prior)
    return nom / evidence

pcfx = np.vectorize(p_c_given_x)

pa = 0.5
pb = 0.5

for i in range(100):
    print "#"+str(i)
    '''
    
    Expectation step: calculate "responsibility" of each cluster to each datapoints.
    a.k.a which 
    p_c1 = P(c1|x) = ...
    p_c2 = P(c2|x) = ...
    
    '''
    
    a = p_c_given_x( x, mu[0], sigma[0], mu[1], sigma[1], pa )
    b = 1 - a
    
    
    pa = prior(a)
    pb = 1 - pa
    
    '''
    Maximization of Likelihood 
    adjust mu and sigma 
    '''
    mu[0] = np.multiply(a, x).sum() / a.sum()
    sigma[0] = np.multiply(a, (x - mu[0])**2).sum() / a.sum() 
    
    mu[1] = np.multiply(b, x).sum() / b.sum()
    sigma[1] = np.multiply(b, (x - mu[1])**2).sum() / b.sum() 
    
    print "mu" 
    print mu
    print "sigma" 
    print sigma
    print "pa-pb"
    print pa
    print pb


    


     
    
