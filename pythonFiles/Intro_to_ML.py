import nltk

from nltk.tokenize import sent_tokenize,word_tokenize

example_text="Hello Mr.Smith, how are you doing today? The weather is great."

stored_sentence = []
stored_sentence=sent_tokenize(example_text) 
# sentences are stored in stored_sentence list

word_stored = []
word_stored=word_tokenize(example_text)
# words are stored in word_stored list

# for i in word_stored:
    # print(i)


