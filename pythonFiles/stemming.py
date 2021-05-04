import nltk
from nltk.stem import PorterStemmer

from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["cloning", "clowning","riding", "ride","drawing","draw"]

for w in example_words:
    print(ps.stem(w))

