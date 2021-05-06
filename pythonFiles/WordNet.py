import nltk
from nltk.corpus import wordnet

# syns = synonyms set

# getting the synonyms of a particular word
syns=[]
syns_1=[]
syns = wordnet.synsets("program")
syns_1 = wordnet.synsets("greetings")

# synset
print(syns[0])
# getting the first synonym element
print(syns[0].lemmas())
# getting the lemmas of the first word
print(syns[0].lemmas()[0].name())
# getting the first lemma of the first word in the list
print(syns[0].definition())
# getting the definition of the first synset
print(syns[0].examples())
# examples based on the first synonym in the list

# antonyms stand for opposite words

synonyms =[]
antonyms = []

for syn in wordnet.synsets("good") :
    for le in syn.lemmas() :
        # le - lemmas
        synonyms.append(le.name())
        if le.antonyms() :
            antonyms.append(le.antonyms()[0].name())


print(set(synonyms))
print(set(antonyms))


word_1 = wordnet.synset("ship.n.01")
#  ship, noun, first noun
word_2 = wordnet.synset("boat.n.01")
#  boat.noun.firstnoun

print(word_1.wup_similarity(word_2))
# comparing similiarity of word_1 with word2 and gives a percentage







