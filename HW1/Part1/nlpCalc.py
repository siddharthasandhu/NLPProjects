import sys


preList=[]
ansList=[]
univDict={}


def PFRScore(classifier):
    realCount=0
    matchCount=0
    for i in range(0,len(ansList)):
        if ansList[i]==classifier:
            realCount=realCount+1
            if preList[i]==classifier:
                matchCount=matchCount+1    
    recall=float(matchCount)/realCount
    print "Recall for "+ classifier + " is "+ str(recall)
    matchCount=0
    realCount=0
    for i in range(0,len(ansList)):
        if preList[i]==classifier:
            realCount=realCount+1
            if ansList[i]==classifier:
                matchCount=matchCount+1
    precision=float(matchCount)/realCount
    print "Precision for "+ classifier + " is "+ str(precision)
    FScore=2*((float(precision*recall))/(precision+recall))
    print "F-Score for "+ classifier + " is "+ str(FScore)
    

def formDictionaries(predFile,ansFile):
    answerFile=open(ansFile,'r')
    predFile=open(predFile,'r')
    for line in answerFile:
        array=line.split()
        ansList.append(array[0])
        if(univDict.has_key(array[0])==False):
            univDict[array[0]]=array[0]
    for line in predFile:
        array=line.split()
        preList.append(array[0])
    for key in univDict:
        PFRScore(univDict[key])    
    
if __name__=="__main__":
    formDictionaries(sys.argv[1],sys.argv[2])  