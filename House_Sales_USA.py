# https://www.kaggle.com/harlfoxem/housesalesprediction/version/1 KAGGLE
        # 15 JAN 2022
        

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

hs_usa = pd.read_csv(r'C:/Users/doguy/Desktop/Dataset/usa_house_sales.csv')


hs_usa = hs_usa.drop(columns = ['id','view'])

############################################
hs_usa['date1'] = hs_usa['date'].astype(str)  
hs_usa.date1 = hs_usa.date1.str[0:4]
############################################

hs_usa = hs_usa.drop(columns = 'date')

#################################NAN VALUE##############################################
hs_usa.isnull().sum() #Number of rows where particular coumn value is any
hs_usa = hs_usa.dropna() #Drop all any values
########################################################################################



#########################################COUNTER OF PRICE###############################
plt.figure(figsize = (15  , 8))

# minimum = hs_usa.loc[hs_usa.price < 500000].count()[0]
# middle = hs_usa.loc[(hs_usa.price >= 500000) & (hs_usa.price <= 1000000)].count()[0]
# high = hs_usa.loc[hs_usa.price > 1000000].count()[0]

# labels = ['Minimum' , 'Middle' , 'High']
# explode = [0.1 , 0.1 , 0.1]
# weights = [minimum , middle, high]

# plt.title('Price')
# plt.pie(weights , labels = labels , autopct = '%.1f %%' , explode = explode )
########################################################################################


############################LINEAR MODEL#################################################
from sklearn import linear_model
from sklearn.model_selection import train_test_split

hs_usa = hs_usa.drop(columns = 'date1')

X = hs_usa.drop(columns = ['price', 'zipcode' , 'lat' ])
Y = hs_usa.price

X_training , x_test , Y_training , y_test = train_test_split(X , Y ,test_size = 0.2 , random_state = 2)
model = linear_model.LinearRegression()
model.fit(X_training , Y_training)
pred = model.predict(x_test)
plt.scatter(y_test , pred , marker = 'o' , cmap= ('summer') , alpha = 0.8 , linewidths = 1.2) 

########################################################################################

from sklearn.metrics import r2_score

print(r2_score(y_test , pred)) #0.6684179943228199

                    #Cross Validation
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
cv = ShuffleSplit(n_splits = 10, test_size = 0.2, random_state=2)
cross_val_score(LinearRegression(), X,Y, cv=cv )
# [0.66841799, 0.62966462, 0.65714009, 0.64421156, 0.66946455,
# 0.6451139 , 0.64343125, 0.62253963, 0.64208805, 0.66104214]

