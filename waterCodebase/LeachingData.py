#Author : Parker Shankin-Clarke (email parkerwsc1@gmail.com)
#Last Date Modified : 12/08/21
#Description :
'''
This script exports the stream and ash leaching data as pandas dataframes 
'''
#General imports
from datetime import datetime 
import pandas as pd
import numpy as np 
import sys
#creak water sampling data from leaching experiments  
SiteU =  ['U'] * 12 
SiteM =  ['M'] * 5
SiteL =  ['L'] * 5
Sites = SiteU + SiteM + SiteL
#year,month,day,hour minute,second
DT = [
      datetime(2017, 10, 21, 7, 16, 0, 0),
      datetime(2017, 11, 4, 7, 51, 0, 0),
      datetime(2017, 11, 18, 8, 25, 0, 0),
      datetime(2017, 12, 20, 8, 14, 0, 0),
      datetime(2018, 1, 13, 15, 37, 0, 0),
      datetime(2018, 1, 28, 9, 23, 0, 0),
      datetime(2018, 2, 3, 11, 37, 0, 0),
      datetime(2018, 2, 17, 8, 22, 0, 0),
      datetime(2018, 3, 11, 8, 26, 0, 0),
      datetime(2018, 3, 18, 8, 46, 0, 0),
      datetime(2018, 3, 24, 10, 27, 0, 0),
      datetime(2018, 4, 8, 8, 43, 0, 0),
      datetime(2018, 2, 3, 13, 25, 0, 0),
      datetime(2018, 3, 11, 7, 13, 0, 0),
      datetime(2018, 3, 18, 10, 10, 0, 0),
      datetime(2018, 3, 24, 7, 27, 0, 0),
      datetime(2018, 4, 8, 10, 10, 0, 0),
      datetime(2018, 2, 3, 14, 0, 0, 0),
      datetime(2018, 3, 11, 6, 25, 0, 0),
      datetime(2018, 3, 18, 11, 16, 0, 0),
      datetime(2018, 3, 24, 12, 25, 0, 0),
      datetime(2018, 4, 8, 10, 44, 0, 0)
     ]
Ca = [98.57,96.35,96.74,
      96.72,135.61,124.26,
      97.2,112.68,88.62,
      121.41,107.37,125.12,
      97.11,88.56,127.8,
      101.79,125.43,100.43,
      74.87,132.23,102.66,
      132.21]
K = [1.08,1.03,1.05,
     1.11,12.5,8.18,
     9.14,5.76,7.86,
     6.26,4.5,2.98,
     6.86,6.31,5.24,
     5.93,4.2,6.88,
     5.65,5.18,6.47,
     5.28]
Mg = [22.86,22.32,22.25,
      22.58,37.23,32.73,
      25.14,28.95,22.96,
      30.62,26.47,29.38,
      25.19,23.11,33.49,
      26.82,30.95,28.08,
      20.67,36.84,27.37,
      34.84]
Na  = [24.77,24.76,25.24,
        24.76,34.22,
        36.09,22.75,28.3, 
        28.36,26.87,
        24.61,25.2, 
        25.09,34.7,33.4,
        35.49,27.27,31.08,
        39.45,37.08,34.76,
        36.33]
rows = list(zip(Sites,DT,Ca,K,Mg,Na))
df = pd.DataFrame(rows,columns = ['Site','DateTime','Ca','K','Mg','Na'])
df_p = pd.DataFrame(rows,columns = ['Site [Token]','DateTime [Y-M-D-H-M-S]','Ca$^{2+}$ [ppm]','K$^{+}$ [ppm]','Mg$^{2+}$ [ppm]','Na$^{+}$ [ppm]'])
#ash leaching data
Site = ['Ash1','Ash2','Ash3',
        'Ash4','Ash5']
Ca = [30.98,17.57,21.62,
      19.78,24.17] 
K =  [15.97,13.75,22.14,
      173.20,88.51]
Mg = [14.88,9.29,12.12,
      10.59,20.27]
Na = [0.34,0.57,0.68,
      4.84,1.92]
rows = list(zip(Site,Ca,K,Mg,Na))
df2 = pd.DataFrame(rows,columns = ['Site','Ca','K','Mg','Na'])
df2_p = pd.DataFrame(rows,columns = ['Site [Token]','K$^{+}$ [ppm]','K$^{+}$ [ppm]','Mg$^{2+}$ [ppm]','Na$^{+}$ [ppm]'])
#normalized creek water concentrations 
DT2 = [datetime(2004, 10,4, 0, 0, 0, 0),
      datetime(2004, 11,4, 0, 0, 0, 0),
      datetime(2004, 12, 4,  0, 0, 0, 0),
      datetime(2005, 1, 5, 0, 0, 0, 0),
      datetime(2005, 2, 5, 0, 0, 0, 0),
      datetime(2005, 3, 5, 0, 0, 0, 0),
      datetime(2005, 4, 5, 0, 0, 0, 0),
      datetime(2005, 5, 5,  0, 0, 0, 0),
      datetime(2005, 6, 5,  0, 0, 0, 0),
      datetime(2005, 7, 5,  0, 0, 0, 0),
      datetime(2005, 8, 5,  0, 0, 0, 0)]
Ca2 = [56.12,89.12,75.63,71.30,
       87.44,74.83,85.12,101.62,
       95.12,100.98,107.63]
K2 = [1.60,1.30,1.52,1.13,
       1.13,1.06,1.07,1.05,
       .92,2.53,2.36]
Mg2 = [35.11,36.86,36.64,19.69,
       24.08,20.72,23.71,27.63,
       26.60,28.97,29.25]
Na2 = [40.23,33.14,33.59,15.58,
       18.72,15.53,18.09,22.02,
       19.60,24.15,25.29]
rows = list(zip(DT2,Ca2,K2,Mg2,Na2))
df3 = pd.DataFrame(rows,columns = ['DateTime','Ca','K','Mg','Na'])
df3_p = pd.DataFrame(rows,columns = ['DateTime [Y-M-D-H-M-S]','Ca$^{2+}$ [ppm]','K$^{+}$ [ppm]','Mg$^{2+}$ [ppm]','Na$^{+}$ [ppm]'])
#local precipitation from rattlesnake canyon
data = pd.read_csv('EL_Cap_Rain_Data.csv')
data['Reading'] = pd.to_datetime(data['Reading'])
data = data[['Reading','Value']]
data = data.set_index('Reading').resample('D').sum()
data = data['Value'].reset_index(drop=False)
data['Value'] = data['Value'].apply(lambda x: x*2.54)
data2 = pd.read_csv('RS_RAIN_DATA.csv')
data2['DATE'] = pd.to_datetime(data2['DATE'])
data2 = data2[(data2['HPCP'] < 900)]
data2 = data2[['HPCP','DATE']]
data2 = data2.set_index('DATE').resample('D').sum()
data2 = data2['HPCP'].reset_index(drop=False)
data2['HPCP'] = data2['HPCP'].apply(lambda x: x*2.54)
#Creek water measurements normalized by pre-storm values
DT3 = [datetime(2018, 1, 13, 0, 0, 0, 0), 
      datetime(2018, 1, 28, 0, 0, 0, 0), 
      datetime(2018, 2, 3,  0, 0, 0, 0), 
      datetime(2018, 2, 17, 0, 0, 0, 0), 
      datetime(2018, 3, 11, 0, 0, 0, 0), 
      datetime(2018, 3, 18, 0, 0, 0, 0), 
      datetime(2018, 3, 24, 0, 0, 0, 0), 
      datetime(2018, 4, 8,  0, 0, 0, 0)] 
Ca3 = [1.40,1.28,1.00,1.16,
       .91,1.25,1.11,1.29]
K3 = [11.71,7.66,8.56,5.40,
      7.36,5.86,4.22,2.79]
Mg3 = [1.65,1.45,1.12,1.29,
       1.02,1.36,1.18,1.31]
Na3 = [1.38,1.45,.91,1.14,
       1.14,1.08,.99,1.01]

rows = list(zip(DT3,Ca3,K3,Mg3,Na3))
df4 = pd.DataFrame(rows,columns = ['DateTime','Ca','K','Mg','Na']) 
