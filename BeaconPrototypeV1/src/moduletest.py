def print_loc(droneLocation):
    print(droneLocation[0])
    print(droneLocation[1])
    print(droneLocation[2])
    
def sendsms(name,number,carrier):
    if carrier!="NONE":
        import smtplib, collections
        gateway=collections.OrderedDict()
        gateway["VERIZON"]="vtext.com"
        gateway["AT&T"]="txt.att.net"
        gateway["BOOST"]="sms.myboostmobile.com"
        gateway["SPRINT"]="messaging.sprintpcs.com"
        gateway["T-MOBILE"]="tmomail.net"
        gateway["VIRGIN MOBILE"]="vmobl.com"
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login('dghprototype@gmail.com','Beacon01')
        server.sendmail( 'dghprototype@gmail.com', number+'@'+gateway[carrier], 'Hello '+name+', this is a message from your DGH defense system. There has been a perimeter breach')
def git_upload():
    import subprocess, sys
    p = subprocess.Popen([r"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", "-ExecutionPolicy", "Unrestricted", "-File",
              "C:/Users/Taylor/Documents/LiClipse Workspace/BeaconPrototypeV1/src/Git.ps1"], 
              stdout=sys.stdout)
    p.communicate()
    print("GIT upload Complete")
    
def readUIFile(loc):
    import collections, re
    fileDict=collections.OrderedDict()
    fileText=open(loc,"r").read()
    fileText=re.sub('\n',":",fileText).upper()
    fileArray=fileText.split(":")
    for n in range(0,len(fileArray)-1,2):
        fileDict[fileArray[n]]=fileArray[n+1]
    return(fileDict)