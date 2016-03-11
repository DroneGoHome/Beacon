#import winsound
#s=winsound.PlaySound("C:/Users/Taylor/Documents/siren.wav",winsound.SND_FILENAME)


import collections
from filehandler import readUIFile


from moduletest import *
uiDictionary=collections.OrderedDict(readUIFile("C:/Users/Taylor/Documents/UI Files/ui1.txt"))
print(uiDictionary)
sendsms(uiDictionary["NAME"], uiDictionary["NUMBER"], uiDictionary["CARRIER"])
print(uiDictionary["NAME"], uiDictionary["NUMBER"], uiDictionary["CARRIER"])


