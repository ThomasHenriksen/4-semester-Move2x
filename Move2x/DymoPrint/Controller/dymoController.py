from win32com.client import Dispatch
import pathlib
import dymoModel # Is not usefull as we don't use the model-layer

my_printer = 'DYMO LabelWriter 450 Turbo'
label_path = pathlib.Path('move2xLabel.label')

class dymoController(customerNo, product, productNo):
    """description of class uses stored information to print order/s"""

    printer_com = Dispatch('Dymo.DymoAddIn')
    printer_com.SelectPrinter('my_printer')
    printer_com.Open(label_path)
    #TEXT is prduct + productNumber , ADDRESS is customerNumber
    printer_label = Dispatch("Dymo.DymoLabels")
    printer_label.SetField('TEXT', product, productNo)
    printer_label.SetField('ADRESSE', customerNo)
    #printer_label.SetField('TEXT_1', label_timestamp) for later use if we have to take in timestamps

    printer_com.StartprintJob()
    printer_com.Print(1, False)
    printer_com.EndPrintJob()
