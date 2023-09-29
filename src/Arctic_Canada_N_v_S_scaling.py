#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:09:10 2023

Note:
    mb_annual_hydrological obtained from /Users/jason/Dropbox/GRACE/Wouters/GRACE_Arctic_Wouters/GRACE_Arctic.py
    but has issues related to my attempts to in-fill gaps...
    A more robust solution to the goal of obtaining a 2002-2015 average mass change is to fit to multi-annual monthly results using:
        /Users/jason/Dropbox/GRACE/Wouters/GRACE_Arctic_Wouters/comp_Wouters_GRACE.py

@author: jason

Notes:
    RegionnS(km2)V(km3)
    Arctic Canada North 3,205    105,139    34,399+/-4,699
    Arctic Canada South 6,67940,893 9,814+/-1,115
    
    ACN_volume=34,399+/-4,699
    ACS_volume=9,814+/-1,115

""" 

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from datetime import datetime 
from numpy.polynomial.polynomial import polyfit

if os.getlogin() == 'jason':
    base_path = '/Users/jason/Dropbox/GRACE/Wouters/GRACE_Arctic_Wouters'

fn='/Users/jason/Dropbox/GRACE/Wouters/GRACE_Arctic_Wouters/output/Arctic_Canada_South_hydrological_year.csv'
ACS=pd.read_csv(fn)
ACS.columns
v=ACS.year<2016
S=np.nanmean(ACS.mass_balance_sept_to_sept_Gt[v])
print(S)

fn='/Users/jason/Dropbox/GRACE/Wouters/GRACE_Arctic_Wouters/output/Arctic_Canada_North_hydrological_year.csv'
ACN=pd.read_csv(fn)
# ACS.columns
v=ACN.year<2016
N=np.nanmean(ACN.mass_balance_sept_to_sept_Gt[v])
print(N)

N_S_ratio=N/S
print(N/S)

fig, ax = plt.subplots(figsize=(12,12))

plt.plot(ACN.year[v],ACN.mass_balance_sept_to_sept_Gt[v],label='ACN mass_balance_sept_to_sept_Gt')
plt.plot(ACS.year[v],ACS.mass_balance_sept_to_sept_Gt[v],label='ACS mass_balance_sept_to_sept_Gt')
plt.legend()

#%%
N_S_ratio=1.0654 # obtained from Wouters 2023 GLAMBIE data using:
    # /Users/jason/Dropbox/GRACE/Wouters/GRACE_Arctic_Wouters/GRACE_Arctic.py
    # /Users/jason/Dropbox/GRACE/Wouters/GRACE_Arctic_Wouters/comp_Wouters_GRACE.py

print(N/S)

#%%

fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/ArcticInSituvGRACE_Arctic-Canada_mass_balance_1971-2022.csv'
os.system('ls -lF '+fn)
AC=pd.read_csv(fn)

ACN_scaled=AC.copy()
ACS_scaled=AC.copy()

ACN_scaled.mass_balance=AC.mass_balance/2*N_S_ratio
ACS_scaled.mass_balance=AC.mass_balance/2/N_S_ratio

ACN_scaled.uncertainty_mass_balance=AC.uncertainty_mass_balance*N_S_ratio
ACS_scaled.uncertainty_mass_balance=AC.uncertainty_mass_balance/N_S_ratio

ACN_scaled.to_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/ArcticInSituvGRACE_Arctic-Canada-North_mass_balance_1971-2022.csv',
                              index=False, float_format="%.2f")
ACS_scaled.to_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/ArcticInSituvGRACE_Arctic-Canada-South_mass_balance_1971-2022.csv',
                              index=False, float_format="%.2f")