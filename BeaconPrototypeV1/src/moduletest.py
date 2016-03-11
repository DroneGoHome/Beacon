def PrintLoc(droneLocation):
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
