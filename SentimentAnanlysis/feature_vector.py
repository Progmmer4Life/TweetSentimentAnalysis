import re
import csv
import nltk
import os

class filterTweets:
    def __init__(self,filename = 'Training.csv'):
        self.featureList = []
        self.stopWords = []
        self.tweets = []
        self.filename = filename
        
    def replaceTwoOrMore(self,s):
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
        return pattern.sub(r"\1\1", s)

    def getStopWordList(self,stopWordListFile):
        stopWords = []
        stopWords.append('AT_USER')
        stopWords.append('URL')

        fp = open(stopWordListFile, 'r')
        line = fp.readline()
        while line:
            word = line.strip()
            stopWords.append(word)
            line = fp.readline()
        fp.close()
        return stopWords
    def getFeatureVector(self,tweet):
        featureVector = []
        stopWords = self.stopWords
        #split tweet into words
        words = tweet.split()
        for w in words:
            #replace two or more with two occurrences
            w = self.replaceTwoOrMore(w)
            #strip punctuation
            w = w.strip('\'"?,.')
            #check if the word stats with an alphabet
            val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            #ignore if it is a stop word
            if(w in stopWords or val is None):
                continue
            else:
                featureVector.append(w.lower())
        return featureVector


    
    def extract_features(self,tweet):
        tweet_words = set(tweet)
        features = {}
        for word in self.featureList:
            features['contains(%s)' % word] = (word in tweet_words)
        return features

    def getFeatureList(self):
        inpTweets = csv.reader(open(os.path.join('data','CSV',self.filename),'rb'),delimiter=',',quotechar='|')
        self.stopWords = self.getStopWordList('stopwords.txt')
        for row in inpTweets:
            category = row[0]
            tweet = row[1]
            featureVector = self.getFeatureVector(tweet)
            self.featureList.extend(featureVector)
            self.tweets.append((featureVector,category))

    def getSVMFeatures(self):
        self.getFeatureList()
        sortedFeatures = set(sorted(self.featureList))
        map = {}
        feature_vector = []
        labels = []
        for t in self.tweets:
            label = 0
            map = {}
            #Initialize empty map
            for w in sortedFeatures:
                map[w] = 0

            tweet_words = t[0]
            tweet_opinion = t[1]
            #Fill the map
            for word in tweet_words:
                #process the word (remove repetitions and punctuations)
                word = self.replaceTwoOrMore(word)
                word = word.strip('\'"?,.')
                #set map[word] to 1 if word exists
                if word in map:
                    map[word] = 1
            #end for loop
            values = map.values()
            feature_vector.append(values)
            if(tweet_opinion == 'positive'):
                label = 0
            elif(tweet_opinion == 'negative'):
                label = 1
            elif(tweet_opinion == 'neutral'):
                label = 2
            labels.append(label)
        #return the list of feature_vector and labels
        return {'feature_vector' : feature_vector, 'labels': labels}
        
    
    def getTrainingSet(self):
        self.getFeatureList()
        self.featureList = list(set(self.featureList))
        training_set = nltk.classify.util.apply_features(self.extract_features,self.tweets)
        return training_set

