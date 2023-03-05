#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 05:22:08 2019

@author: jason
"""
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from numpy.polynomial.polynomial import polyfit
from matplotlib.ticker import FormatStrFormatter
import matplotlib as mpl
from datetime import date

today = date.today()
versionx= today.strftime('%Y%m%d')

fs=22

plt.rcParams['font.sans-serif'] = ['Georgia']
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = "grey"
plt.rcParams["font.size"] = fs
#params = {'legend.fontsize': 20,
#          'legend.handlelength': 2}
plt.rcParams['legend.fontsize'] = fs*0.8

th=1
ss=10
do_plot_1=0 # not the final plot

plt.close()
#fig, ax = plt.subplots()

i_standard_year=2003
f_standard_year=2015

iyear=1971 ; fyear=2022
n_years=fyear-iyear+1
fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/WGMS_compilation_GOA.csv'
WGMS_data = pd.read_csv(fn)

fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/GRACE_Wouters/Wouters_MB_sorted_Canada_as_one.txt'
dfGRACE = pd.read_csv(fn, header=None, sep='\t' )
dfGRACE.loc[:,0]=-dfGRACE.loc[:,0]


# fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/region_names.txt'
# df_region_name = pd.read_csv(fn, header=None, sep='\t' )
# region_name=df_region_name.loc[:,0]

fn='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/glaciers.csv'
glaciers=pd.read_csv(fn,names=['name','region'])

iceland_glaciers=glaciers[glaciers.region=='Iceland'].name
iceland_glaciersx=[x.upper() for x in iceland_glaciers.values]

ArcticCanada_glaciers=glaciers[glaciers.region=='Arctic-Canada'].name
ArcticCanada_glaciers=[x.upper() for x in ArcticCanada_glaciers.values]

glaciers['region_id']=np.nan

v=glaciers.region=='Iceland' ; glaciers['region_id'][v]=0
v=glaciers.region=='Spitsbergen' ; glaciers['region_id'][v]=1
v=glaciers.region=='Russia' ; glaciers['region_id'][v]=2
v=glaciers.region=='Alaska' ; glaciers['region_id'][v]=3
v=glaciers.region=='Arctic-Canada' ; glaciers['region_id'][v]=4
v=glaciers.region=='Norway-Sweden' ; glaciers['region_id'][v]=5
v=glaciers.region=='Greenland' ; glaciers['region_id'][v]=6

# print(glaciers)

n_glaciers=len(glaciers)
mb=np.zeros((n_glaciers, n_years))*np.nan

for k in range(1,n_glaciers+1):
    mb[k-1,:]=WGMS_data.iloc[:,k+1].values.tolist()
    # print(k,glaciers.name[k])

x=iceland_glaciersx ; x.insert(0,'year')
WGMS_data_regional_selection=WGMS_data[x]
WGMS_data_regional_selection.to_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/Iceland_glaciers_annual_mass_balance_WGMS_1971-2022.csv')

x=ArcticCanada_glaciers ; x.insert(0,'year')
WGMS_data_regional_selection=WGMS_data[x]
WGMS_data_regional_selection.to_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/data/Arctic-Canada_glaciers_annual_mass_balance_WGMS_1971-2022.csv')
#%% obtain regionally scaled mass balance

year=np.arange(iyear, fyear+1)

do_plot_1=1

if do_plot_1:
    plt.close()
    fig, ax = plt.subplots(figsize=(10, 10))

std_anoms=np.zeros((n_glaciers, n_years))*np.nan
mb_scaled_all=np.zeros((n_glaciers, n_years))*np.nan

for k in range(n_glaciers):
    temp=mb[k,:]
    v=np.where((np.isfinite(temp))&(year >= i_standard_year)&(year <= f_standard_year))
    c=len(v[0])
    # print(k,glaciers.name[k],c,glaciers['region'][k])
    if c>12:
        print(k,c,glaciers['region'][k],glaciers['region_id'][k],glaciers.name[k])
        std_anom=(temp-np.nanmean(temp[v[0]]))/np.nanstd(temp[v[0]])
        std_anoms[k,:]=std_anom
        mb_scaled=(std_anom-1.)*dfGRACE.loc[glaciers['region_id'][k],0]
        mb_scaled_all[k,:]=mb_scaled
        # if glaciers['region'][k]=='Alaska':
#         if glaciers['region'][k]=='Norway-Sweden':
#             # plt.plot(year,std_anoms[k,:],label=glaciers.name[k])
#             plt.plot(year,mb_scaled_all[k,:],label=glaciers.name[k])
# plt.legend()
#        print(k,regions[k]-1,
#              glaciers.name[k],regions[k]-2,dfGRACE.loc[regions[k]-2,0])
    if glaciers.name[k]=='MEIGHEN ICE CAP':
        # sasa
#    if glaciers.name[k]=='Devon NW':
#    if glaciers.name[k]=='Gulkana':
#    if glaciers.name[k]=='Melville':
#    if glaciers.name[k]=='Meighen':
    # if glaciers.name[k]=='KONGSVEGEN':
        
        n_col=1 ; n_row=3
        if do_plot_1:
            fig, ax = plt.subplots(1, 2, sharex='col', sharey='row',figsize=(10, 10))
    
            plt.subplot(n_row, n_col, 1)
            plt.plot(year,std_anom,'-o',c=(0.0, 0.0, 0.),label='std') 
            plt.legend()
            plt.subplot(n_row, n_col, 2)
            plt.plot(year,mb_scaled,'-o',c=(0.0, 0.0, 0.6),label='mb') 
            plt.legend()
        
        temp=0.
        cum=np.zeros((n_years))
        for i in range(0, n_years):
            if abs(mb_scaled[i])<9000: temp+=mb_scaled[i]
            cum[i]=temp
        if do_plot_1:
            plt.subplot(n_row, n_col, 3)
            plt.plot(year,cum,'.',c=(0.6, 0.0, 0.),label='cumulative')
            plt.legend()



def RHI_MB(region_index,n_years,composite_mb,composite_mb_stdev):
    # Russian-High-Arctic 2010 and 2017 −22 GT/y
    # Sommer, C., Seehaus, T., Glazovsky, A., and Braun, M. H.: Brief communication: Increased glacier mass loss in the Russian High Arctic (2010–2017), The Cryosphere, 16, 35–42, https://doi.org/10.5194/tc-16-35-2022, 2022.
    
    from numpy.polynomial.polynomial import polyfit
    
    region_index=2 #RHI
    region_index_svalbard=1
    
    Svalbard_vs_RHI_slope=0.18672458037678966
    annual_rate=-22/(2017-2010)
    annual_std=6/(2017-2010)
    
    temp=0.
    cum=np.zeros((n_years))*np.nan
    for i in range(0, n_years):
        if ((i+iyear>=2010)&(i+iyear<=2017)):
            composite_mb[region_index,i]=annual_rate
            composite_mb_stdev[region_index,i]=annual_std
            temp+=composite_mb[region_index,i]
            cum[i]=temp
        else:
            composite_mb[region_index,i]=composite_mb[region_index_svalbard,i]*Svalbard_vs_RHI_slope
            composite_mb_stdev[region_index,i]=annual_std
            temp+=composite_mb[region_index,i]
            cum[i]=temp        
    
    # v=np.where((year>=2010)&(year<=2017))
    # v=np.where((year>=iyear)&(year<=fyear))
    # plt.plot(year[v[0]],cum[v[0]])
    # x=df_regional_cumulative['Svalbard'][v[0]]-df_regional_cumulative['Svalbard'][v[0][0]]
    
    # plt.plot(year[v],x)
    
    # b, m = polyfit(x,cum[v], 1)
    
    # print('Svalbard vs RHI slope',m)

    return composite_mb,composite_mb_stdev,cum

def Greenland_MB(region_index,n_years,composite_mb,composite_mb_stdev):
    # Greenland mass balance:
    # Mankoff, Ken; Fettweis, Xavier; Solgaard, Anne; Langen, Peter; Stendel, Martin; Noël, Brice; van den Broeke, Michiel R.; Karlsson, Nanna; Box, Jason E.; Kjeldsen, Kristian, 2021, "Greenland ice sheet mass balance from 1840 through next week", https://doi.org/10.22008/FK2/OHI23Z, GEUS Dataverse, V449 
    # Mankoff, K. D., Fettweis, X., Langen, P. L., Stendel, M., Kjeldsen, K. K., Karlsson, N. B., Noël, B., van den Broeke, M. R., Solgaard, A., Colgan, W., Box, J. E., Simonsen, S. B., King, M. D., Ahlstrøm, A. P., Andersen, S. B., and Fausto, R. S.: Greenland ice sheet mass balance from 1840 through next week, Earth Syst. Sci. Data, 13, 5001–5025, https://doi.org/10.5194/essd-13-5001-2021, 2021. doi: 10.5194/essd-13-5001-2021
    fn='/Users/jason/Dropbox/TMB_Mankoff/MB_SMB_D_BMB_ann.csv'
    df=pd.read_csv(fn)
    
    region_index=6 
    
    temp=0.
    cum=np.zeros((n_years))*np.nan
    for i in range(0, n_years):
        v=np.where(df.time==i+iyear)
        composite_mb[region_index,i]=df.MB[v[0]]
        composite_mb_stdev[region_index,i]=df.MB_err[v[0]]
        temp+=composite_mb[region_index,i]
        cum[i]=temp

    return composite_mb,composite_mb_stdev,cum


ly='p'

do_composite=1

if do_composite:

    # n_col=1 ; n_row=6
    # fig, ax = plt.subplots(1, n_row)
    region_name=['Iceland','Svalbard','Russian-High-Arctic','Alaska','Arctic-Canada','Norway-Sweden','Greenland']
    n_regional_composites=len(region_name)
    # n_regional_composites-=1
    
    composite_mb=np.zeros((n_regional_composites, n_years))
    composite_mb_stdev=np.zeros((n_regional_composites, n_years))

    # ------------------------------------------------------------------------- 
    columns=['year', 'Iceland','Svalbard','Russian-High-Arctic','Alaska','Arctic-Canada','Norway-Sweden','Greenland']
    df_regional_cumulative = pd.DataFrame(columns = columns) 
    df_regional_annual = pd.DataFrame(columns = columns)
    df_regional_std = pd.DataFrame(columns = columns)
    # df_regional_cumulative.index.name = 'index'
    df_regional_cumulative["year"]=pd.Series(np.arange(iyear,fyear+1))
    df_regional_annual["year"]=pd.Series(np.arange(iyear,fyear+1))
    df_regional_std["year"]=pd.Series(np.arange(iyear,fyear+1))

    for region_index in range(0, n_regional_composites):
        year=np.arange(iyear, fyear+1)

        print(region_name[region_index],region_index)
        # if ((region_index==0)): # Iceland
        # if ((region_index==1)): # Svalbard
        # if ((region_index==3)): # Alaska
        # if ((region_index==4)): # Arctic-Canada
        # if ((region_index==6)):
        # if ((region_index==0)or(region_index==1)or(region_index==3)or(region_index==4)or(region_index==5)):
#            print(region_index,region_name2[region_index])
    #        if region_name2[region_index]=='Alasregion_indexa':
            # if region_name2[region_index]=='Norway-Sweden':
            # if region_name2[region_index]=='Alaska':
            # if region_name2[region_index]=='Iceland':
            # if region_name2[region_index]=='Svalbard':
            # if region_name2[region_index]=='Arctic-Canada':
            # if region_name2[region_index]!='Icelandx':
            # if region_name[region_index]!='Greenland':
        v=np.where(glaciers.region_id==region_index)
#                print(region_index,v[0])
        temp=0.
        cum=np.zeros((n_years))
        for i in range(0, n_years):
            v2=np.where(np.isfinite(mb_scaled_all[v[0],i]))
            if len(v2[0]) > 0:
                composite_mb[region_index,i]=np.nanmean(mb_scaled_all[v[0],i])
                composite_mb_stdev[region_index,i]=np.nanstd(mb_scaled_all[v[0],i])
                temp+=composite_mb[region_index,i]
            cum[i]=temp
        if region_index==2: # RHI
            composite_mb,composite_mb_stdev,cum=RHI_MB(region_index,n_years,composite_mb,composite_mb_stdev)
        if region_index==6: # Greenland
            composite_mb,composite_mb_stdev,cum=Greenland_MB(region_index,n_years,composite_mb,composite_mb_stdev)

        df_regional_cumulative[region_name[region_index]]=pd.Series(cum)
        df_regional_annual[region_name[region_index]]=pd.Series(composite_mb[region_index,:])
        df_regional_std[region_name[region_index]]=pd.Series(composite_mb_stdev[region_index,:])
        cum*=1e9 # put in kg
        if do_plot_1:
            plt.close()
            fig, ax = plt.subplots(figsize=(12, 12))
            if region_index==0:
                year=year[14:]
                cum=cum[14:]
                
            ax.plot(year,cum,c=(1., 0.7, 0.7),linewidth=th*3) 
            ax.plot(year,cum,'o',c=(1.0, 0.0, 0.),label=region_name[region_index]+' glacial mass balance') 
    #                ax.xlabel('year')
            ax.ticklabel_format(style='plain')
            plt.xlim(1970,fyear+1)
            if region_index==0: #Iceland
                plt.ylim(-3.2e11,4e10)
            if region_index==4: # Arctic-Canada
                plt.ylim(-1.38e12,15e10)
            if region_index==6: # Greenland
                plt.ylim(-6e12,15e10)
            plt.ylabel('metric tons')
    #                plt.ax.yaxis.set_major_formatter(FormatStrFormatter('%18.0f'))
            ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    #                plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    #                ax.ticklabel_format(useOffset=False)
            # plt.legend(alpha=1)
            legend = plt.legend(loc="upper right", edgecolor="grey")
            legend.get_frame().set_alpha(1)
            # legend.get_frame().set_facecolor((0, 0, 1, 0.1))
            
            mult=0.7
            props = dict(boxstyle='round', facecolor='w', alpha=1,edgecolor='w')
            txt='Arctic Monitoring and Assessment Program (AMAP), after Box et al 2018 ERL'
            txt='Box, J.E., W.T. Colgan, B. Wouters, D.O. Burgess, S. O’Neel, L.I. Thomson, S.H. Mernild 2018. Global sea-level contribution from Arctic land ice: 1971–2017, Environmental Research Letters, ERL-105795, https://doi.org/10.1088/1748-9326/aaf2ed, updated 5 years'
            txt='after: Global sea-level contribution from Arctic land ice: 1971–2017,\nEnvironmental Research Letters,\nBox, JE, WT Colgan, B Wouters, DO Burgess, S O’Neel, LI Thomson, SH Mernild 2018. \n...updated by 5 years: 2018 to 2022\n@Climate_Ice and @AMAP_Arctic, ver. '+versionx
            yy0=0.02
            if region_name[region_index]=='Greenland':
                mult=0.59
                txt='after Mankoff, K. D., Fettweis, X., Langen, P. L., Stendel, M., Kjeldsen, K. K., Karlsson, N. B.,\nNoël, B., van den Broeke, M. R., Solgaard, A., Colgan, W., Box, J. E., Simonsen, S. B., King M. D.,\nAhlstrøm, A. P., Andersen, S. B., and Fausto, R. S.:\nGreenland ice sheet mass balance from 1840 through next week, Earth Syst. Sci. Data, 13, 5001–5025,\nhttps://doi.org/10.5194/essd-13-5001-2021, 2021. doi: 10.5194/essd-13-5001-2021\n@Climate_Ice ver. '+versionx
                yy0=0.02
    #                ax.text(0.02, 0.2,
    #                        txt,
    #                        transform=ax.transAxes, fontsize=fs*mult,
    #                        verticalalignment='top', bbox=props,rotation=0,color='grey',
    #                        rotation_mode="anchor")
            xx0=0.02 ; dy=-0.05 ; cc=0
    #                color_code='#6AD8EA'
            co=0.5
            
            if do_plot_1:
                plt.text(xx0, yy0+cc*dy, txt,fontsize=fs*mult,color=(co,co,co),transform=ax.transAxes, bbox=props) ; cc+=1.
    #                plt.text(xx0, yy0+cc*dy, date_string[0:4]+
    #                         ' '+calendar.month_name[int(month)]+
    #                         ' '+day, fontsize=font_size,color='w'
    #                         ,transform=ax.transAxes); cc+=1.
    
                if ly == 'x':
                    plt.show()
                
                figsubpath='GOA'
                figname=region_name[region_index]
                if ly == 'p':
                    figpath='/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/Figs/regional_results/'
                    os.system('mkdir -p '+figpath)
                    figname=figpath+figname+'.png'
                    plt.savefig(figname, bbox_inches='tight', dpi=100)
                    # os.system('ls -lF '+figname) 
    #                    os.system('open '+figname) 


wo=1
if wo:
    # df_regional_cumulative['Russian-High-Arctic']=df_regional_cumulative['Svalbard']*2
    # df_regional_cumulative.to_csv('/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/data_multi_indicators/glaciers/GOA_1971-2022.csv')
    df_regional_cumulative.to_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/GOA_regional_cumulative_1971-2022.csv',
                                  index=False, float_format="%.2f")
    df_regional_annual.to_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/GOA_regional_annual_1971-2022.csv',
                                  index=False, float_format="%.2f")
    df_regional_std.to_csv('/Users/jason/Dropbox/Glaciers_of_the_Arctic/GOA-2023/output/GOA_regional_std_1971-2022.csv',
                                  index=False, float_format="%.2f")
# do_gif=1

# if do_gif:
#     figpath='/Users/jason/Dropbox/AMAP/Arctic-multi-indicators/Figs/GOA/'
#     os.system('/usr/local/bin/convert -delay 250 -loop 0 '+figpath+'*v2.png '+figpath+'anim_v2.gif')
