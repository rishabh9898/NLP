import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import re, string
import preprocessor as p
import matplotlib.pyplot as plt

lemma_tweets = []
tweets = []
with open('tweets.csv',encoding = 'utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        tweets.append(row['text'])

temp = [len(element) for element in tweets]
len_strings = 0 if len(temp) == 0 else (float(sum(temp)) / len(temp))
print("The Average length of Sentence in list is : " + str(len_strings))

# lemit = WordNetLemmatizer()
# lemmatized = [[lemit.lemmatize(word) for word in word_tokenize(s)]
#               for s in tweets]
  
# lemma_tweets = lemmatized


for i in range(len(tweets)):

    tweets[i] = tweets[i].lower()

# ----------------------------------------------------------------------------------------------------
#  Removes all the emojis from the tweets
import emoji
def give_emoji_free_text(text):
    clean_text =emoji.get_emoji_regexp().sub("", text)
    return clean_text

for i in range(len(tweets)):
    tweets[i] = give_emoji_free_text(tweets[i])
# ----------------------------------------------------------------------------------------------------
# Removes all Https
def give_http_free_text(text):
    text = re.sub(r'http\S+', '', text)
    return text

for i in range(len(tweets)):
    tweets[i] = give_http_free_text(tweets[i])
# -----------------------------------------------------------------------------------------------------
#  Removes @ symbol in tweets 
def give_atrate_free_text(text):
    clean_without_attherate = re.sub('@', '', text)
    return clean_without_attherate

for i in range(len(tweets)):
    tweets[i] = give_atrate_free_text(tweets[i])
# -----------------------------------------------------------------------------------------------------
# Removing punctuations 
def give_punct_free_text(text):
    tokenizer = nltk.RegexpTokenizer(r"\w+") 
    no_punct = tokenizer.tokenize(text)
    return no_punct

for i in range(len(tweets)):
    tweets[i] = give_punct_free_text(tweets[i])


# ----------------------------------------------------------------------------------------------------
# Removing stopwords
stop_words = set(stopwords.words("English"))

def give_stop_free_text(text):
    filtered_sentence = [] 
    count = 0 
    for w in text: 
        if w not in stop_words:
            count+=1 
            filtered_sentence.append(w)
            return(filtered_sentence[count-1])

for i in range(len(tweets)):
    tweets[i] = give_stop_free_text(tweets[i])


# --------------------------------------------------------------------------------------------------
