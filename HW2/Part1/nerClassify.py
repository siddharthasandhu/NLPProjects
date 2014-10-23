import subprocess
from cStringIO import StringIO 
import os
import sys

class wordThread:
    def __init__(self,wording,prevWord,prevPrevWord,nextWord,nextNextWord):
        self.mainWord="mainWord:"+str(self.wordBreak(wording))
        self.someWord=str(self.wordBreak(wording))
        self.prevWord="prevWord:"+str(self.wordBreak(prevWord))
        self.tagPrevWord="tagPrevWord:"+str(self.tagBreak(prevWord))
        self.prevPrevWord="prevPrevWord:"+str(self.wordBreak(prevPrevWord))
        self.tagPrevPrevWord="tagPrevPrevWord:"+str(self.tagBreak(prevPrevWord))
        self.nextWord="nextWord:"+str(self.wordBreak(nextWord))
        self.tagNextWord="tagNextWord:"+str(self.tagBreak(nextWord))
        self.nextNextWord="nextNextWord:"+str(self.wordBreak(nextNextWord))
        self.tagNextNextWord="tagNextNextWord:"+str(self.tagBreak(nextNextWord))
        self.firstThree="firtThree:"+str(self.firstThree(self.someWord))
        self.lastThree="lastThree:"+str(self.lastThree(self.someWord))
        self.finalSentence=str(self.mainWord+" "+self.firstThree + " " + self.lastThree + " " + self.nextWord + " " + self.tagNextWord + " " + self.nextNextWord +" " + self.tagNextNextWord + " " +self.prevWord +  " " + self.tagPrevWord + " " + self.prevPrevWord + " " + self.tagPrevPrevWord + "\n")
    def wordBreak(self,word):
        if word!='':
            newWord=word.rsplit('/',2)
            return newWord[0].lower()
        else:
            return ''
    def tagBreak(self,word):
        if word!=" ":
            newWord=word.rsplit("/",2)
            return newWord[len(newWord)-1]
        else:
            return ''
    def firstThree(self,word):
        if len(word)>=3:
            return str(word[0]+word[1]+word[2])
        else:
            return word
    def lastThree(self,word):
        if len(word)>=3:
            return str(word[len(word)-3]+word[len(word)-2]+word[len(word)-1])
        else:
            return word
        
def readText(line):
    inputFile=open("input.file",'w')
    arrayWords = line.split()
    for i, v in enumerate(arrayWords):
        if len(arrayWords)>2:
            if i < len (arrayWords)-2 and i >1:
                const=i
                newWord=wordThread(v,arrayWords[const-1],arrayWords[const-2],arrayWords[const+1],arrayWords[const+2])
            elif i == len(arrayWords) - 2 :
                const=i
                newWord=wordThread(v,arrayWords[const-1],arrayWords[const-2],arrayWords[const+1]," ") 
            elif i == len(arrayWords)- 1 :
                const=i
                newWord=wordThread(v,arrayWords[const-1],arrayWords[const-2]," "," ")
            elif i == 1 :
                const=i
                newWord=wordThread(v,arrayWords[const-1]," ",arrayWords[const+1],arrayWords[const+2])
            elif i == 0 :
                const=i
                newWord=wordThread(v," "," ",arrayWords[const+1],arrayWords[const+2])
        else:
            if len(arrayWords)==1:
                const=i
                newWord=wordThread(v," "," "," "," ")
            if len(arrayWords)==2:
                if i==0:
                    const=i
                    newWord=wordThread(v," "," ",arrayWords[const+1]," ")
                elif i==1:
                    const=i
                    newWord=wordThread(v,arrayWords[const-1]," "," "," ")    
        inputFile.write(str(newWord.finalSentence))
    inputFile.close()

def tagger(outputFile,line):
    output=open(outputFile,'r')
    count=0
    newSentence=''
    for line1 in output:
        inpArray=line1.split()
        lineArray=line.split()
        if count==0:
            sent=lineArray[count].rsplit('/',2)
            newSentence=str(sent[0]+"/"+sent[len(sent)-1]+"/"+inpArray[0])
            count=count+1
        else:
            sent=lineArray[count].rsplit('/',2)
            newSentence=str(newSentence + " "+sent[0]+"/"+sent[len(sent)-1]+"/"+inpArray[0])
            count=count+1 
    newSentence=newSentence.replace('HASH','#')   
    sys.stdout.write(newSentence+'\n')
    output.close()


def main(buf,model):
    line=buf.getvalue()   
    line=line.replace('#','HASH')
    readText(str(line))
    cmd="/home/siddhartha/Downloads/megam_0.92/megam -nc -predict " + model + " multitron input.file > output.file"
    process=subprocess.call(cmd,shell=True)
    tagger("output.file",line)
        
        
if __name__=="__main__":
    while True: 
        val=sys.stdin.readline()
        if val != '\n':
            buf=StringIO(val)
            main(buf,sys.argv[1])
            buf.close()
            os.remove("input.file")
            os.remove("output.file")