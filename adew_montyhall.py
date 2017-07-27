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
    
  Monty Hall hosts a quiz, in it hidden one prize behind one door.
  There are three doors: A,B,C.
  You have to choose one door.
  Monty then open one door, that is neither your pick nor having the prize.
  So there's left two doors now.
  Do you switch door? or do you stick? Which is better strategy?

Monty Hall problem taken from A. Downey's book.
'''


class Experiment:    
    def __init__(self, variables, lists):
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
        df_f = self.omega.loc[f]
        pf = df_f["Tally"].sum() * 1.0 / self.omega["Tally"].sum()
        return pf

    
    def p_given(self,f,g):        
        omega_g = self.omega.loc[g]        # restrict sample down to g
        tally_g = omega_g["Tally"].sum()
        
        omega_f = omega_g.loc[f]
        tally_f = omega_f["Tally"].sum()
        
        return tally_f * 1.0/ tally_g
        
    def sample(self,num):
                
        prizes = np.random.randint(1,4,num)
        doors = np.random.randint(1,4,num) # hundred times.
        strategy = np.random.randint(1,3,num) # hundred times.
        r = range(num)
        
        for i in r:
            p = prizes[i]
            d = doors[i]            
            s = "switch" if strategy[i] == 1 else "stick"
            
            self.omega.loc[(self.omega["Prize"]==str(p)) & (self.omega["Door"]==str(d)) & (self.omega["Strategy"]==s), "Tally"] += 1
                           
    def assignlabels(self):
        for i,r in self.omega.iterrows():
            
            if r["Strategy"] == "stick":
                
                self.omega.loc[i, "Label"] = "Win" if r["Door"] == r["Prize"] else "Lose"
            else: #switch
                self.omega.loc[i, "Label"] = "Win" if r["Door"] != r["Prize"] else "Lose"
        
         
    
# let's create the sample space. We got two variables "Door" and "Prize" and "Strategy"
# (chosen)Door and Prize is either A,B,C
# Strategy is either "Switch" or "Stick".
# calling the class will expand the sample space by all possibilities.
ex = Experiment(["Prize","Door","Strategy"], [["1","2","3"], ["1","2","3"], ["switch","stick"]] )
ex.assignlabels()
ex.sample(1000)
print ex

# how much probability for "switch" strategy ?
print ex.p_given(ex.omega["Label"] == "Win", ex.omega["Strategy"] == "switch")
# how much probability for "stick" strategy ?
print ex.p_given(ex.omega["Label"] == "Win", ex.omega["Strategy"] == "stick")






  

