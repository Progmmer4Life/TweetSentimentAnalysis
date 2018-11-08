from Tweet_class import *
import re
import csv
import pprint
import nltk.classify
import matplotlib.pyplot as plt

# Generate the training set
training_set = nltk.classify.util.apply_features(extract_features, tweets)
te=open('TestedSentiment.csv','w')
csWr=csv.writer(te,dialect='excel')

# Train the Naive Bayes classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
tTweet=[]
#testing by passing csv file
with open('Testing.csv','r')as File:
	reader=csv.reader(File,delimiter='\n')
	for testTweet in reader:
		#print(testTweet)
		processedTestTweet = processTweet(testTweet[0])
		sentiment = NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet, stopWords)))
                csWr.writerow([sentiment])
		print("testTweet = %s, sentiment = %s\n" % (testTweet, sentiment))
		tTweet.append((processedTestTweet, sentiment));
test_set = nltk.classify.apply_features(extract_features,tTweet)
te.close()
#classifier = nltk.NaiveBayesClassifier.train(training_set)
# Accuracy
accuracy = nltk.classify.accuracy(NBClassifier,training_set)

#Printing the accuracy
'''total = accuracy * 100
print('Naive Bayes Accuracy: %4.2f' % total)'''

#Printing the accuracy for the test set
accuracyTestSet = nltk.classify.accuracy(NBClassifier,test_set)
totalTest = accuracyTestSet * 100
print('\nNaive Bayes Accuracy with the Test Set: %4.2f' % totalTest)
