import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better",pos="a"))
# "a" stands for adjective
print(lemmatizer.lemmatize("running",'v'))
print(lemmatizer.lemmatize("churning",'v'))
