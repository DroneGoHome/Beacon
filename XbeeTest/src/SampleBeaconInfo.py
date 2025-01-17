from geopy.distance import vincenty
import collections


#Beacon Configuration
bShape="Cylinder" #Beacon Shape
nFBehavior="RTL" #Beacon behavior for unknown drones or drones inside no-fly
bRadius=15 #Beacon Radius in meters
bLoc=[40.399479, -74.299261, 200] #Beacon Lat/Long/Alt

droneList=collections.OrderedDict()  #Drone dictionary
droneList["drone1"]=[40.399479, -74.299258, 205] #Key is drone ID. Drone Lat/Long/Alt
droneList["drone2"]=[40.394720, -73.987302, 20]
droneList["drone3"]=[40.394456, -73.987602, 20]
droneList["drone4"]=[40.394654, -73.987150, 20]
droneList["drone5"]=[40.394951, -73.987750, 20]
droneList["drone6"]=[40.394026, -73.987369, 20]
droneList["drone7"]=[]

#loop through whole dictionary
for key, value in droneList.items():
    print(key+': loop')
    print(len(droneList[key]))
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
    print("Beacon GPS Location: "+ str(bLoc))
    print(key+" GPS Location: "+str(droneList[key]))

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
                    except:
                        #send NFBehavior
                        print("Assume "+key+" is in no-fly")
            else:
                print("No Drone Info! Requesting Info or initiating DoS Attack")      
        except:
            #request drone info. Upon 3 failures of same drone use DoS attack
            print("Unknown failure. Requesting Info or initiating DoS Attack")
