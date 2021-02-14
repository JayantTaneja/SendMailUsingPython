import smtplib

def sendmailcode(server,port,username,password,to,message):
    myconnection = smtplib.SMTP(server,port)
    myconnection.starttls()
    '''
    starts the tls service(transport layer socket) for security
    '''
    myconnection.login(username,password)
    myconnection.sendmail(username,to,message)
    myconnection.close()
    '''
    terminates the connection and logs out from the mail
    '''

sender_email=input("Enter your email id       : ")

password=input("Enter password            : ")

reciever_email=input("Enter email id of reciever: ")


sendmailcode('smtp.gmail.com',587,sender_email,password,reciever_email,message)


