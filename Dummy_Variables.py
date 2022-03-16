# Dummy Variables: String halinde olan X değerleri numeric hale getirme yoludur. Pandas ile de kullanılabilir

#This project to learn what is dummy variables

import pandas as pd
from sklearn import linear_model

data = pd.read_csv(r'C:\Users\Asus\Desktop\Data\carprices.csv')


dummies = pd.get_dummies(data['Car Model']) #Burada Car Model Text'i için bir Dummy variables yarattık

data = data.drop("Car Model" , axis = 1) #Car Model'i sildik

Set = pd.concat([data , dummies] , axis = 'columns') #iki veriyi birleştirmeye yarar #Concantate


#Bu Dummy variables'leri yaptıktan sonra birini silebilirsin çünkü kafa karışıklığı yaratabiliyor.
final = Set.drop(["Mercedez Benz C class"] , axis = 1)


reg = linear_model.LinearRegression()

X = final.drop('Sell Price($)' , axis = 1)
y = final["Sell Price($)"]

reg.fit(X , y)
print("""
      00 = Mercedes 
      01 = BMW X5 
      10 = Audi A5""")
pred = reg.predict([[69500 , 7 , 0 , 1]]) #69500 MileAge , 7 Age , BMW X5 
print("Fiyat Aralığınız {}".format(pred))
score = reg.score(X , y) # %94 
print("Makinenin Başarı Oranı {}".format(score))