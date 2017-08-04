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
    
How to check independence of random variable?

X,Y independent if and only if ⩝ x, y  P(x, y) = P(x) P(y)


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
    
           
  #  def is_independent(self,p,q):
  #      two random variables are independent if for all possible values of the two, 
  #      the joint probability of the two equals to multiplication of the probability of
  #      the first value times the probability of the second value.
  #      X,Y independent if and only if ⩝ x, y  P(x, y) = P(x) P(y)
  #
  #         how to verify that these random variable independent one another?
  #         it means that we verify (for rain/sun case):
  #             1. P ( x1 = rain and x2 = rain ) = P ( x1 = rain )  x P ( x2 = rain )
  #             2. P ( x1 = rain and x2 = sun  ) = P ( x1 = rain )  x P ( x2 = sun  )
  #             3. P ( x1 = sun  and x2 = rain ) = P ( x1 = sun  )  x P ( x2 = rain )
  #             4. P ( x1 = sun  and x2 = sun  ) = P ( x1 = sun  )  x P ( x2 = sun  )
  #         so for each of these combos we need to verify that case.     

    def is_independent(self, _list):
        elements = []
        for l in _list:
            elements.append ( list( self.omega[l].unique() ) )
        combo = list (product (*elements))
        df = DataFrame(combo)
        df.columns = _list
        
        print df
        
        
        # we are checking for each combination of x , y if the P(x,y) equals to P(x) P(y)
        # c = self.p( ex.omega["Intelligence"]==value1 & ex.omega["University"]==value2 )
        # 
        
        for row in df.itertuples(index = False):
            col_idx = 0
            q = self.omega # reset query 
            px_py = 1
            
            for col in row:
                
                colname = df.columns[col_idx]
                print colname + " == '" + col + "'"           
                p_x = self.p(self.omega[colname]==col)
               
                px_py = px_py * p_x
                
                q = q.query( df.columns[col_idx] + " == '" + col + "'" )
                col_idx = col_idx + 1
                
            p_xy = q["Tally"].sum() * 1.0 / self.omega["Tally"].sum()
            
            print px_py
            print p_xy
            if (px_py != p_xy):
                return False
                
        return True
                 
         
    def cptrand(self, list, probability):
        ''' 
        this function accept a list of names and list of probabilities (must sum to 1 so make normalization as needed.
        will return the chosen variable from name according to the randomizer according to probability.

        '''

        p = np.random.multinomial(1, probability)
        i = 0
        for x in p:
            if x == 1:
                return list[i]
            i = i + 1
                
        return ""
                                
    def reset(self, tally=0):
        self.omega.loc[:,"Tally"] = tally
        
   

# let's create the sample space. We got two variables "Door" and "Prize" and "Strategy"
# (chosen)Door and Prize is either A,B,C
# Strategy is either "Switch" or "Stick".
# calling the class will expand the sample space by all possibilities.
ex = Experiment( ["Intelligence","University","Sex"], [["Smart","Normal","Below"], ["MIT","ZonkUni"], ["Male","Female"]] )
#initial is Sun 


#ex.set( ex.omega[:], 1 )
ex.reset(1)

print ex

# sex is independent to university
print ex.is_independent( ["Sex","University"] )

# intelligence is independent to university
print ex.is_independent( ["Intelligence","University"] )

# now what if we slightly change the tally by telling that no MIT student are having Intelligence below normal
ex.set((ex.omega["Intelligence"] == "Below") & (ex.omega["University"] == "MIT"), 0)

# lets print the dist table
print ex

# intelligence is dependent to university
# it is not independent anymore since it is observed that Intelligence and University have special correlation

print ex.is_independent( ["Intelligence","University"] )

# what about sex? does it still hold independent?
print ex.is_independent( ["Sex", "Intelligence"] )

