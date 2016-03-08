import serial, sys


GCS = serial.Serial("COM4", baudrate=57600, timeout=3)
GCS.close()
GCS.open()
#temp="\xfe\t\x03"
for x in range(0,1):
    print(GCS.read(17))
GCS.close()