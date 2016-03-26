print("Booting defense system...")
import collections, sys, subprocess, datetime, time, threading #@UnresolvedImport #@UnusedImport
from moduletest import *
sys.path.append(r"C:\Users\Taylor\AppData\Local\Programs\Python\Python35-32\Lib\site-packages")
from geopy.distance import vincenty #@UnresolvedImport
print("Import complete. Beginning defense system")
#while True:    
#Beacon Configuration
beaconInfo=readUIFile("C:\\Users\\Taylor\\Documents\\UI Files\\BeaconUI.txt")
bShape=beaconInfo["SHAPE"] #Beacon Shape
nFBehavior=beaconInfo["BEHAVIOR"] #Beacon behavior for unknown drones or drones inside no-fly
bRadius=int(beaconInfo["RADIUS"]) #Beacon Radius in meters
bRetry=int(beaconInfo["RETRY"])
bLoc=[40.535828, -74.300070, 200] #Beacon Lat/Long/Alt
droneList=collections.OrderedDict()  #Drone dictionary
droneList["DGH Prototype DIY Quadcopter"]=[cs.lat, cs.lng, cs.alt] #Key is drone ID. Drone Lat/Long/Alt
def perim_check():
    for cycle in range (0,1):
        #loop through whole dictionary
        #droneList["DGH Prototype DIY Quadcopter"]=[cs.lat, cs.lng, cs.alt] #@UndefinedVariable
        for key, value in droneList.items():
            #print(key+': loop '+str(cycle))
            #adjust beacon location accuracy for comparison to drone
            try:
                if value:
                    dLatAc=len(str(value[0])) #get accuracy of drone Lat
                    dLonAc=len(str(value[1])) #get accuracy of drone long
                    adjBLoc=[float(str(bLoc[0])[:dLatAc]), float(str(bLoc[1])[:dLonAc])] #adjusted beacon accuracy
                else:
                    #request drone info. Upon 3 failures of same drone use DoS attack
                    print("No Drone Info! Requesting Info or initiating DoS Attack")
            except:
                #request drone info. Upon 3 failures of same drone use DoS attack
                print("No Drone Info! Requesting Info or initiating DoS Attack")
                print("Unknown error: "+str(sys.exc_info()[0]))
            #print("Beacon GPS Location: "+ str(bLoc))
            #print(key+" GPS Location: "+str(value))
    
            if bShape=="CYLINDER":
                try:
                    if value:
                        dDist=round(vincenty(adjBLoc,value[0:2]).meters,2)
                        print(key+"'s Lat/Long distance from beacon: "+str(dDist))
                        if dDist>bRadius:
                            #send serial data about beacon and request drone info
                            print(key+" outside no-fly")
                            dStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                            tStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                            with open("C:\\Users\\Taylor\\Documents\\GitHub\\DataCollection\\test.csv",'a') as myfile:
                                myfile.write("\n"+dStamp+";"+tStamp+";"+key+";"+str(dDist)+";"+"Drone detected outside no-fly zone!")
                        elif dDist<=bRadius:
                            print(key+" is inside beacon lat/long")
                            try:
                                if value[2]>bLoc[2]:
                                    #send serial data about beacon and request drone info
                                    print(key+" is over no-fly")
                                    dStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                                    tStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                                    with open("C:\\Users\\Taylor\\Documents\\GitHub\\DataCollection\\test.csv",'a') as myfile:
                                        myfile.write("\n"+dStamp+";"+tStamp+";"+key+";"+str(dDist)+";"+"None, Drone over no-fly zone")
                                else:
                                    #send serial data for NFBehavior
                                    print(key+" is in no-fly")
                                    #attempts to initiate RTL mode
                                    for attempt in range (1,bRetry+1):
                                        if cs.mode != nFBehavior: #@UndefinedVariable                                  
                                            Script.ChangeMode(nFBehavior)#@UndefinedVariable
                                            print("Attempt #"+attempt+". Sent beacon request: "+nFBehavior)
                                            Script.Sleep(750)#@UndefinedVariable
                                            dStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                                            tStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                                    with open("C:\\Users\\Taylor\\Documents\\GitHub\\DataCollection\\test.csv",'a') as myfile:
                                        myfile.write("\n"+dStamp+";"+tStamp+";"+key+";"+str(dDist)+";"+"Initiated RTL")                                    
                            except:
                                #send NFBehavior
                                print("Assume "+key+" is in no-fly")
                                print("Unknown error: "+str(sys.exc_info()[0]))
                                for attempt in range (1,bRetry+1):
                                        if cs.mode != nFBehavior: #@UndefinedVariable                                  
                                            Script.ChangeMode(nFBehavior)#@UndefinedVariable
                                            print("Attempt #"+attempt+". Sent beacon request: "+nFBehavior)
                                            Script.Sleep(750)#@UndefinedVariable
                                dStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                                tStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                                with open("C:\\Users\\Taylor\\Documents\\GitHub\\DataCollection\\test.csv",'a') as myfile:
                                    myfile.write("\n"+dStamp+";"+tStamp+";"+key+";"+str(dDist)+";"+"Assuming drone is in no-fly, initiated RTL")     
                except:
                    #request drone info. Upon 3 failures of same drone use DoS attack
                    print("Unknown failure. Requesting Info or initiating DoS Attack")
                    print("Unknown error: "+str(sys.exc_info()[0]))
        #Script.Sleep(1000)#@UndefinedVariable
        time.sleep(1)
        print("Finished, publishing results")

        
threading.Thread(target=perim_check()).start()
#threading.Thread(target=git_upload()).start()

'''
print("Finished, publishing results")
p = subprocess.Popen([r"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", "-ExecutionPolicy", "Unrestricted", "-File",
              "C:/Users/Taylor/Documents/LiClipse Workspace/BeaconPrototypeV1/src/Git.ps1"], 
              stdout=sys.stdout)
p.communicate()
'''
print("Upload Complete")