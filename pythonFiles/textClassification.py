import nltk
# nltk.download('movie_reviews')
import random
from nltk.corpus import stopwords
from nltk.corpus import movie_reviews

stop_words = set(stopwords.words("English"))

documents = [(list(movie_reviews.words(fileid)), category)
               for category in movie_reviews.categories()
               for fileid in movie_reviews.fileids(category)]

# alternate way ( Same meaning of the above code)

# documents = []

# for category in movie_reviews.categories() :
#     for fileid in movie_reviews.fileids(category) :
#         documents.append(list(movie_reviews.words(fileid)),category)

random.shuffle(documents)

# print(documents[1])

all_words = []

for w in movie_reviews.words() :
    all_words.append(w.lower())
    # adds words in lowercase to our all words list

all_words = nltk.FreqDist(all_words)

# gets the frequency of words

# print(all_words.most_common(15))
#  retreives the 15 most common words 

all_not_stop_words = []
for wi in all_words:
    if wi not in stop_words:
        all_not_stop_words.append(w.lower())

all_not_stop_words = nltk.FreqDist(all_not_stop_words)

print(all_not_stop_words.most_common(15))

#  retrieves the most common words that are not stop words

