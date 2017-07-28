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
Original problem:
    
    CPT:
        X    |   X - 1   |  P  |
        -----------------------|
        sun  |   sun     | 0.9 |
        rain |   sun     | 0.1 |
        sun  |   rain    | 0.3 |
        rain |   rain    | 0.7 |
        

taken from Pieter Abbeel lecture on HMM
'''


class Experiment:    
    def __init__(self, variables, lists):
        """
        variables : list of variable names
        lists : each combination of each variable names.
        """
        lists = list (product(*lists ))
        self.omega = DataFrame(lists)        
        self.omega["Tally"] = pd.Series(0, index=self.omega.index)        
        self.omega["Label"] = pd.Series("", index=self.omega.index)
        variables.append("Tally")
        variables.append("Label")
        self.omega.columns = variables
        
    def set(self, expression, value):
        self.omega.loc[expression,"Tally"] = value
        
    def __str__(self):
        return "%s" % self.omega
        
    def p(self,f):  
        ''' check probability of a random variable '''
        df_f = self.omega.loc[f]
        pf = df_f["Tally"].sum() * 1.0 / self.omega["Tally"].sum()
        return pf

    
    def p_given(self,f,g):        
        omega_g = self.omega.loc[g]        # restrict sample down to g
        tally_g = omega_g["Tally"].sum()
        
        omega_f = omega_g.loc[f]
        tally_f = omega_f["Tally"].sum()
        
        return tally_f * 1.0/ tally_g
        
    def cptrand(self, list, probability):
        ''' 
        this function accept a list of names and list of probabilities (must sum to 1 so make normalization as needed.
        will return the chosen variable from name according to the randomizer according to probability.
        sample dict:
             a = cpt_random([])
            
             np.random.multinomial(1, [1/3.0, 2/3.0, 0, 0])
             Out[60]: array([0, 1, 0, 0])
        '''

        p = np.random.multinomial(1, probability)
        i = 0
        for x in p:
            if x == 1:
                return list[i]
            i = i + 1
                
        return ""
        
    def hmm(self,day1):
        if (day1 == "Sun"):
            day2 = self.cptrand(["Sun","Rain"], [0.9, 0.1])
        else:
            day2 = self.cptrand(["Sun","Rain"], [0.3, 0.7])
        return day2
        
    
    '''
    Original problem:
        
        CPT:
            Xt-1 |   Xt      |  P (Xt | Xt-1) |
            ----------------------------------|
            sun  |   sun     |   0.9          |
            sun  |   rain    |   0.1          |
            rain |   sun     |   0.3          |
            rain |   rain    |   0.7          |
            
    
    taken from Pieter Abbeel lecture on HMM
    
    '''
    def sample(self, num, initial):
        r = range(num)
        day1 = [initial] * num
        day2 = []
       
        for d in day1:
            nextday = self.hmm(d)    
            day2.append(nextday)
            
        for i in r:
            d1 = day1[i]
            d2 = day2[i]
            
            self.omega.loc[(self.omega["X1"]==d1) & (self.omega["X2"]==d2), "Tally"] += 1   
                           
    def reset(self):
        self.omega.loc[:,"Tally"] = 0

# let's create the sample space. We got two variables "Door" and "Prize" and "Strategy"
# (chosen)Door and Prize is either A,B,C
# Strategy is either "Switch" or "Stick".
# calling the class will expand the sample space by all possibilities.
ex = Experiment( ["X1","X2"], [["Rain","Sun"], ["Rain","Sun"]] )
#initial is Sun 
ex.sample(100, "Sun") 


print ex
print ex.p( ex.omega["X2"]=="Sun" )  
print ex.p( ex.omega["X2"]=="Rain" ) 

# initial is Rain
ex.reset()
ex.sample(100, "Rain") 

print ex
print ex.p( ex.omega["X2"]=="Sun" )  
print ex.p( ex.omega["X2"]=="Rain" ) 

  

