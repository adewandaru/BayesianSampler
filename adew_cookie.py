# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:40:23 2017

@author: user
"""

from itertools import product
import pandas as pd
import numpy as np

# creating sample space
omega = np.array (list (product(["van","choco"], ["b1","b2"])))
omega = np.insert(omega,2,values=[1,1,1,1],axis=1)
    
# now let see the probability of each following random events
#sum_is_seven = list(filter(lambda x: x[0] + x[1] == 7, omega))


#red_is_even = list(filter(lambda x: x[0] % 2 == 0, omega))
bowl1 = list(filter(lambda x: x[1] == "b1", omega))

