#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:49:16 2022

@author: jasmindersingh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import statsmodels.api as sm

data = pd.read_csv("hmeq.csv")
print(data.shape) 
data.fillna(0)

# create a list of our conditions
conditions = [
    (data['BAD'] != 1),
    ((data['CLAGE'] > 150) | (data['DELINQ'] > 2) & (data['DEBTINC'] > 28)),
    ((data['CLAGE'] <= 150) | (data['DEROG'] >= 1)),
    ((data['BAD'] == 1))]

# create a list of the values we want to assign for each condition
values = ['LOW', 'MEDIUM', 'HIGH', 'NEED MORE DATA']

# create a new column and use np.select to assign values to it using our lists as arguments
data['RISK'] = np.select(conditions, values)
data.fillna(0)