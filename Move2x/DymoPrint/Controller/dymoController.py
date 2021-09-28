from win32com.client import Dispatch
import pathlib

my_printer = 'DYMO LabelWriter 450 Turbo'
label_path = pathlib.Path('move2xLabel.label')

class dymoController(object):
    """description of class uses stored information in model to print order/s"""

    printer_com = Dispatch('Dymo.DymoAddIn')
    printer_com.SelectPrinter('my_printer')
    printer_com.Open(label_path)

    printer_label = Dispatch("Dymo.DymoLabels")
    printer_label.SetField('TEXT', label_product)
    printer_label.SetField('ADDRESS', label_val)

    printer_com.StartprintJob()
    printer_com.Print(1, False)
    printer_com.EndPrintJob()
