import serial

#Define port, rate, and timeout
UAS = serial.Serial("COM4", baudrate=57600, timeout=3)
GCS = serial.Serial("COM3", baudrate=57600, timeout=3)
temp="1"
UAS.close()
GCS.close()

UAS.open()
GCS.open()

#write characters specified in utf_8
UAS.write(temp.encode(encoding='ASCII'))
print("sent1: "+temp)

#receive serial data as string


msg = str(GCS.read(len(temp)).decode('ASCII'))
print(msg)
GCS.close()
UAS.close()
