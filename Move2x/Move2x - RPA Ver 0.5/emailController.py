from script import xmlScript as xml
from script import ReadEmail as email




def readEmail():
    return email.getEmail()
def saveXml(order):
    xml.saveToXmlFromEmail(order)
def getOrderFromEmail():
    emailText = readEmail()
    update = False
    for emailOrder in emailText:
        text = emailOrder.split()
        i = len(text)-1 
        if(text[11] =='1' ):
            order = [text[i][1:6],text[i-4],text[9]+' '+text[10]+' '+text[11]+' '+text[12]+' '+text[13]+' '+text[14]]
        elif(text[11] == 'phone'):
            order = [text[i][1:6],text[i-4],text[9]+' '+text[10]+' '+text[11]+' '+text[12]]
        else:
            order = [text[i][1:6],text[i-4],text[9]+' '+text[10]+' '+text[11]+' '+text[12]+' '+text[13]]
        saveXml(order)
        update = True
    
    return update
    
    

