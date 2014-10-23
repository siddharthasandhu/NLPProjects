import nltk
from nltk.corpus import brown
from nltk.corpus import reuters
from nltk.classify import maxent
from nltk.tag.stanford import POSTagger
import pickle
'''
brownFile = open("brown.some",'w')
reuterFile=open("reuter.some",'w')

count = 0
for sent in brown.sents():
    for m in sent:
        word=m.lower()
        if count == 1:
            break
        elif word == "to" or word == "too" or word == "their" or word == "they're" or word == "loose" or word =="lose" or word == "its" or word == "it's" or word == "your" or word == "you're":
            count = 1
    if count == 1:
        print " ".join(sent) 
        brownFile.write(" ".join(sent) + "\n")
        count=0
        
for sent in reuters.sents():
    for m in sent:
        word=m.lower()
        if count == 1:
            break
        elif word == "to" or word == "too" or word == "their" or word == "they're" or word == "loose" or word =="lose" or word == "its" or word == "it's" or word == "your" or word == "you're":
            count = 1
    if count == 1:
        print " ".join(sent) 
        reuterFile.write(" ".join(sent) + "\n")
        count=0
reuter.close()        
brownFile.close()        
'''
brownFile = open("brown.some",'r')
newLine = brownFile.readlines() 
tagArray = []
for line in newLine :
    tagArray.extend(line.split())  
st = POSTagger('/home/siddhartha/Downloads/stanford-postagger-full-2014-01-04/models/english-bidirectional-distsim.tagger', '/home/siddhartha/Downloads/stanford-postagger-full-2014-01-04/stanford-postagger.jar')
tagSent = st.tag(tagArray)
f = open('brownTagger.pickle', 'wb')
pickle.dump(tagSent, f)
f.close()
#print tagSent




