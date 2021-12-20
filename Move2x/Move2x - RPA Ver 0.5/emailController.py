"""
This script is used for controlling the Email and XML save

Made by 
@BJARKE ROBERT STØVE ANDERSØN
@CHRISTIAN MARC JØRGENSEN
@MAGNUS SØRENSEN 
@THOMAS HENRIKSEN  
"""
from script import xmlScript as xml
from script import ReadEmail as email



#This method is used to read the Email
def readEmail():
    return email.getEmail() #Returns the email or emails if there are more

#This method is used to save the XML file
def saveXml(order):
    xml.saveOrder(order)


"""
This method is used for deconstructing the email and assemble an order

                  !!!!!!Attention!!!!!!!
THIS CODE NEEDS TO BE REFACTORED FROM HARDCODED TO DYNAMIC

Return:
-update (--bool): outputs true if there is a new email
"""
def getOrderFromEmail():
    emailText = readEmail()
    update = False
    for emailOrder in emailText:
        text = emailOrder.split()
        i = len(text)-1 
        if(text[11] =='1' ):
            order = [text[i-4],text[i][1:6],text[9]+' '+text[10]+' '+text[11]+' '+text[12]+' '+text[13]+' '+text[14]]
        elif(text[11] == 'phone'):
            order = [text[i-4],text[i][1:6],text[9]+' '+text[10]+' '+text[11]+' '+text[12]]
        else:
            order = [text[i-4],text[i][1:6],text[9]+' '+text[10]+' '+text[11]+' '+text[12]+' '+text[13]]
        saveXml(order)
        
        update = True
    
    return update
    
    

