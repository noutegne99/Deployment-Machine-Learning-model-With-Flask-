######### Some Important Libraries

#!pip install selenium
#!pip install dhash
#!pip install tldextract
#!pip install PIL
#!pip install bs4


#!pip3 install flask
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import metrics
import pickle


################################# SEUILLAGE DES SCORES TEXTE ET PERCEPTION ##############################################

PhishingLegitimeSHA3224SS=pd.read_csv('C:/Users/bkoua/Eprojet_/SHA3224/PhishingLegitimeSHA3224SS.csv')
df1 = PhishingLegitimeSHA3224SS
################################# SEUILLAGE DU TEXTE ET DE LA PERCEPTION ##############################################
for index in range(0,len(df1)): 
    #print (index)
    if( df1.iat[index,1] == 0 or df1.iat[index,1]>10 or df1.iat[index,1]<-10):
        df1.iat[index,1] = -1
    #print (df1 )
    else:
        df1.iat[index,1] = 1
for index in range(0,len(df1)): 
    #print (index)
    if( df1.iat[index,2] == 0 or df1.iat[index,2]>5 or df1.iat[index,2]<-5):
        df1.iat[index,2] = -1
    #print (df1 )
    else:
        df1.iat[index,2] = 1
        
        
dataset = df1        
################################ Splitting the dataset into the Training set and Test set ###########################
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
X4 = dataset.iloc[:, [1,2,3,4,5,6,7,9,10]].values
y = dataset.iloc[:, 11].values
X_train, X_test, y_train, y_test = train_test_split(X4, y, test_size = 0.25, random_state = 0)
# Fitting model with training data
classifier = SVC(kernel='linear', C=1, random_state=0).fit(X_train, y_train)#SVC(kernel = 'linear', random_state = 0)
# Save model to the disk
pickle.dump(classifier,open('model.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

#Predicting the Test set results
#y1_pred = classifier.predict([[-1,-1,1,1,1,1,-1,1,1]])
#y1_pred

