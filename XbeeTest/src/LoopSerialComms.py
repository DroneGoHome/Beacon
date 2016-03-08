import serial

#Define port, rate, and timeout
UAS = serial.Serial("COM4", baudrate=57600, timeout=3)
#GCS = serial.Serial("COM3", baudrate=57600, timeout=3)
temp=1
UAS.close()
#GCS.close()

UAS.open()
#GCS.open()

while temp<=15:
    
    #write characters specified in utf_8
    UAS.write(str(temp).encode(encoding='ASCII'))
    print("UAS sent: "+str(temp))
    temp=temp+1 
    
''' #receive serial data as string
    msg = str(GCS.read(1).decode('ASCII'))
    #strips out b'' from the string 
    print("GCS received: "+msg)
    temp=temp+1
    print("incremented temp to: "+str(temp))
    #send response to UAS'''
    

#GCS.close()
UAS.close()