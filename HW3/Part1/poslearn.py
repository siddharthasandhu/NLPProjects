import nltk
from nltk.corpus import brown
from nltk.classify import maxent
import pickle

def pos_itfeatures(sentence):
    features=[]
    newSent = enumerate(sentence)
    for i,(word,key) in newSent:
        if word.lower().strip() == "its" :
            tag="its"
            if i == 0:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = "<START>"
                feature['ppTag']= "<START>"
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord']="<START>"
                feature['ppWord']="<START>"
                feature['nWord']= sentence[i+1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
            elif i == 1:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag']= "<START>"
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']="<START>" 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
            elif i==(len(sentence)-1):
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] =  sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = "<END>"
                feature['nnTag'] = "<END>"
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = "<END>"
                feature['nnWord']=  "<END>"
                features.append((feature,tag))
            elif i==(len(sentence)-2):
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] =  sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = "<END>"
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  "<END>"
                features.append((feature,tag))
            else:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
        elif word.lower().strip() == "it":
            if sentence[i+1][0] == "'s": 
                tag = "it's"
                print tag
                if i == 0:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = "<START>"
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = sentence[i + 3][1]
                    feature['pWord']="<START>"
                    feature['ppWord']="<START>"
                    feature['nWord']= sentence[i+2][0]
                    feature['nnWord']=  sentence[i + 3][0]
                    features.append((feature,tag))
                elif i == 1:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = sentence[i-1][1]
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = sentence[i + 3][1]
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']="<START>" 
                    feature['nWord'] = sentence[i + 2][0]
                    feature['nnWord']=  sentence[i + 3][0]
                    features.append((feature,tag))
                elif i==(len(sentence)-1):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = "<END>"
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = "<END>"
                    feature['nnWord']= "<END>"
                    features.append((feature,tag))
                elif i==(len(sentence)-2):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = "<END>"
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = "<END>"
                    feature['nnWord']=  "<END>"
                    features.append((feature,tag))
                else:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = sentence[i + 3][1]
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = sentence[i + 2][0]
                    feature['nnWord']=  sentence[i + 3][0]
                    features.append((feature,tag))
    return features

def pos_youfeatures(sentence):
    features=[]
    newSent = enumerate(sentence)
    for i,(word,key) in newSent:
        if word.lower().strip() == "your" :
            tag="your"
            if i == 0:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = "<START>"
                feature['ppTag']= "<START>"
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord']="<START>"
                feature['ppWord']="<START>"
                feature['nWord']= sentence[i+1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
            elif i == 1:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag']= "<START>"
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']="<START>" 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
            elif i==(len(sentence)-1):
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] =  sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = "<END>"
                feature['nnTag'] = "<END>"
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = "<END>"
                feature['nnWord']=  "<END>"
                features.append((feature,tag))
            elif i==(len(sentence)-2):
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] =  sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = "<END>"
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  "<END>"
                features.append((feature,tag))
            else:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
        elif word.lower().strip() == "you"  :
            if sentence[i+1][0] == "'re":
                tag = "you're"
                print tag
                if i == 0:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = "<START>"
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = sentence[i + 3][1]
                    feature['pWord']="<START>"
                    feature['ppWord']="<START>"
                    feature['nWord']= sentence[i+2][0]
                    feature['nnWord']=  sentence[i + 3][0]
                    features.append((feature,tag))
                elif i == 1:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = sentence[i-1][1]
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = sentence[i + 3][1]
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']="<START>" 
                    feature['nWord'] = sentence[i + 2][0]
                    feature['nnWord']=  sentence[i + 3][0]
                    features.append((feature,tag))
                elif i==(len(sentence)-1):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = "<END>"
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = "<END>"
                    feature['nnWord']=  "<END>"
                    features.append((feature,tag))
                elif i==(len(sentence)-2):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = "<END>"
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = "<END>"
                    feature['nnWord']=  "<END>"
                    features.append((feature,tag))
                else:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = sentence[i + 3][1]
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = sentence[i + 2][0]
                    feature['nnWord']=  sentence[i + 3][0]
                    features.append((feature,tag))
    return features

def pos_theirfeatures(sentence):
    features=[]
    newSent = enumerate(sentence)
    for i,(word,key) in newSent:
        if word.lower().strip() == "they":
            if sentence[i+1][0] == "'re":
                tag="they're"
                print tag
                if i == 0:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = "<START>"
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = sentence[i + 3][1]
                    feature['pWord']="<START>"
                    feature['ppWord']="<START>"
                    feature['nWord']= sentence[i+2][0]
                    feature['nnWord']=  sentence[i + 3][0]
                    features.append((feature,tag))
                elif i == 1:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = sentence[i-1][1]
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = sentence[i + 3][1]
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']="<START>" 
                    feature['nWord'] = sentence[i + 2][0]
                    feature['nnWord']=  sentence[i + 3][0]
                    features.append((feature,tag))
                elif i==(len(sentence)-1):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = "<END>"
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = "<END>"
                    feature['nnWord']=  "<END>"
                    features.append((feature,tag))
                elif i==(len(sentence)-2):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = "<END>"
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = "<END>"
                    feature['nnWord']=  "<END>"
                    features.append((feature,tag))
                else:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = sentence[i + 3][1]
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = sentence[i + 2][0]
                    feature['nnWord']=  sentence[i + 3][0]
                    features.append((feature,tag))
        elif word.lower().strip() == "their":
            tag = "their"
            if i == 0:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = "<START>"
                feature['ppTag']= "<START>"
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord']="<START>"
                feature['ppWord']="<START>"
                feature['nWord']= sentence[i+1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
            elif i == 1:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag']= "<START>"
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']="<START>" 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
            elif i==(len(sentence)-1):
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] =  sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = "<END>"
                feature['nnTag'] = "<END>"
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = "<END>"
                feature['nnWord']=  "<END>"
                features.append((feature,tag))
            elif i==(len(sentence)-2):
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] =  sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = "<END>"
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  "<END>"
                features.append((feature,tag))
            else:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
    return features

def pos_loosefeatures(sentence):
    features=[]
    newSent = enumerate(sentence)
    for i,(word,key) in newSent:
        if word.lower().strip() == "loose" :
            tag="loose"
            if i == 0:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = "<START>"
                feature['ppTag']= "<START>"
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord']="<START>"
                feature['ppWord']="<START>"
                feature['nWord']= sentence[i+1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
            elif i == 1:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag']= "<START>"
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']="<START>" 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
            elif i==(len(sentence)-1):
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] =  sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = "<END>"
                feature['nnTag'] = "<END>"
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = "<END>"
                feature['nnWord']=  "<END>"
                features.append((feature,tag))
            elif i==(len(sentence)-2):
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] =  sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = "<END>"
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  "<END>"
                features.append((feature,tag))
            else:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
        elif word.lower().strip() == "lose":
            tag = "lose"
            if i == 0:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = "<START>"
                feature['ppTag']= "<START>"
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord']="<START>"
                feature['ppWord']="<START>"
                feature['nWord']= sentence[i+1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
            elif i == 1:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag']= "<START>"
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']="<START>" 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
            elif i==(len(sentence)-1):
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] =  sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = "<END>"
                feature['nnTag'] = "<END>"
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = "<END>"
                feature['nnWord']=  "<END>"
                features.append((feature,tag))
            elif i==(len(sentence)-2):
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] =  sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = "<END>"
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  "<END>"
                features.append((feature,tag))
            else:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i + 1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append((feature,tag))
    return features

def pos_tofeatures(sentence):
    features=[]
    newSent = enumerate(sentence)
    if len(sentence) > 3 :
        for i,(word,key) in newSent:
            if word.lower().strip() == "to" :
                tag="to"
                if i == 0:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = "<START>"
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+1][1]
                    feature['nnTag'] = sentence[i + 2][1]
                    feature['pWord']="<START>"
                    feature['ppWord']="<START>"
                    feature['nWord']= sentence[i+1][0]
                    feature['nnWord']=  sentence[i + 2][0]
                    features.append((feature,tag))
                elif i == 1:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = sentence[i-1][1]
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+1][1]
                    feature['nnTag'] = sentence[i + 2][1]
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']="<START>" 
                    feature['nWord'] = sentence[i + 1][0]
                    feature['nnWord']=  sentence[i + 2][0]
                    features.append((feature,tag))
                elif i==(len(sentence)-1):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = "<END>"
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = "<END>"
                    feature['nnWord']=  "<END>"
                    features.append((feature,tag))
                elif i==(len(sentence)-2):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = sentence[i+1][1]
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = sentence[i +1][0]
                    feature['nnWord']=  "<END>"
                    features.append((feature,tag))
                else:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = sentence[i+1][1]
                    feature['nnTag'] = sentence[i + 2][1]
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = sentence[i + 1][0]
                    feature['nnWord']=  sentence[i + 2][0]
                    features.append((feature,tag))
            elif word.lower().strip() == "too":
                tag = "too"
                if i == 0:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = "<START>"
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+1][1]
                    feature['nnTag'] = sentence[i + 2][1]
                    feature['pWord']="<START>"
                    feature['ppWord']="<START>"
                    feature['nWord']= sentence[i+1][0]
                    feature['nnWord']=  sentence[i + 2][0]
                    features.append((feature,tag))
                elif i == 1:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = sentence[i-1][1]
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+1][1]
                    feature['nnTag'] = sentence[i + 2][1]
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']="<START>" 
                    feature['nWord'] = sentence[i + 1][0]
                    feature['nnWord']=  sentence[i + 2][0]
                    features.append((feature,tag))
                elif i==(len(sentence)-1):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = "<END>"
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = "<END>"
                    feature['nnWord']= "<END>"
                    features.append((feature,tag))
                elif i==(len(sentence)-2):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = sentence[i+1][1]
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = sentence[i + 1][0]
                    feature['nnWord']=  "<END>"
                    features.append((feature,tag))
                else:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = sentence[i+1][1]
                    feature['nnTag'] = sentence[i + 2][1]
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = sentence[i + 1][0]
                    feature['nnWord']=  sentence[i + 2][0]
                    features.append((feature,tag))
        return features

def createModel():
    global classifierit
    global classifierloose
    global classifieryou
    global classifierto
    global classifiertheir
    brownFile = open("AllText.some",'r')
    newLine = brownFile.readlines() 
    trainingitSet = []
    traininglooseSet = []
    trainingyouSet = []
    trainingtoSet = []
    trainingtheirSet= []
    for sent in newLine:
        text=nltk.word_tokenize(sent.lower())
        tagSent=nltk.pos_tag(text)
        try :       
            arrayOfitFeature = pos_itfeatures(tagSent)
            arrayOfyouFeature = pos_youfeatures(tagSent)
            arrayOftheirFeature = pos_theirfeatures(tagSent)
            arrayOflooseFeature = pos_loosefeatures(tagSent)
            arrayOftoFeature = pos_tofeatures(tagSent)
        except IndexError:
            print "huha"
            
        if arrayOfitFeature:
            trainingitSet.extend(arrayOfitFeature)
        if arrayOftheirFeature:
            trainingtheirSet.extend(arrayOftheirFeature)
        if arrayOflooseFeature:
            traininglooseSet.extend(arrayOflooseFeature)
        if arrayOftoFeature:
            trainingtoSet.extend(arrayOftoFeature)
        if arrayOfyouFeature:
            trainingyouSet.extend(arrayOfyouFeature)
        
    
    algorithm = nltk.classify.MaxentClassifier.ALGORITHMS[1]
    #encodingit = maxent.TypedMaxentFeatureEncoding.train(trainingitSet, count_cutoff=3, alwayson_features=True)
    classifierit = maxent.MaxentClassifier.train(trainingitSet, algorithm)
    f = open('classifierit.pickle', 'wb')
    pickle.dump(classifierit, f)
    f.close()
    #encodingloose = maxent.TypedMaxentFeatureEncoding.train(traininglooseSet, count_cutoff=3, alwayson_features=True)
    classifierloose = maxent.MaxentClassifier.train(traininglooseSet, algorithm)
    f = open('classifierloose.pickle', 'wb')
    pickle.dump(classifierloose, f)
    f.close()
    #encodingyou = maxent.TypedMaxentFeatureEncoding.train(trainingyouSet, count_cutoff=3, alwayson_features=True)
    classifieryou = maxent.MaxentClassifier.train(trainingyouSet, algorithm)
    f = open('classifieryou.pickle', 'wb')
    pickle.dump(classifieryou, f)
    f.close()
    #encodingto = maxent.TypedMaxentFeatureEncoding.train(trainingtoSet, count_cutoff=3, alwayson_features=True)
    classifierto = maxent.MaxentClassifier.train(trainingtoSet, algorithm)
    f = open('classifierto.pickle', 'wb')
    pickle.dump(classifierto, f)
    f.close()
    #encodingtheir = maxent.TypedMaxentFeatureEncoding.train(trainingtheirSet, count_cutoff=3, alwayson_features=True)
    classifiertheir = maxent.MaxentClassifier.train(trainingtheirSet, algorithm)
    f = open('classifiertheir.pickle', 'wb')
    pickle.dump(classifiertheir, f)
    f.close()      


if __name__=="__main__":
    createModel()

