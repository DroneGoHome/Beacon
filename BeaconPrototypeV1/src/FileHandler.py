import collections, re
def readUIFile(loc):
    fileDict=collections.OrderedDict()
    fileText=open(loc,"r").read()
    fileText=re.sub('\n',":",fileText).upper()
    fileArray=fileText.split(":")
    for n in range(0,len(fileArray)-1,2):
        fileDict[fileArray[n]]=fileArray[n+1]
    return(fileDict)
#print(readUIFile("C:/Users/Taylor/Documents/UI Files/ui1.txt"))