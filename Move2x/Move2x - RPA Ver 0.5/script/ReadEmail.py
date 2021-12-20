"""
This script is used for reading E-mails


Made by 
@BJARKE ROBERT STØVE ANDERSØN
@CHRISTIAN MARC JØRGENSEN
@MAGNUS SØRENSEN 
@THOMAS HENRIKSEN  
"""
import imaplib
import email
"""
This method gets a Email from G-Mail and returns the mail

return:

-emailOrder (--emailOrder): output the a Email 
"""
def getEmail():
    #credentials - E-mail for reading
    username ="move2produktion@gmail.com"
    
    #generated app password - save this
    app_password= "igjbgewbhipccxes"
    
    # https://www.systoolsgroup.com/imap/
    gmail_host= 'imap.gmail.com'
    
    #set connection
    mail = imaplib.IMAP4_SSL(gmail_host)
    
    #login
    mail.login(username, app_password)
    
    #select inbox
    mail.select("INBOX")
    
    #select specific mails
    _, selected_mails = mail.search(None,'UNSEEN', '(FROM "move2ordre@gmail.com")')
    
    #total number of mails from specific user
    #print("Total messages from selected Email:" , len(selected_mails[0].split()))

    emailOrder =[]
    for num in selected_mails[0].split():
        _, data = mail.fetch(num , '(RFC822)')
        _, bytes_data = data[0]
        messageText = ''
        #convert the byte data to message
        email_message = email.message_from_bytes(bytes_data)
        print("\n===========================================")
    
        #access data
       # print("To:", email_message["to"])
       # print("From: ",email_message["from"])
       # print("Date: ",email_message["date"])
       # print("Subject: ",email_message["subject"])
        for part in email_message.walk():
            if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                message = part.get_payload(decode=True)
              #  print("Message: \n", message.decode())
                messageText = message.decode()
              #  print("==========================================\n")
                emailOrder.append(messageText)
                break
    return emailOrder