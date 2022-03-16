# -*- coding: utf-8 -*-

#Dictionary like a suit for DataFrame

import pandas as pd

web_stats = {'Day' : [1,2,3,4,5,6] , 'Visitors' : [56,65,45,34,65,76] , 'Bounce_Rate' : [76,56,54,56,34,23]}

df = pd.DataFrame(web_stats , index = list("ABCDEF"))
print(df)

#You can see the columns specifically

print(df["Day"])
#or
print(df.Day) 
#There is no difference.

#If you want to see multiple columns:
    
print(df[['Day' , 'Visitors']])

#You can use tolist() to see values of columns as a list:

print(df.Day.tolist()) #[1, 2, 3, 4, 5, 6]