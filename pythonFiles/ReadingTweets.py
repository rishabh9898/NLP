import csv
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import re, string

processed_word_list = []
tweets = []
with open('tweets.csv',encoding = 'utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        tweets.append(row['text'])
print(tweets)

temp = [len(element) for element in tweets]
len_strings = 0 if len(temp) == 0 else (float(sum(temp)) / len(temp))
print("The Average length of Sentence in list is : " + str(len_strings))

lemit = WordNetLemmatizer()
lemmatized = [[lemit.lemmatize(word) for word in word_tokenize(s)]
              for s in tweets]
  


# stop_words = set(stopwords.words("English"))

# filtered_words = list(filter(lambda word: word not in stopwords.words('english'), tweets))

# print(filtered_words)