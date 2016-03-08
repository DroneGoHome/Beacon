import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login('dghprototype@gmail.com','Beacon01')
server.sendmail( 'dghprototype@gmail.com', '7329913605@txt.att.net', 'Hey Linda, this is a test SMS from python. Hopefully you have ATT!' )