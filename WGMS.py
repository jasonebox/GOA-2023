#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 07:51:48 2023

@author: jason
"""


# import rasterio
import glob
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
# from collections import Counter
# import matplotlib.animation as animation
import matplotlib as mpl 
# from shapely import geometry
# import geopandas as gpd


fs=20
th=1
# plt.rcParams['font.sans-serif'] = ['Georgia']
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
co=0.9; plt.rcParams['grid.color'] = (co,co,co)
plt.rcParams["font.size"] = fs
plt.rcParams['legend.fontsize'] = fs*0.8
plt.rcParams['mathtext.default'] = 'regular'



fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/DOI-WGMS-FoG-2022-09/data/glacier.csv'
GLACIER=pd.read_csv(fn, encoding = "ISO-8859-1")

# print(GLACIER.columns)

fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/DOI-WGMS-FoG-2021-05/WGMS-FoG-2021-05-EE-MASS-BALANCE.csv'
fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/DOI-WGMS-FoG-2021-05/WGMS-FoG-2021-05-EEE-MASS-BALANCE-POINT.csv'
info=pd.read_csv(fn, encoding = "ISO-8859-1")
fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/DOI-WGMS-FoG-2022-09/data/mass_balance.csv'
df=pd.read_csv(fn, encoding = "ISO-8859-1")
# fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/DOI-WGMS-FoG-2021-05/WGMS-FoG-2021-05-E-MASS-BALANCE-OVERVIEW.csv'
# INVESTIGATOR=pd.read_csv(fn, encoding = "ISO-8859-1")
# print(df.columns)
# print(INVESTIGATOR.columns)
# print(info.columns)

fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/glaciers.csv'
glaciers=pd.read_csv(fn,names=['name','region'])
gl=[]
for i in glaciers.name:
    # print(i)
    name=i.upper()
    gl.append(name)
    # v=info.NAME==name
    
    # print(name,lat[len(lat)])

    # print(df.NAME[v[0]])#,df.POLITICAL_UNIT[v[0]],df.WGMS_ID[v[0]])

# gl´np.a


# v=((df.NAME=="DEVON ICE CAP NW") & (df["BALANCE_CODE"]=='BA'))
iyear=1971 ; fyear=2022 ; n_years=fyear-iyear+1
years_int=np.arange(iyear,fyear+1).astype(int)
years=np.arange(iyear,fyear+1).astype(str)

df_all=pd.DataFrame({'year':years_int})

wo=1

for i,glacier in enumerate(gl):
    # if i==0:
    # if glacier=='DEVON ICE CAP NW':
    # if glacier=='STORGLACIAEREN':
    if glacier!='null':
        v2=info.NAME==name
        v=np.where(GLACIER.NAME==glacier)
        lat=np.array(GLACIER.LATITUDE[v[0]].values)
        lat=lat[-1]
        lon=np.array(GLACIER.LONGITUDE[v[0]].values)
        lon=lon[-1]
        # v=np.where(INVESTIGATOR.NAME==glacier)
        # investigator=np.array(INVESTIGATOR.SPONS_AGENCY[v[0]].values)
        # investigator=investigator[-2]

        print(glacier,sum(v2),lat,lon)
        
        MB=np.zeros(n_years)*np.nan
        MB_cum=np.zeros(n_years)*np.nan
        
        temp=0.
        
        for yy in range(n_years):
            v=((df.NAME==glacier) & (df.YEAR==yy+iyear) &  (df.UPPER_BOUND==9999))
            # print(yy+iyear,sum(v))
            if glacier=='DEVON ICE CAP NW' and yy+iyear==2021:
                MB[yy]=-5/1000
                temp+=MB[yy]
                MB_cum[yy]=temp                
            if glacier=='DEVON ICE CAP NW' and yy+iyear==2022:
                MB[yy]=-576/1000
                temp+=MB[yy]
                MB_cum[yy]=temp      
            if glacier=='AUSTRE BROEGGERBREEN' and yy+iyear==2022:
                MB[yy]=-1393/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='MIDTRE LOVENBREEN' and yy+iyear==2022:
                MB[yy]=-1239/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='KONGSVEGEN' and yy+iyear==2022:
                MB[yy]=-968/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='WALDEMARBREEN' and yy+iyear==2020:
                MB[yy]=-2276/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='WALDEMARBREEN' and yy+iyear==2021:
                MB[yy]=-947/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='IRENEBREEN' and yy+iyear==2020:
                MB[yy]=-2204/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='IRENEBREEN' and yy+iyear==2021:
                MB[yy]=-705/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='LANGFJORDJOEKELEN' and yy+iyear==2022:
                MB[yy]=-1900/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='RABOTS GLACIAER' and yy+iyear==2021:
                MB[yy]=-500/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='RABOTS GLACIAER' and yy+iyear==2022:
                MB[yy]=-943/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='STORGLACIAEREN' and yy+iyear==2021:
                MB[yy]=-823/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='STORGLACIAEREN' and yy+iyear==2022:
                MB[yy]=-212/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='ENGABREEN' and yy+iyear==2022:
                MB[yy]=150/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='HOFSJOEKULL N' and yy+iyear==2022:
                MB[yy]=280/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='HOFSJOEKULL E' and yy+iyear==2022:
                MB[yy]=-190/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='HOFSJOEKULL SW' and yy+iyear==2022:
                MB[yy]=460/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='BRUARJOKULL' and yy+iyear==2022:
                MB[yy]=344/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='DYNGJUJOKULL' and yy+iyear==2022:
                MB[yy]=422/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='EYJABAKKAJOKULL' and yy+iyear==2022:
                MB[yy]=-359/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='LANGJOKULL ICE CAP' and yy+iyear==2022:
                MB[yy]=-50/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='TUNGNAARJOKULL' and yy+iyear==2022:
                MB[yy]=-1355/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='KOLDUKVISLARJ.' and yy+iyear==2022:
                MB[yy]=386/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='GULKANA' and yy+iyear==2022:
                MB[yy]=-1160/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='AUSTDALSBREEN' and yy+iyear==2021:
                MB[yy]=-1775/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='AUSTDALSBREEN' and yy+iyear==2022:
                MB[yy]=-50/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='AALFOTBREEN' and yy+iyear==2022:
                MB[yy]=-550/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='HANSEBREEN' and yy+iyear==2021:
                MB[yy]=-2335/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='HANSEBREEN' and yy+iyear==2022:
                MB[yy]=-1050/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='NIGARDSBREEN' and yy+iyear==2022:
                MB[yy]=800/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='GRAASUBREEN' and yy+iyear==2021:
                MB[yy]=-1541/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='STORBREEN' and yy+iyear==2021:
                MB[yy]=-1672/1000
                temp+=MB[yy]
                MB_cum[yy]=temp 
            if glacier=='WOLVERINE' and yy+iyear==2022:
                 MB[yy]=-1180/1000
                 temp+=MB[yy]
                 MB_cum[yy]=temp 
            if glacier=='MEIGHEN ICE CAP' and yy+iyear==2022:
                 MB[yy]=-762/1000
                 temp+=MB[yy]
                 MB_cum[yy]=temp 
            if sum(v)>0:
                MB[yy]=df.ANNUAL_BALANCE[v]/1000
                temp+=MB[yy]
                MB_cum[yy]=temp
        print(glacier,yy+iyear,sum(v),MB[yy])
        
        MBx=MB.copy()
        MBx*=1000
        v=~np.isnan(MBx)
        MBx[v]=MBx[v].astype(int)
        output=pd.DataFrame({'year':years_int,glacier:MBx})
        df_all=df_all.merge(output,on='year')
# print(df_all)
# #%%
        do_plot=0
        if do_plot:
            plt.close()
            fig, ax = plt.subplots(figsize=(10.5,10))
    
            plt_cum=1
            nam=''
            if plt_cum:
                ax.plot(years_int,MB_cum,zorder=20,c='k')
                ax.fill_between(years_int, 0, MB_cum, where=MB_cum>0, color='b',alpha=0.5,interpolate=True)
                ax.fill_between(years_int, 0, MB_cum, where=MB_cum<0, color='r',alpha=0.5,interpolate=True)
                ax.set_ylabel('cumulative mass balance\ntons water per square meter')#'m$^{-2}$')
                nam='_cum'
            else:
                ax.plot(years_int,MB,zorder=20,c='k') #, drawstyle='steps-mid'
                ax.fill_between(years_int, 0, MB, where=MB>0, color='b',alpha=0.5,interpolate=True)
                ax.fill_between(years_int, 0, MB, where=MB<0, color='r',alpha=0.5,interpolate=True)
                ax.set_ylabel('mass balance tons water per square meter')#'m$^{-2}$')
            ax.set_title(glacier)
            ax.tick_params(which='major', labelrotation=90)
            xos=0.4
            ax.set_xlim(min(years_int)-xos,max(years_int)+xos)
            mult=0.9
            xx0=0.05
            ax.text(xx0,0.08, "@climate_ice, data via WGMS",transform=ax.transAxes, fontsize=fs*mult,
                verticalalignment='top',rotation=0,color='grey', rotation_mode="anchor")  
            # ax.text(xx0,0.08, "@climate_ice, data via WGMS via\n"+investigator,transform=ax.transAxes, fontsize=fs*mult,
            #     verticalalignment='top',rotation=0,color='grey', rotation_mode="anchor")  
            plt.xticks(np.arange(min(years_int), max(years_int)+1, 2.0))

            ly='p'
            if ly == 'x':plt.show()
            
            fig_path='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/Figs/'
            if ly == 'p':
                plt.savefig(fig_path+glacier+nam+'.png', bbox_inches='tight', dpi=200)
                # if plt_eps:
                #     plt.savefig(fig_path+site+'_'+str(i).zfill(2)+nam+'.eps', bbox_inches='tight')

if wo:
    df_all.to_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/WGMS_compilation_GOA.csv')
