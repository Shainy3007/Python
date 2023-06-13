#importing the library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#reading data
data = pd.read_csv(r"C:/Users/ACER/Desktop/New folder/xlsheet2.csv")

#complete data
data

#data of first 5 rows
data.head()

data.columns

#visualising NewPositiveCases vs Recovered using relplot
sns.relplot(x="NewPositiveCases",y="Recovered",data=data)

#visualising TotalPositiveCases vs Deaths using relplot
sns.relplot(x="TotalPositiveCases",y="Deaths",data=data)

#visualising TotalPositiveCases vs NewPositiveCases and introducing HUE through Recovered data using relplot
sns.relplot(x="TotalPositiveCases",y="NewPositiveCases",hue="Recovered",data=data)

#Creating a pairplot of the complete data
sns.pairplot(data)

#visualising a line graph of HospitalizedPatients vs HomeConfinement using relplot
sns.relplot(x="HospitalizedPatients",y="HomeConfinement",kind="line",data=data)

#visualising a line graph of Recovered vs HomeConfinement using relplot
sns.relplot(x="Recovered",y="HomeConfinement",kind="line",data=data)
