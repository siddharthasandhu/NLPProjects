import math
import sys


class resSet:
    def __init__(self,probab,resultName):
        self.prob=float(probab)
        self.name=resultName


class dictItem:
    def __init__(self,key,Occur,Prob,AntiProb,unique,totalWords):
        self.key=key
        self.Occur=Occur
        self.Prob=Prob
        self.AnProb=AntiProb
        self.totalWords=totalWords
        self.unique=unique


class dictOfWords:
    def __init__(self):
        self.dict1={}
        self.name=''
    def checkAndAdd(self,word,item):
        self.dict1[word]=item   
    def setValue(self,key):
        self.name=key


def checkVal(listOfres):
    result=listOfres[0].prob
    name=listOfres[0].name
    for val in listOfres:
        value=float(val.prob)
        if result<value:
            result=value
            name=val.name
    return name

def getProbMess(dict1,line):
    countProb=0
    mega=float(dict1.dict1[dict1.dict1.keys()[0]].unique + dict1.dict1[dict1.dict1.keys()[0]].totalWords)
    valueList=dict1.dict1[dict1.dict1.keys()[0]].AnProb
    array=line.split()
    for words in array:
        if (dict1.dict1.has_key((words.rstrip()).lower())==True):
            countProb=float(countProb)+float(dict1.dict1[(words.rstrip()).lower()].Prob)
            valueList=dict1.dict1[words.rstrip().lower()].AnProb
        else:
            countProb=countProb+math.log(1/mega)         
    result=float(countProb)+float(valueList)
    return float(result)

def resultSet(line,simpleList):
    listOfres=[]
    for v in simpleList:
        res=float(getProbMess(v,line))
        result=resSet(res,v.name)
        listOfres.append(result)
    finRes=checkVal(listOfres)
    return finRes
        
def classifyFiler(simpleList,fileToRead):
    filetoRead=open(fileToRead,'r')
    filetoWrite=open("predAnswer.nb",'a')
    for line in filetoRead:
        stringElem=resultSet(line,simpleList)
        filetoWrite.write(stringElem+'\n')
    filetoRead.close()
    filetoWrite.close()
            

def readFile(classifyFile,NewFileToRead):
    IdenDict={}
    NewFile=NewFileToRead
    simpleList = []
    filetoRead=open(classifyFile,'r')
    for line in filetoRead:
        arrayofwords=line.split()
        if len(arrayofwords)==7:
            if IdenDict.has_key(arrayofwords[0].rstrip())==False:
                IdenDict[arrayofwords[0].rstrip()]=arrayofwords[0].rstrip()
                x= dictOfWords()
                x.setValue(arrayofwords[0].rstrip())
                simpleList.append(x)
                newEntry=dictItem(arrayofwords[1].rstrip(),arrayofwords[2].rstrip(),arrayofwords[3].rstrip(),arrayofwords[4].rstrip(),arrayofwords[6].rstrip(),arrayofwords[5].rstrip())
                x.checkAndAdd(arrayofwords[1],newEntry)           
            else:
                for val in simpleList:
                    if val.name==arrayofwords[0].rstrip():
                        newEntry=dictItem(arrayofwords[1].rstrip(),arrayofwords[2].rstrip(),arrayofwords[3].rstrip(),arrayofwords[4].rstrip(),arrayofwords[6].rstrip(),arrayofwords[5].rstrip())
                        val.checkAndAdd(arrayofwords[1].rstrip(),newEntry)
    filetoRead.close()
    classifyFiler(simpleList,NewFile)
    
def main(NameOfTrainingFile,fileToRead):
    readFile(NameOfTrainingFile,fileToRead)
    
if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])
    