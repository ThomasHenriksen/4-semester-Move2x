from win32com.client import Dispatch
import pathlib


my_printer = 'DYMO LabelWriter 450 Turbo'
label_path = pathlib.Path('move2xLabel.label')

def dymoController(customerNo, product, productNo):
    """description of class uses stored information to print order/s"""
    print(customerNo)
    print(product)
    print(productNo)
    printer_com = Dispatch('Dymo.DymoAddIn')
    printer_com.SelectPrinter('my_printer')
    printer_com.Open(label_path)
    #TEXT is prduct + productNumber , ADDRESS is customerNumber
    printer_label = Dispatch("Dymo.DymoLabels")
    printer_label.SetField('Product', product)
    printer_label.SetField('ADRESSE', "Customer No: " + customerNo + "Product: " + product + " Product No: " + productNo)
    #printer_label.SetField('TEXT_1', label_timestamp) for later use if we have to take in timestamps

    printer_com.StartprintJob()
    printer_com.Print(1, False)
    printer_com.EndPrintJob()
