from Tweet_class import *
from naive_bayes import *

import re
import csv
import pprint
import nltk.classify
import matplotlib.pyplot as plt



#piechar
positive=negative=neutral=0
total=0
#Senti=[]
with open('TestedSentiment.csv','r')as readTestSenti:
    readr=csv.reader(readTestSenti,delimiter='\n')
    for senti in readr:
        if(senti[0]=='positive'):
            positive+=1
        elif(senti[0]=='negative'):
            negative+=1
        else:
            neutral+=1
total=positive+negative+neutral

posper=(positive*100)/total
negper=(negative*100)/total
neuper=(neutral*100)/total


 
# Data to plot
labels = 'Positive', 'negative', 'neutral'
sizes = [posper,negper,neuper]
colors = ['yellowgreen', 'red', 'lightskyblue']
explode = (0.1, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
