print("Booting defense system...")
import collections, sys, subprocess, datetime, time, threading #@UnresolvedImport #@UnusedImport
sys.path.append(r"C:\Users\Taylor\AppData\Local\Programs\Python\Python35-32\Lib\site-packages")
sys.path.append(r"C:\Users\Taylor\Documents\LiClipse Workspace\BeaconPrototypeV1\src")
from moduletest import *
from geopy.distance import vincenty #@UnresolvedImport
print("Import complete. Beginning defense system")
#while True:    
#Beacon Configuration
beaconInfo=readUIFile("C:\\Users\\Taylor\\Documents\\UI Files\\BeaconUI.txt")
bShape=str(beaconInfo["SHAPE"]) #Beacon Shape
nFBehavior=str(beaconInfo["BEHAVIOR"]) #Beacon behavior for unknown drones or drones inside no-fly
bRadius=int(beaconInfo["RADIUS"]) #Beacon Radius in meters
bRetry=int(beaconInfo["RETRY"])
bLoc=[0.00, 0.00, 200] #Beacon Lat/Long/Alt
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
                        if dDist>bRadius:#Outside nofly
                            #send serial data about beacon and request drone info
                            print(key+" outside no-fly")
                            dStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                            tStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                            updateLog(dStamp,tStamp,key,dDist,"Drone detected outside no-fly zone.")
                        elif dDist<=bRadius:#Inside nofly
                            print(key+" is inside beacon lat/long")
                            try:
                                if value[2]>bLoc[2]:
                                    #send serial data about beacon and request drone info
                                    print(key+" is over no-fly")
                                    dStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                                    tStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                                    updateLog(dStamp,tStamp,key,dDist,"Drone over no-fly zone")
                                else:
                                    #send serial data for NFBehavior
                                    print(key+" is in no-fly")
                                    #attempts to initiate RTL mode
                                    for attempt in range (1,bRetry+1):
                                        if cs.mode != nFBehavior: #@UndefinedVariable                              
                                            Script.ChangeMode(nFBehavior)#@UndefinedVariable
                                            print("Attempt #"+str(attempt)+". Sent beacon request: "+nFBehavior)
                                            dStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                                            tStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                                            updateLog(dStamp,tStamp,key,dDist,"Drone detected inside No-Fly. Initiated "+nFBehavior+" command!")
                                            time.sleep(0.75)
                                    if cs.mode != nFBehavior:#@UndefinedVariable
                                        dStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                                        tStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                                        updateLog(dStamp,tStamp,key,dDist,"Unable to command drone after "+str(bRetry)+" attempts.")
                                        #initiate jammer
                                                                                
                            except:
                                #send NFBehavior
                                print("Assume "+key+" is in no-fly")
                                print("Unknown error: "+str(sys.exc_info()[0]))
                                for attempt in range (1,bRetry+1):
                                    if cs.mode != nFBehavior: #@UndefinedVariable                                  
                                        Script.ChangeMode(nFBehavior)#@UndefinedVariable
                                        print("Attempt #"+str(attempt)+". Sent beacon request: "+nFBehavior)                                       
                                        dStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                                        tStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                                        updateLog(dStamp,tStamp,key,dDist,"Assuming drone is in no-fly, initiated RTL")
                                        time.sleep(0.75)
                                if cs.mode != nFBehavior:#@UndefinedVariable
                                    dStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                                    tStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                                    print("Failed to initiate "+nFBehavior)
                                    updateLog(dStamp,tStamp,key,dDist,"Unable to command drone after "+str(bRetry)+" attempts.")
                                    #initiate jammer
                except:
                    #request drone info. Upon 3 failures of same drone use DoS attack
                    print("Unknown failure. Requesting Info or initiating DoS Attack")
                    print("Unknown error: "+str(sys.exc_info()[0]))
        time.sleep(1)
        print("Finished, publishing results")

        
threading.Thread(target=perim_check()).start()
threading.Thread(target=git_upload()).start()