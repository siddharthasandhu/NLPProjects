import sys


preList=[]
ansList=[]
univDict={}


def PFRScore():
    classifier=0
    realCount=0
    matchCount=0
    for i in range(0,len(ansList)):
        if float(ansList[i]) > float(classifier):
            realCount=realCount+1
            if float(preList[i])>float(classifier):
                matchCount=matchCount+1    
    recall=float(matchCount)/realCount
    print "Recall for is "+ str(recall)
    matchCount=0
    realCount=0
    for i in range(0,len(ansList)):
        if float(preList[i])>0:
            realCount=realCount+1
            if float(ansList[i])>0:
                matchCount=matchCount+1
    precision=float(matchCount)/realCount
    print "Precision for  is "+ str(precision)
    FScore=2*((float(precision*recall))/(precision+recall))
    print "F-Score for  is "+ str(FScore)
    

def formDictionaries(predFile,ansFile):
    answerFile=open(ansFile,'r')
    predFile=open(predFile,'r')
    for line in answerFile:
        array=line.split()
        ansList.append(array[0])
    for line in predFile:
        array=line.split()
        preList.append(array[0])
    PFRScore()    
    
if __name__=="__main__":
    formDictionaries(sys.argv[1],sys.argv[2])  
