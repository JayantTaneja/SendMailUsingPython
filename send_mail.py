import smtplib
'''
smtp is a server protocol
this lib contains the required stuff for it
'''

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

sendmailcode('smtp.gmail.com',587,'pythonap2v@gmail.com','ap2vap2v','jayanttaneja1@gmail.com','Hi There !! \n this message has been sent by a python program')

