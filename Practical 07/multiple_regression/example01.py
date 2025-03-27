import pandas
from sklearn import linear_model

df=pandas.read_csv("data.csv")

x=df[['Weight','Volume']]
y=df['CO2']

regr=linear_model.LinearRegression()
regr.fit(x,y)

predictedCO2=regr.predict(pandas.DataFrame([[3300,1300]],columns=['Weight','Volume']))

print(predictedCO2)
