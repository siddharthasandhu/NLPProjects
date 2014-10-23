import nltk
from nltk.corpus import brown
from nltk.classify import maxent
import pickle

def file_itfeatures(sentence):
    features=[]
    newSent = enumerate(sentence)
    for i,(word,key) in newSent:
        if word.lower() == "its" :
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
            else:
                feature={}
                feature['cTag']= sentence[i][1]
                feature['pTag'] = sentence[i-1][1]
                feature['ppTag'] =  sentence[i-2][1]
                feature['nTag'] = sentence[i+1][1]
                feature['nnTag'] = sentence[i + 2][1]
                feature['pWord'] = sentence[i-1][0]
                feature['ppWord']=sentence[i-2][0] 
                feature['nWord'] = sentence[i +1][0]
                feature['nnWord']=  sentence[i + 2][0]
                features.append(feature)
        elif word.lower() == "it":
            if sentence[i+1][0]=="'s":
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
                    features.append(feature)
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
                    features.append(feature)
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
                    features.append(feature)
                elif i==(len(sentence)-2):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = sentence[i + 2][0]
                    feature['nnWord']=  "<END>"
                    features.append(feature)
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
                    features.append(feature)
    return features

def file_youfeatures(sentence):
    features=[]
    newSent = enumerate(sentence)
    if len(sentence)>29: 
        print sentence[23]
        print sentence[29]
    for i,(word,key) in newSent:
        if word.lower() == "your":
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
        elif word.lower() == "you":
            if sentence[i+1][0]=="'re":
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
                    features.append(feature)
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
                    features.append(feature)
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
                    features.append(feature)
                elif i==(len(sentence)-2):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = sentence[i + 2][0]
                    feature['nnWord']=  "<END>"
                    features.append(feature)
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
                    features.append(feature)
    return features

def file_theirfeatures(sentence):
    features=[]
    newSent = enumerate(sentence)
    for i,(word,key) in newSent:
        if word.lower() == "they" :
            if sentence[i+1][0]=="'re":
                if i == 0:
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] = "<START>"
                    feature['ppTag']= "<START>"
                    feature['nTag'] = sentence[i+1][1]
                    feature['nnTag'] = sentence[i + 2][1]
                    feature['pWord']="<START>"
                    feature['ppWord']="<START>"
                    feature['nWord']= sentence[i+2][0]
                    feature['nnWord']=  sentence[i + 3][0]
                    features.append(feature)
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
                    features.append(feature)
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
                    features.append(feature)
                elif i==(len(sentence)-2):
                    feature={}
                    feature['cTag']= sentence[i][1]
                    feature['pTag'] =  sentence[i-1][1]
                    feature['ppTag'] =  sentence[i-2][1]
                    feature['nTag'] = sentence[i+2][1]
                    feature['nnTag'] = "<END>"
                    feature['pWord'] = sentence[i-1][0]
                    feature['ppWord']=sentence[i-2][0] 
                    feature['nWord'] = sentence[i + 2][0]
                    feature['nnWord']=  "<END>"
                    features.append(feature)
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
                    features.append(feature)
        elif word.lower() == "their":
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
    return features

def file_loosefeatures(sentence):
    features=[]
    newSent = enumerate(sentence)
    for i,(word,key) in newSent:
        if word.lower() == "loose" :
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
        elif word.lower() == "lose":
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
    return features

def file_tofeatures(sentence):
    features=[]
    newSent = enumerate(sentence)
    for i,(word,key) in newSent:
        if word.lower() == "to" :
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
        elif word.lower() == "too":
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
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
                features.append(feature)
    return features

def refineFile(line):
    writeFile=open("Solution",'w')
    testitSet = []
    testlooseSet = []
    testyouSet = []
    testtoSet = []
    testtheirSet= []
    for l in line:
        finalLine=l
        if l!="\n":
            print l
            text=nltk.word_tokenize(l.lower())
            arrayLine=nltk.pos_tag(text) 
            print arrayLine
            try :
                arrayOfitFeature = file_itfeatures(arrayLine)
                arrayOfyouFeature = file_youfeatures(arrayLine)
                arrayOftheirFeature = file_theirfeatures(arrayLine)
                arrayOflooseFeature = file_loosefeatures(arrayLine)
                arrayOftoFeature = file_tofeatures(arrayLine)
            except IndexError:
                print "huha"
                
            testitSet.extend(arrayOfitFeature)
            testtheirSet.extend(arrayOftheirFeature)
            testlooseSet.extend(arrayOflooseFeature)
            testtoSet.extend(arrayOftoFeature)
            testyouSet.extend(arrayOfyouFeature)
            newLine= l.split()
            if arrayOfitFeature:
                count = 0
                print arrayOfitFeature
                repArray=classifierit.batch_classify(arrayOfitFeature)
                for index,val in enumerate(newLine):
                    if newLine[index] == "it's" or newLine[index] == "its":
                        newLine[index] = repArray[count]
                        count = count + 1 
                    elif newLine[index] == "It's" or newLine[index] == "Its":
                        if  repArray[count] == "it's":
                            newLine[index] = "It's"
                        elif repArray[count] == "its":
                            newLine[index] = "Its"
                        count = count + 1     
            if arrayOfyouFeature:
                count=0
                print arrayOfyouFeature
                repArray = classifieryou.batch_classify(arrayOfyouFeature)
                print repArray
                for index,val in enumerate(newLine):
                    if newLine[index] == "your" or newLine[index] == "you're":
                        print index,count
                        newLine[index] = repArray[count]
                        count = count + 1 
                    elif newLine[index] == "Your" or newLine[index] == "You're":
                        if repArray[count] == "your":
                            newLine[index]="Your"
                            count = count + 1
                        elif repArray[count] == "your're":
                            newLine[index]= "You're"
                            count = count + 1 
            if arrayOftheirFeature:
                count=0
                print arrayOftheirFeature
                repArray = classifiertheir.batch_classify(arrayOftheirFeature)
                for index,val in enumerate(newLine):
                    if newLine[index] == "their" or newLine[index] == "they're":
                        newLine[index] = repArray[count]
                        count = count + 1 
                    elif newLine[index] == "Their" or newLine[index] == "They're":
                        if repArray[count] == "their":
                            newLine[index] = "Their"
                        elif repArray[count] == "they're" :
                            newLine[count]= "They're"
                        count = count + 1 
            if arrayOflooseFeature:
                count=0
                print arrayOflooseFeature
                repArray = classifierloose.batch_classify(arrayOflooseFeature)
                for index,val in enumerate(newLine):
                    if newLine[index] == "loose" or newLine[index] == "lose":
                        newLine[index] = repArray[count]
                        count = count + 1 
                    elif newLine[index] == "Loose" or newLine[index] == "Lose":
                        if repArray[count] == "loose":
                            newLine[index] = "Loose"
                        elif repArray[count] == "lose":
                            newLine[index] = "Lose"
                        count = count + 1 
            if arrayOftoFeature:
                count=0
                print arrayOftoFeature
                repArray = classifierto.batch_classify(arrayOftoFeature)
                for index,value in enumerate(newLine):
                    if newLine[index] == "to" or newLine[index] == "too":
                        newLine[index] = repArray[count]
                        count = count + 1 
                    elif newLine[index] == "To" or newLine[index] == "Too":
                        if repArray[count] == "to":
                            newLine[index] = "To"
                        elif repArray[count] == "too":
                            newLine[index] = "Too"
                        count = count + 1
            finalLine = " ".join(newLine) + "\n"
            print finalLine
        writeFile.write(finalLine)
                 
            
def readFile():
    readFile=open('hw3.dev.err.txt','r')
    newLine=readFile.readlines()
    readFile.close()
    refineFile(newLine)

  
if __name__=="__main__":
    global classifierit
    global classifierloose
    global classifieryou
    global classifierto
    global classifiertheir
    f= open('classifierit.pickle')
    classifierit = pickle.load(f)
    f.close()
    f= open('classifierloose.pickle')
    classifierloose = pickle.load(f)
    f.close()
    f= open('classifieryou.pickle')
    classifieryou = pickle.load(f)
    f.close()
    f= open('classifierto.pickle')
    classifierto = pickle.load(f)
    f.close()
    f= open('classifiertheir.pickle')
    classifiertheir = pickle.load(f)
    f.close()
    readFile()