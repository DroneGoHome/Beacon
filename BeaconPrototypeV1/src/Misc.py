#import winsound
#s=winsound.PlaySound("C:/Users/Taylor/Documents/siren.wav",winsound.SND_FILENAME)


import collections
from FileHandler import readUIFile
uiDictionary=collections.OrderedDict(readUIFile("C:/Users/Taylor/Documents/UI Files/ui1.txt"))
print(uiDictionary["name".upper()])