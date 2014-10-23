import math
import sys

class dictOfWords:
    def __init__(self,unique):
        self.dict1={}
        self.count=0
        self.name=''
        self.totalWords=0
        self.uniqueWords=unique
    def checkAndAdd(self,word):
        if self.dict1.has_key(word)==False:
                self.dict1[word]=1
                self.totalWords=self.totalWords+1
        else:
                self.dict1[word]=self.dict1[word]+1
                self.totalWords=self.totalWords+1    
    def setValue(self,key):
        self.name=key
    def calculateProb(self,word):
        probability=math.log(float(float(self.dict1[word]+1)/float(self.totalWords+self.uniqueWords)))
        return probability
        

def calculateTotal(dict1):
    count=0
    for key in dict1:
        count=dict1[key]+count
    return count
    
def checkUnique(count):
    count=0
    for m in list:
        count=count+m.count
    return count
    
def writeFile(list1,IdenDict,NameofModelFile):
    dictFinal={}
    fileCreate=open(NameofModelFile,'a')
    m=calculateTotal(IdenDict)
    for x in list1:
        for key in x.dict1:
            if(dictFinal.has_key(key)==False):
                val=x.calculateProb(key)
                name=x.name
                totalWords=x.dict1[key]
                comparVal=math.log(float(float(IdenDict[x.name])/float(m)))
                uniqueWords=x.uniqueWords
                catTotal=x.totalWords
                finalString=name + " "+ key + " " + str(totalWords) +" "+ str(val)+ " "+ str(comparVal) +" " + str(catTotal)+ " " + str(uniqueWords)  
                fileCreate.write(finalString+ "\n")
    fileCreate.close()
    
def readFile(trainingFile,NameofModelFile):
    IdenDict={}
    simpleList = []
    unique=len(set(w.lower() for w in open(trainingFile).read().split()))
    filetoRead=open(trainingFile,'r')
    for line in filetoRead:
        arrayofwords=line.split()
        if IdenDict.has_key(arrayofwords[0])==False:
            IdenDict[arrayofwords[0]]=1
            x= dictOfWords(unique)
            x.setValue(arrayofwords[0])
            simpleList.append(x)
        else:
            IdenDict[arrayofwords[0]]=IdenDict[arrayofwords[0]]+1
    filetoRead.close()
    filetoRead=open(trainingFile,'r')
    for line in filetoRead:
        arrayofwords=line.split(' ')
        for y in simpleList:
            if y.name==arrayofwords[0]:
                for word in arrayofwords:
                        y.checkAndAdd(str(((word.rstrip()).lower())))
    writeFile(simpleList,IdenDict,NameofModelFile)
    
def main(NameOfTrainingFile,NameofModelFile):
    readFile(NameOfTrainingFile,NameofModelFile)
    
if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])
    