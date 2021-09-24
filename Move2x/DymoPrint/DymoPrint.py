from win32com.client import Dispatch
import pathlib

label_val = 'customer name'
label_product = 'product name'
my_printer = 'DYMO LabelWriter 450 Turbo'
label_path = pathlib.Path('move2xLabel.label')

printer_com = Dispatch('Dymo.DymoAddIn')
printer_com.SelectPrinter('my_printer')
printer_com.Open(label_path)

printer_label = Dispatch("Dymo.DymoLabels")
printer_label.SetField('TEXT', label_product)
printer_label.SetField('ADDRESS', label_val)

printer_com.StartprintJob()
printer_com.Print(1, False)
printer_com.EndPrintJob()


