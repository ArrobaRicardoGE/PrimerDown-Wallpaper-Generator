import smtplib,os

#Please note that these are environment variables
aTW_EMAIL = os.environ["TW_EMAIL"]
aTW_EMAIL_PASS = os.environ["TW_EMAIL_PASS"]
aTW_EMAIL_RECIPIENT = os.environ["TW_EMAIL_RECIPIENT"]

def sendEmail(subject, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(aTW_EMAIL,aTW_EMAIL_PASS)
        server.sendmail(aTW_EMAIL,aTW_EMAIL_RECIPIENT,"Subject: {}\r\nFrom: {}\r\nTo: {}\r\n{}".format(subject,aTW_EMAIL,aTW_EMAIL_RECIPIENT,message))
        server.close()
        return("Email successfully sent")
    except Exception as e:
        return("Unable to send email: {}".format(e))

if(__name__=="__main__"):
    print(sendEmail("Test Email","\nHi, this is just for testing purposes"))