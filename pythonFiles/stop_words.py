import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence="This is example showing stop word filttration."
stop_words = set(stopwords.words("English"))

# print(stop_words)

words = word_tokenize(example_sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
# print(filtered_sentence)

