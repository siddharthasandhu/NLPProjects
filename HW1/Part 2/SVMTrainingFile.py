import os
import collections

class ident:
    def __init__(self,counter,name):
        self.counter=counter
        self.name=name
        
        
def createTrainingFile():
    univDict={}
    counter=1
    trainingFile = open("trainingfile2.txt",'r')
    svmTraining=open("SVMTraing_file2.txt",'a')
    for line in trainingFile:
        array=line.split()
        for words in array:
            if univDict.has_key(str(words.rsplit())) == False:
                univDict[str(words.rsplit())] = str(counter)
                counter=counter+1
    trainingFile.close()
    trainingFile = open("trainingfile2.txt",'r')
    for line in trainingFile:
        dictLoc={}
        array=line.split()
        res=''
        if array[0]=="SPAM":
            res = "-1"
        elif array[0]=="HAM":
            res = "+1"
        for words in array:
            if univDict.has_key(str(words.rsplit())):
                if dictLoc.has_key(str(words.rsplit())):
                    dictLoc[str(words.rsplit())].counter=dictLoc[str(words.rsplit())].counter + 1
                else:
                    report=ident(1,univDict[str(words.rsplit())])
                    dictLoc[str(words.rsplit())]=report
        newDict={} 
        for key in dictLoc:
            if newDict.has_key(int(dictLoc[key].name))==False:
                newDict[int(dictLoc[key].name)]=str(dictLoc[key].counter)
        od= collections.OrderedDict(sorted(newDict.items()))
        for key,value in od.iteritems():
            res= res + " "+ str(key) + ":"+ str(value)
        svmTraining.write(res + "\n")
    svmTraining.close()
    trainingFile.close()
    

if __name__=="__main__":
    createTrainingFile()