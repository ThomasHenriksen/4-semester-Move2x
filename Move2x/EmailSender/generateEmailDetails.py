import random

def listOfCompanies():
    companyList = ["Olympos", "Allen", "Ulf", "Alcippe", "Achieng"]
    return companyList

def returnCompany():
    companyList = listOfCompanies()
    i = random.randint(0,len(companyList)-1)
    companyReturn = companyList[i]
    return companyReturn

