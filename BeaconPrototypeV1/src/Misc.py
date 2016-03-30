def updateLog(dStamp,tStamp,key,dDist,message):
    import os.path
    fPath="C:/Users/Taylor/Documents/GitHub/DataCollection/test.csv"
    if not os.path.exists(fPath):
        print("true")
        with open("C:\\Users\\Taylor\\Documents\\GitHub\\DataCollection\\test.csv",'a') as myfile:
                                        myfile.write("Local Date;Local Time;UAS ID;Distance From Beacon;Beacon Response")
    with open("C:\\Users\\Taylor\\Documents\\GitHub\\DataCollection\\test.csv",'a') as myfile:
                                        myfile.write("\n"+dStamp+";"+tStamp+";"+key+";"+str(dDist)+";"+message)

updateLog("test","test2","test3","test4","test5")
testvar=4