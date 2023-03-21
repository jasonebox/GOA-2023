#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:09:10 2023

@author: jason
"""

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable
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

#%%

fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/ArcticInSituvGRACE_Arctic-Canada_mass_balance_1971-2022.csv'
AC=pd.read_csv(fn)

ACN_scaled=AC.copy()
ACS_scaled=AC.copy()

ACN_scaled.mass_balance=AC.mass_balance*(1-N_S_ratio)
ACS_scaled.mass_balance=AC.mass_balance*N_S_ratio

ACN_scaled.uncertainty_mass_balance=AC.uncertainty_mass_balance*(1-N_S_ratio)
ACS_scaled.uncertainty_mass_balance=AC.uncertainty_mass_balance*N_S_ratio

ACN_scaled.to_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/ArcticInSituvGRACE_Arctic-Canada-North_mass_balance_1971-2022.csv',
                              index=False, float_format="%.2f")
ACS_scaled.to_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/ArcticInSituvGRACE_Arctic-Canada-South_mass_balance_1971-2022.csv',
                              index=False, float_format="%.2f")