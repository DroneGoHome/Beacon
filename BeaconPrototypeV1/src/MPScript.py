import collections, sys, time
sys.path.append(r"C:\Users\Taylor\AppData\Local\Programs\Python\Python35-32\Lib\site-packages")
print("Booting defense system...")
from geopy.distance import vincenty

print("Import complete. Beginning defense system")
#while True:    
#Beacon Configuration
bShape="Cylinder" #Beacon Shape
nFBehavior="RTL" #Beacon behavior for unknown drones or drones inside no-fly
bRadius=5 #Beacon Radius in meters
bLoc=[40.228354, -74.495501, 200] #Beacon Lat/Long/Alt

droneList=collections.OrderedDict()  #Drone dictionary
#droneList["drone1"]=[cs.lat, cs.lng, cs.alt] #Key is drone ID. Drone Lat/Long/Alt

for cycle in range (0,10):
    #loop through whole dictionary
    droneList["drone1"]=[cs.lat, cs.lng, cs.alt]
    for key, value in droneList.items():
        #print(key+': loop '+str(cycle))
        #adjust beacon location accuracy for comparison to drone
        try:
            if droneList[key]:
                dLatAc=len(str(droneList[key])) #get accuracy of drone Lat
                dLonAc=len(str(droneList[key])) #get accuracy of drone long
                adjBLoc=[str(bLoc[0])[:dLatAc], str(bLoc[1])[:dLonAc]] #adjusted beacon accuracy
            else:
                #request drone info. Upon 3 failures of same drone use DoS attack
                print("No Drone Info! Requesting Info or initiating DoS Attack")
        except:
            #request drone info. Upon 3 failures of same drone use DoS attack
            print("No Drone Info! Requesting Info or initiating DoS Attack")
        #print("Beacon GPS Location: "+ str(bLoc))
        #print(key+" GPS Location: "+str(droneList[key]))

        if bShape=="Cylinder":
            try:
                if droneList[key]:
                    dDist=round(vincenty(adjBLoc,droneList[key]).meters,2)
                    print(key+"'s Lat/Long distance from beacon: "+str(dDist))
                    if dDist>bRadius:
                        #send serial data about beacon and request drone info
                        print(key+" outside no-fly")
                    elif dDist<=bRadius:
                        print(key+" is inside beacon lat/long")
                        try:
                            if droneList["drone1"][2]>bLoc[2]:
                                #send serial data about beacon and request drone info
                                print(key+" is over no-fly")
                            else:
                                #send serial data for NFBehavior
                                print(key+" is in no-fly")
                                print('Script.ChangeMode("RTL")')
                                print("Sent beacon request: "+nFBehavior)
                        except:
                            #send NFBehavior
                            print("Assume "+key+" is in no-fly")
                            print('Script.ChangeMode("RTL")')
                            print("Sent beacon request: "+nFBehavior)
                else:
                    print("No Drone Info! Requesting Info or initiating DoS Attack")      
            except:
                #request drone info. Upon 3 failures of same drone use DoS attack
                print("Unknown failure. Requesting Info or initiating DoS Attack")
    Script.Sleep(3000)
print("finished")