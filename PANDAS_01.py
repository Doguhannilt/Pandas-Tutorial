# -*- coding: utf-8 -*-

import pandas as pd 


#Istanbul 
data_set = pd.read_csv(r'C:\Users\Asus\Desktop\DATA\traffic_density_202001.csv')
print(data_set.head())

##Read Headers
print(data_set.columns)

##Read each Column
print(data_set['AVERAGE_SPEED']) , print(data_set.NUMBER_OF_VEHICLES)

#Read each Row 
print(data_set.iloc[1])

##Read a specific location (R , C)
print(data_set.iloc[1,0])

##Read a special values of column
print(data_set.loc[data_set['AVERAGE_SPEED'] == 27])

##Set a total column
data_set['Total'] = data_set['MAXIMUM_SPEED'] + data_set['MINIMUM_SPEED'] / 2

#I creating column that named Total and that colums including max.speed + min.speede
print(data_set.head())
print(data_set.iloc[0].MAXIMUM_SPEED + data_set.iloc[0].MINIMUM_SPEED) #Check.

#Drop specific column
data_set = data_set.drop(['Total'] , axis = 1) 
print(data_set)

#Saving our DATA 
data_set.to_csv('modified.csv' , index = False) #Destroy index

#Filtering DATA

new_data_set = data_set.loc[ (data_set['NUMBER_OF_VEHICLES'] == 50) & (data_set['AVERAGE_SPEED'] == 35) & (data_set['MAXIMUM_SPEED'] > 70) ]
new_data_set.to_csv('New Specific Data.csv' , index = False)





