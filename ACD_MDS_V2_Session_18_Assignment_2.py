# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 14:33:39 2018

@author: Eliud Lelerai
"""

import numpy as pd
import pandas as pd
from scipy import stats
import math

# computing mean,variance and standard deviation for proportions

#state1 
p1=0.52
q1=0.48
n1=100
state1_mean=n1*p1
state1_var=n1*p1*q1
standerr1=state1_var/n1

#state2
p2=0.47
q2=0.53
n2=100
state2_mean=n2*p2
state2_var=n2*p2*q2
standerr2=state2_var/n2


   
#Step-2: Computing the random chance probability of difference using z score

mean_diff=(state2_mean-state1_mean)

diff_standard_error=math.sqrt(standerr1+standerr2)

z=mean_diff/diff_standard_error

import scipy.stats as st

z_prob=st.norm.cdf(-7.080)


#Step-3:  probability that the survey will show a greater percentage of Republican
         #voters in the second state than in the first state?

print(z_prob)

#It is almost zero


