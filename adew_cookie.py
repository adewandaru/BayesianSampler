# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:40:23 2017

@author: dewandaru@gmail.com
"""

from itertools import product
import pandas as pd
import numpy as np
from pandas import DataFrame
'''
Original question:
    
    Suppose there are two bowls of cookies.
    Bowl 1 contains 30 of Vanilla and 10 of Chocolates.
    Bowl 2 contains 20 of Vanilla and 20 of Chocolates.
    Suppose choosing bowl randomly and picking one of the cookies. 
    The cookie is vanilla. What is the probability it comes from Bowl 1?

This cookie problem taken from A. Downey's book and we will adapt it using BayesianSampler
to solve it.

'''


# let's select vanilla
#vanilla = om.loc[om["Flavor"]=="vanilla"] 

#bowl1_given_vanilla = vanilla.loc[om["Bowl"]=="b1"]

# now let's count the bowl1 probability given vanilla


class Experiment:    
    def __init__(self,variables, lists):
        lists = list (product(*lists ))
        self.omega = DataFrame(lists)
        self.omega["Tally"] = pd.Series(0, index=self.omega.index)
        variables.append("Tally")
        self.omega.columns = variables
        
    def set(self, expression, value):
        self.omega.loc[expression,"Tally"] = value
        
    def __str__(self):
        return "%s" % self.omega
        
    def p(self,f):  
        df_f = self.omega.loc[f]
        pf = df_f["Tally"].sum() * 1.0 / self.omega["Tally"].sum()
        return pf

    
    def p_given(self,f,g):        
        omega_g = self.omega.loc[g]        # restrict sample down to g
        tally_g = omega_g["Tally"].sum()
        
        omega_f = omega_g.loc[f]
        tally_f = omega_f["Tally"].sum()
        
        return tally_f * 1.0/ tally_g
    
# let's create the sample space. We got two variables "Flavor" and "Bowl"
# Flavor can be vanilla and choco.
# Bowl can be b1 or b2.
# calling the class will expand the sample space by all possibilities.
ex = Experiment(["Flavor","Bowl"], [["vanilla","choco"], ["b1","b2"]] )

# we will set the tally to match the experiment configuration.
ex.set( (ex.omega["Bowl"]=="b1") & (ex.omega["Flavor"]=="vanilla"), 30 )
ex.set( (ex.omega["Bowl"]=="b1") & (ex.omega["Flavor"]=="choco"), 10 )

ex.set( (ex.omega["Bowl"]=="b2") & (ex.omega["Flavor"]=="vanilla"), 20 )
ex.set( (ex.omega["Bowl"]=="b2") & (ex.omega["Flavor"]=="choco"), 20 )

# what do we have?
print ex

# what is the probability of Bowl1 given Vanilla? == P(b1|vanilla) 
print ex.p_given( ex.omega["Bowl"]=="b1", ex.omega["Flavor"]=="vanilla" ) 

# what is the probability of Bowl1 and Vanilla both picked?
print ex.p( ( ex.omega["Bowl"]=="b1" ) & ( ex.omega["Flavor"]=="vanilla" ) ) 


  

