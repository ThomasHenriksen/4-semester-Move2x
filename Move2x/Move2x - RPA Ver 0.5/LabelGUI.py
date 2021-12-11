import tkinter as tk
from tkinter import *

from concurrent import futures
import time
import os 
from PIL import Image, ImageTk
from script import xmlScript as xml
import labelController 
import emailController
thread_pool_executor = futures.ThreadPoolExecutor(max_workers=2)

class MainFrame(tk.Frame):
 
    def __init__(self, *args, **kwargs):
        btnY = 235

        super().__init__(*args, **kwargs)

        

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
        global var1
        var1 = tk.IntVar()
        self.btnCancel = tk.Button(self, text='Cancel Order', command=self.btnCancel)
        self.btnCancel.place(y=btnY, x=300, anchor='s')
        self.btnPrint = tk.Button(self, text='Print Order', command=self.btnPrint)
        self.btnPrint.place(y=btnY, x=400, anchor='s')
        self.btnRefresh = tk.Button(self, text='Refresh Orders', command=self.btnRefresh)
        self.btnRefresh.place(y=btnY, x=190, anchor='s')
        self.btnRefresh = tk.Button(self, text='Open Dymo', command=self.btnOpenDymo)
        self.btnRefresh.place(y=btnY, x=90, anchor='s')
        self.c1 = tk.Checkbutton(self, text='Email check',variable=var1, onvalue=1, offvalue=0, command=self.c1Check)
        self.c1.place(y=btnY, x=540, anchor='s')
        self.lblCustomer = tk.Label(self, bg="white", text='Customer')
        self.lblCustomer.place(y=82, x=430, anchor='s') # y=120, x=470, anchor='s'
        self.lblProduct = tk.Label(self, bg="white", text=' ')
        self.lblProduct.place(y=111, x=420, anchor='s')
        self.lblTime = tk.Label(self, bg="white", text='time', compound='center')
        self.lblTime.place(y=82, x=515, anchor='s')
        global iemail
        iemail = 0
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

    def c1Check(self):
        thread_pool_executor.submit(self.blocking_email)
         
    def btnCancel(self):
        thread_pool_executor.submit(self.blocking_Cancel)

    def btnOpenDymo(self):
        thread_pool_executor.submit(self.blocking_OpenDymo)

    def btnPrint(self):
        thread_pool_executor.submit(self.blocking_Print)
    def btnRefresh(self):
        thread_pool_executor.submit(self.blocking_refresh)
    def xmlOrder(self):
        self.listbox.delete(0,tk.END)
        orderList = xml.getOrder()
        
        orderList = sorted(orderList, key = lambda i: i[2])
        for order in orderList:
            if(order[1] == '000000'):
                self.btnCancel['state'] = 'disabled'
                self.btnPrint['state'] = 'disabled'
                self.om1['state'] = 'disabled'
            else:
                self.btnCancel['state'] = 'normal'
                self.btnPrint['state'] = 'normal'
                self.om1['state'] = 'normal'
            self.after(0, self.listbox_insert,order[2] +' - '+ order[1] +' - '+ order[3] +' - '+ order[4] )
        self.after(0, self.set_lblCustomer_text, orderList[0][1])
        self.after(0, self.set_lblTime_text, orderList[0][2])
        self.after(0, self.set_size_options(orderList[0][3]))
        self.after(0, self.set_lblProduct_text, orderList[0][4])
        return orderList

    
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
            menu.add_command(label=string, command=lambda value=string: self.om_variable.set(value))
    
    def option_select(self, *args):
        return self.om_variable.get()    

 

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
        order = xml.getOrder()
        
        self.after(0, self.set_lblCustomer_text, order[index][1])
        self.after(0, self.set_lblTime_text, order[index][2])
        self.after(0, self.set_size_options(order[index][3]))
        self.after(0, self.set_lblProduct_text, order[index][4])

    def blocking_Cancel(self):
        xml.changeStatusOnOrderXml('ocr', self.lblCustomer['text']+' '+ self.lblProduct['text'],'Cancel' ,self.option_select())
        self.xmlOrder()
    def blocking_OpenDymo(self):
        labelController.dymo() 
    def blocking_Print(self):
        self.btnCancel['state'] = 'disabled'
        self.btnPrint['state'] = 'disabled'
        self.om1['state'] = 'disabled'
        labelController.labelMaker(self.lblCustomer['text'],self.lblTime['text'], self.lblProduct['text'],self.option_select())
        xml.changeStatusOnOrderXml('ocr', self.lblCustomer['text']+' '+ self.lblProduct['text'],'Done',self.option_select())
        self.xmlOrder()
        self.btnCancel['state'] = 'normal'
        self.btnPrint['state'] = 'normal'
        self.om1['state'] = 'normal'
    def blocking_refresh(self):
        self.xmlOrder()    
    def blocking_email(self):
        while(var1.get() == 1):
            update = emailController.getOrderFromEmail()
            
            if(update):
                self.xmlOrder()
            time.sleep(2)
               

         
if __name__ == '__main__':
    app = tk.Tk()
    app.title("Move2x")
    app.geometry("650x245+1250+0")
    app.resizable(width=False, height=False)
    app.wm_attributes("-topmost", 1)
    main_frame = MainFrame()
    app.mainloop()

