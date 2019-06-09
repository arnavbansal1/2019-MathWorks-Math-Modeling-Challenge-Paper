import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from collections import Counter
from math import log, inf
import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.multiclass import OneVsRestClassifier
import pickle

data = pd.read_csv("tedsa_2016_puf.csv")
data = data[
   ["AGE", "ARRESTS", "EDUC", "EMPLOY", "ETHNIC", "SEX", "LIVARAG", "MARSTAT", "PRIMINC", "PSYPROB", "RACE", "SUB1"]] # demographic categories
classifier = DecisionTreeClassifier()
for i in range(0,len(data)):
   if(i%10000==0):
       print(i)
   if(data.iloc[i,-1]==6):
       data.iloc[i,-1] = 7
templist = []
for i in range(0,len(data)):
   if(data.iloc[i,-1]!=2 and data.iloc[i,-1]!=4 and data.iloc[i,-1]!=7 and data.iloc[i,-1]!=12):
       templist.append(i)
data = data.drop(templist)
X = data.iloc[:, :-1] # columns of independent variables
y = data.iloc[:, -1] # column of dependent variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
pickle.dump(classifier, open('tree.pk','wb'))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print('Accuracy: '+str(accuracy_score( y_test,y_pred)))
tempdata = pd.read_csv("300test1.csv") # reads csv file into pandas library
print(tempdata)
templist = []
classifier = pickle.load(open('tree.pk', 'rb'))
for i in range(0,len(tempdata)):
   templist.append(classifier.predict_proba([tempdata.iloc[i,:]]))
counter = 0
counter_alcohol = 0
counter_marijuana = 0
counter_opioids = 0
counter_nicotine = 0
maxvalue = -1
maxindex = -1
for arr in templist:
   for i in range(0, len(arr)):
       if(arr[i]>maxvalue):
           maxvalue = arr[i]
           maxindex = i
       if(arr[i]==1.0):
           counter+=1
   if maxindex==0:
      counter_alcohol+=1
   if maxindex==1:
       counter_marijuana+=1
   if maxindex==2:
       counter_opioids+=1
   if maxindex==3:
       counter_nicotine+=1
   maxvalue = -1
   maxindex = -1
print("Number of total drug high school senior users: "+str(counter))
print("Number of nicotine high school senior users: " +str(counter_nicotine))
print("Number of marijuana high school senior users: " +str(counter_marijuana))
print("Number of alcohol high school senior users: " +str(counter_alcohol))
print("Number of unprescribed high school senior opioid users: " +str(counter_opioids))
