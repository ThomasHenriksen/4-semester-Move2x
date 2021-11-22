import tkinter as tk
from tkinter import *
from concurrent import futures
import time
import os 
from PIL import Image, ImageTk
from pathlib import Path
from script import xmlScript as xml
import labelController 
thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)
 
class MainFrame(tk.Frame):
 
    def __init__(self, *args, **kwargs):
        btnY = 265
        super().__init__(*args, **kwargs)
        self.label = tk.Label(self, text='')
        self.label.pack(side="top", pady=5, padx=5, anchor="w")
        sb = Scrollbar(self, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.listbox = tk.Listbox(self)
        self.listbox.bind('<<ListboxSelect>>', self.getElement)
        self.listbox.configure(yscrollcommand=sb.set)
        sb.config(command=self.listbox.yview)
        self.listbox.pack(side="left", padx=0, pady=0, anchor="nw", fill=tk.X,expand=True)
        backgroundImg = ImageTk.PhotoImage(Image.open("resources\\Label.png").resize((341, 198)))
        self.lblBgImg=tk.Label(self, image = backgroundImg)
        self.lblBgImg.image = backgroundImg
        self.lblBgImg.pack(side="top")

        self.btnCancel = tk.Button(self, text='Cancel Order', command=self.btnCancel)
        self.btnCancel.place(y=btnY, x=300, anchor='s')
        self.btnPrint = tk.Button(self, text='Print Order', command=self.btnPrint)
        self.btnPrint.place(y=btnY, x=400, anchor='s')
       
        self.lblCustomer = tk.Label(self, bg="white", text='Customer')
        self.lblCustomer.place(y=112, x=430, anchor='s') # y=120, x=470, anchor='s'
        self.lblProduct = tk.Label(self, bg="white", text=' ')
        self.lblProduct.place(y=141, x=420, anchor='s')
        self.lblTime = tk.Label(self, bg="white", text='time', compound='center')
        self.lblTime.place(y=112, x=515, anchor='s')
        self.options = tk.StringVar(self) # variable 
        global qualityList 
        qualityList = ["1"]

        self.om_variable = tk.StringVar(self)
        self.om_variable.set(qualityList[0])
        self.om_variable.trace('w', self.option_select)

        self.options.set(qualityList[0]) # default value
        self.om1 =tk.OptionMenu(self, self.om_variable, *qualityList)
        
        self.om1.place(y=btnY+2, x=465, anchor='s')
        self.pack(fill=BOTH, expand=1)
        self.xmlOrder()

    def btnCancel(self):
        
        thread_pool_executor.submit(self.blocking_Cancel)
    def btnPrint(self):
        
        thread_pool_executor.submit(self.blocking_Print)
    def xmlOrder(self):
         orderList = self.getOrder()
         for order in orderList:
             self.after(0, self.listbox_insert, order[0] +' '+ order[3] )
         self.after(0, self.set_lblCustomer_text, orderList[0][0])
         self.after(0, self.set_lblTime_text, orderList[0][1])
         self.after(0, self.set_size_options(orderList[0][2]))
         self.after(0, self.set_lblProduct_text, orderList[0][3])
         return orderList

    def getOrder(self):
        orderList = xml.readOrderXml('ocr')
        order = []
        for b in orderList:
            if(len(b) > 4):
               order.append(b[:4])
               order.append(b[4:])
            else:
               order.append(b)
        

        return order
    def set_size_options(self, quality):
        
        size =int(quality)   
        
        i = 0
        qualityList = []
        while(i < size):
           i+=1
           qualityList.append(i)
           
        qualityList.reverse()
        menu = self.om1["menu"]
        menu.delete(0, "end")
        self.om_variable.set(qualityList[0])
        for string in qualityList:
            menu.add_command(label=string, 
                             command=lambda value=string: self.om_variable.set(value))
    
    def option_select(self, *args):
        return self.om_variable.get()    
    def set_label_text(self, text=''):
        self.label['text'] = text

    def set_lblCustomer_text(self, text=''):
        self.lblCustomer['text'] = text

    def set_lblProduct_text(self, text=''):
        self.lblProduct['text'] = text

    def set_lblTime_text(self, text=''):
        self.lblTime['text'] = text

    def listbox_insert(self, item):
        self.listbox.insert(tk.END, item)

    def getElement(self, event):
        selection = event.widget.curselection()
        index = selection[0]
        value = event.widget.get(index)
        order = self.getOrder()
     
        self.after(0, self.set_lblCustomer_text, order[index][0])
        self.after(0, self.set_lblTime_text, order[index][1])
        self.after(0, self.set_size_options(order[index][2]))
        self.after(0, self.set_lblProduct_text, order[index][3])

    def blocking_Cancel(self):
        NUll
    
    
    
    def blocking_Print(self):
        
        labelController.labelMaker(self.lblCustomer['text'],self.lblTime['text'], self.lblProduct['text'],self.option_select())

 
if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("650x275")
    app.resizable(width=False, height=False)
    main_frame = MainFrame()
    app.mainloop()

