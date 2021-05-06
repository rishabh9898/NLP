import nltk
# nltk.download('movie_reviews')
import random
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews

stop_words = set(stopwords.words("English"))

documents = [(list(movie_reviews.words(fileid)), category)
               for category in movie_reviews.categories()
               for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words() :
    all_words.append(w.lower())
    # adds words in lowercase to our all words list

all_words = nltk.FreqDist(all_words)
#  retreives the frequency of the words

word_features = []
for i in all_words.most_common(3000):
    word_features.append(i[0])

# retrieve top 3000 words

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev),category) for (rev,category) in documents]



