from script import xmlScript as xml
from script import ReadEmail as email


#[10017, '01:00', '3 pcs black 1 fuse r (1213)']
def readEmail():
    return email.getEmail()
def saveXml(order):
    xml.saveToXmlFromEmail(order)
def getOrderFromEmail():
    emailText = readEmail()

    update = False
    
    i = 0

    for emailOrder in emailText:

        text = emailOrder.split()
        i = len(text)-1    
        order = [text[i][1:6],text[i-4],text[9]+' '+text[10]+' '+text[11]+' '+text[12]]
        saveXml(order)
        update = True
    
    return update
    
    

