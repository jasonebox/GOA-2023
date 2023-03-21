#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:26:22 2023

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

fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/GLAMBIE/example_csv_svalbard.csv'
df=pd.read_csv(fn)

cols=df.columns
print(df.columns)
print(df)

# region_name=['Iceland','Svalbard','Russian-Arctic','Alaska','Arctic-Canada-North','Arctic-Canada-South','Scandinavia']
# region_name2=['Iceland','Svalbard and Jan Mayen','Russian Arctic','Alaska','Arctic Canada, North','Arctic Canada, South','Scandinavia']
# RGI_ID=['6','7','9','1','3','4','8']
# n_regional_composites=len(RGI_ID)

# for i in range(0, n_regional_composites):
#     print(i,RGI_ID[i])
#     if i>=0:
#         x=pd.read_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/ArcticInSituvGRACE_'+region_name[i]+'_mass_balance_1971-2022.csv')
#         x.columns
#         x.uncertainty_mass_balance[x.uncertainty_mass_balance>50]==49.99
#         out_fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/GLAMBIE/'+region_name[i]
#         out=open(out_fn+'.csv','w')
#         out.write('region;region_id;start_date;end_date;glacier_change_observed;glacier_change_uncertainty;unit;glacier_area_reference;glacier_area_observed;remarks\n')

#         for yy,year in enumerate(x.year):
#             start_date='15/09/'+str(year-1)
#             end_date='15/09/'+str(year)
#             print(region_name2[i],RGI_ID[i],start_date,end_date,x.mass_balance[yy],x.uncertainty_mass_balance[yy],'Gt','N/A','N/A')
#             if ~np.isnan(x.mass_balance[yy]):
#                 out.write(region_name2[i]+';'+\
#                           RGI_ID[i]+';'+\
#                           start_date+';'+\
#                           end_date+';'+\
#                           str("%.2f"%x.mass_balance[yy])+';'+\
#                           str("%.2f"%x.uncertainty_mass_balance[yy])+';'+\
#                           'Gt'+';'+\
#                           'nan'+';'+\
#                           'nan'+';'+\
#                           'update to Box et al 2018\n')
#         out.close()

region_name=['Iceland','Svalbard','Russian-Arctic','Alaska','Arctic-Canada-North','Arctic-Canada-South','Scandinavia']
region_name2=['Iceland','Svalbard and Jan Mayen','Russian Arctic','Alaska','Arctic Canada, North','Arctic Canada, South','Scandinavia']
areas=[11060,33958,51591,86725,105128,40888,2949]
RGI_ID=['6','7','9','1','3','4','8']
n_regional_composites=len(RGI_ID)

for i in range(0, n_regional_composites):
    print(i,RGI_ID[i])
    if i>=0:
        x=pd.read_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/ArcticInSituvGRACE_'+region_name[i]+'_mass_balance_1971-2022.csv')
        x.columns
        x.uncertainty_mass_balance[np.isnan(x.uncertainty_mass_balance)]==0
        out_fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/GLAMBIE_ArcticInSituvGRACE_submission_comma_sep/'+region_name[i]
        out=open(out_fn+'.csv','w')
        out.write('region_id,start_date,end_date,glacier_change_observed,glacier_change_uncertainty,unit,glacier_area_reference,glacier_area_observed,remarks\n')

        sep=','

        for yy,year in enumerate(x.year):
            start_date='15/09/'+str(year-1)
            end_date='15/09/'+str(year)
            print(region_name2[i],RGI_ID[i],start_date,end_date,x.mass_balance[yy],x.uncertainty_mass_balance[yy],'Gt','N/A','N/A')
            if (~np.isnan(x.mass_balance[yy])&(~np.isnan(x.uncertainty_mass_balance[yy]))):
                out.write(RGI_ID[i]+sep+\
                          start_date+sep+\
                          end_date+sep+\
                          str("%.2f"%x.mass_balance[yy])+sep+\
                          str("%.2f"%x.uncertainty_mass_balance[yy])+sep+\
                          'Gt'+sep+\
                          str(areas[i])+sep+\
                          str(areas[i])+sep+\
                          'update to Box et al 2018\n')
        out.close()