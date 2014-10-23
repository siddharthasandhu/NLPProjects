import glob
import os

trainingFile = open("trainingSPAMHAM.txt",'a')

def createTrainingFile():
    os.chdir("/home/siddhartha/Documents/CSCI544/SPAM_training")
    for file in glob.glob("*.txt"):
        firstPart=file.split('.')
        newLine= firstPart[0] + ' '
        f=open(file,'r').read().replace('\n'," ")
        newLine=newLine+ f + '\n'
        trainingFile.write(newLine)
    trainingFile.close()
    
        
if __name__=="__main__":
    createTrainingFile()