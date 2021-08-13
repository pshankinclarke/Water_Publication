#Author : Parker Shankin-Clarke (email parkerwsc1@gmail.com)
#Last Date Modified : 12/08/21
#Description :
'''
This script : 
1.) applies a correction to C/N data based on standards (for more information see the supplement)
2.) finds the detection limit for C&N
3.) calculates error bars (for more information see the supplement)
'''
#General imports
import pandas as pd
from scipy import stats
import sys
def apply_correc(df,col,M0,M1,MT):
   '''
      apply standard correction to measurements 
   '''
   #number of samples in dataframe, number of samples between M0 and M1
   m = df.shape[0]
   #S0,and Sm are the intial and final standard ratios respectivly 
   S0 = M0 / MT 
   Sm = M1 / MT
   #Standard ratio for any sample n, n ~ [1,m]
   Sn = [S0]
   for n in range(1, m) :
      Sn.append(Sn[n-1] + (Sm - S0) / m)
   #Vn is the correction
   df['Vn'] = Sn
   #Un is the measured value 
   #Nn = Un / Sn
   df['corrected' + ' ' + col] = df[col] / df['Vn']
   return df[['Sample ID','mass','corrected' + ' ' + col]]
def find_min(df,col0,col1):
   '''
      find detection limit for carbon and nitrogen
   '''
   df['mass'] = pd.to_numeric(df['mass'], errors = 'coerce')
   df = df[df[col0] > .0000000001]
   df.dropna(inplace = True)  
   #multiply col1 and col2 togeather 
   #make into new column 
   df['composite'] = df[col0] * df[col1]
   df['composite'] = df['composite'].div(100)
   X = df['composite'].tolist() 
   minimum = min([i for i in X if i > .0000000001])
   ind = X.index(minimum)
   return minimum,ind
if __name__ == "__main__":
   #load csv in pandas dataframe
   CN_data = pd.read_csv("CN_Measurements_Original.csv") 
   print(CN_data)
   #standards :
   #<-- C1 :
   Check1_N = 9.388992
   Check1_C = 72.48412
   #<-- D9 :
   Check2_N = 10.11252
   Check2_C = 72.9741
   #<-- E2 :
   Check3_N = 8.550572
   Check3_C = 71.55618
   #<-- G2 :
   Check4_N = 9.035851
   Check4_C = 73.23338
   #dataframe sections that correspond to standards 
   #and the corresponding list of standards : 
   secs = [(0,20),(20,25),(25,50)]
   standsN = [(Check1_N,Check2_N),
              (Check2_N,Check3_N),
              (Check3_N,Check4_N)]
   standsC = [(Check1_C,Check2_C),
              (Check2_C,Check3_C),
              (Check3_C,Check4_C)]
   dfs = []
   for sec,stand in zip(secs,standsN) :
      df_slice = CN_data[sec[0] : sec[1]] 
      df = apply_correc(df = df_slice,
                        col = 'N',
                        M0 = stand[0],
                        M1 = stand[1],
                        MT = 10.36)
      dfs.append(df)
   N_corr = pd.concat(dfs).reset_index(drop=True)
   dfs = []
   for sec,stand in zip(secs,standsC) :
      df_slice = CN_data[sec[0] : sec[1]]
      df = apply_correc(df = df_slice,
                        col = 'C',
                        M0 = stand[0],
                        M1 = stand[1],
                        MT = 71.09)
      dfs.append(df)
   C_corr = pd.concat(dfs).reset_index(drop=True)
   C_corr.to_csv('C_corrections.csv')
   N_corr.to_csv('N_corrections.csv')  
   Cmin,Cin = find_min(df = C_corr,col0 = 'corrected C',col1 = 'mass')
   Nmin,Nin = find_min(df = N_corr,col0 = 'corrected N',col1 = 'mass')
   #slice CN_corr into required columns 
   #calculate error bars 
   C_error = stats.sem(a = C_corr['corrected C'].to_numpy(), axis = 0, ddof = 1, nan_policy='propagate')
   N_error = stats.sem(a = N_corr['corrected N'].to_numpy(), axis = 0, ddof = 1, nan_policy='propagate')
