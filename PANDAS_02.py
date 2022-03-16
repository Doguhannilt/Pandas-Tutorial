# -*- coding: utf-8 -*-

import pandas as pd

data_set = pd.read_csv(r'C:\Users\Asus\Desktop\PANDAS\park_location.csv')

#Filtering as string value
new_data_set =data_set.loc[~data_set['COUNTY_NAME'].str.contains('ZEYTİNBURNU')]

# print(new_data_set.head(10))

#☻if you put ~ (alt - 126) that means drop every values that you choosing. 

#https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.groupby.htm
#Groupby
print(new_data_set.groupby(['NEIGHBORHOOD_NAME']).mean()) #28.854939  41.065105
print(new_data_set.groupby(['NEIGHBORHOOD_NAME']).sum()) #115.419758  164.260420

#Renaming Columns in a Pandas DataFrame
new_data_set = new_data_set.rename(columns = ({'NEIGHBORHOOD_NAME' : 'Komşu İlçeler' , 'COUNTY_NAME' : 'İlçeler'}) , inplace=False)
print(new_data_set.head())

#How to fill missing values:
    
new_data_set['NAME'].fillna("0") 
#MyDataFrame.fiilna(fiil-value)

print(new_data_set)