# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 20:13:50 2015

@author: Michael
"""

import pandas


df = pandas.read_csv("titanic3.csv")

#new column with value of 1
df['Count'] = 1

#drop unnecessary columns
df.pop('name')
df.pop('fare')
df.pop('cabin')
df.pop('ticket')
df.pop('sibsp')
df.pop('parch')
df.pop('boat')
df.pop('body')
df.pop('home.dest')


#categorise Age Column for more overview
df.loc[(df.age >= 0) & (df.age <=14), 'Age'] = 'Age <14'
#df.age[df.age<=14] = '<14'
df.loc[(df.age > 14) & (df.age <=30), 'Age'] = 'Age 14-30'
#df.age[(df.age > 14) & (df.age <=30)] = '14-30'

df.loc[(df.age > 30) & (df.age <=50), 'Age'] = 'Age 31-50'
#df.age[(df.age > 30) & (df.age <=50)] = '31-50'

df.loc[(df.age > 50) & (df.age <=80), 'Age'] = 'Age >51'
#df.age[(df.age > 50) & (df.age <=80)] = '>51'
df.age.fillna('NA', inplace=True)
df.loc[(df.age == 'NA'), 'Age'] = 'NA'


#Categorise Survived Column
df.loc[(df.survived == 0), 'Status'] = 'Perished'
df.loc[(df.survived == 1), 'Status'] = 'Survived'


#Categoriese Passenger Class
df.loc[(df.pclass == 1), 'Passenger Class'] = 'Class 1'
df.loc[(df.pclass == 2), 'Passenger Class'] = 'Class 2'
df.loc[(df.pclass == 3), 'Passenger Class'] = 'Class 3'

#Rename Sex, Female, Male
df.loc[(df.sex == 'male'), 'Sex'] = 'Male'
df.loc[(df.sex == 'female'), 'Sex'] = 'Female'

#Rename Embarked
df.loc[(df.embarked == 'C'), 'Embarked'] = 'Cherbourg'
df.loc[(df.embarked == 'Q'), 'Embarked'] = 'Queenstown'
df.loc[(df.embarked == 'S'), 'Embarked'] = 'Southampton'

df.embarked.fillna('Embarked NA', inplace=True)
df.loc[(df.embarked == 'Embarked NA'), 'Embarked'] = 'Embarked NA'

#drop old variables
df.pop('age')
df.pop('survived')
df.pop('embarked')
df.pop('sex')
df.pop('pclass')



print df.head()


df.to_csv('titanic1.csv', index=False)

#Without Age = 'NA' and Embarked = 'Embarked NA'
#1044 Values
df1 = df.loc[df.Age != 'NA']

#Without Embarked = 'Embarked NA'
#1307 Values
df2 = df.loc[df.Embarked != 'Embarked NA']

df1.to_csv('titanic_without_age.csv', index=False)

df2.to_csv('titanic_without_embarked.csv', index=False)