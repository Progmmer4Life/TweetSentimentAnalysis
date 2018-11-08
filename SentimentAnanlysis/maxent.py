import re
import csv
import pprint
import nltk.classify
import matplotlib.pyplot as plt
from Tweet_class import *
from naive_bayes import *




MaxEntClassifier = nltk.classify.maxent.MaxentClassifier.train(training_set, 'GIS', trace=3, \
                    encoding=None, labels=None, gaussian_prior_sigma=0, max_iter = 3)
testTweet = 'Congrats @ravikiranj, i heard you wrote a new tech post on sentiment analysis'
processedTestTweet = processTweet(testTweet)
print(MaxEntClassifier.classify(extract_features(getFeatureVector(processedTestTweet,stopWords))))


#print informative features
print(MaxEntClassifier.show_most_informative_features(10))
