import tweepy
import csv
from textblob import TextBlob
import sys


####input your credentials here
consumer_key = 'VaXXwARLDXANLJNLaTluaBFOX'
consumer_secret = 'FoyEOfUT2tQTPdilZbMIamCl3283ScdJNZMHYIfGO7vdkNgFAs'
access_token = '970957284171026432-OBWSdlJBJi8yyvHA3qkUbCmQQnCSIy6'
access_token_secret = 'feUITreKvxnOu3yoLtYdxasEngJJv3MY3QukWBx2X81QT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

searchTerm=raw_input('Enter the search term:')
numSearch= int(input('Enter the no. of Tweets to be crawled : '))

#for training
# Open/Create a file to append data
csvFile = open('Training.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile,dialect='excel')

for tweet in tweepy.Cursor(api.search,q=searchTerm,lang="en").items(numSearch):
    a=TextBlob(tweet.text)
    b=a.sentiment.polarity
    if(b>0):
        c=['|positive|','|',tweet.text.encode('utf-8'),'|']
    elif(b<0):
        c=['|negative|','|',tweet.text.encode('utf-8'),'|']
    else:
        c=['|neutral|','|',tweet.text.encode('utf-8'),'|']
    
    if((not tweet.retweeted) and ('RT @' not in tweet.text)):
    	csvWriter.writerow(c)
	print (c)

numSearch1= numSearch*0.2

#For testing
#Open/Create a file to append data
csvFile = open('Testing.csv', 'w')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=searchTerm,count=140,
                           lang="en").items(numSearch1):
    
    if((not tweet.retweeted) and ('RT @' not in tweet.text)):
    	csvWriter.writerow([tweet.text.encode('utf-8')])
	print (tweet.text)

