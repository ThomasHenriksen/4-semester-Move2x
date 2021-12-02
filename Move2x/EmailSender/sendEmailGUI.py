import tkinter as tk
from tkinter import *
from concurrent import futures
import time
import os
from PIL import Image, ImageTk
#from script import xmlScript as xml
import sendEmail
import ProductAccess
thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)
 
class MainFrame(tk.Frame):
 
    def __init__(self, *args, **kwargs):
        btnY = 200

        super().__init__(*args, **kwargs)

        
        sb = Scrollbar(self, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)

        self.listbox = tk.Listbox(self)
        self.listbox.bind('<<ListboxSelect>>')
        self.listbox.configure(yscrollcommand=sb.set)

        sb.config(command=self.listbox.yview)
        self.listbox.pack(side="left", padx=0, pady=0, anchor="nw", fill=tk.X,expand=True)

        self.btnSend = tk.Button(self, text='Send', command=self.btnSend)
        self.btnSend.place(y=btnY, x=25, anchor='w', width=50)
        self.pack(fill=BOTH, expand=1) 
        self.lblCustomer = tk.Label(self)
        self.lblProduct = tk.Label(self)
        self.lblTime = tk.Label(self)
        self.xmlOrder()

    def set_lblCustomer_text(self, text=''):
        self.lblCustomer['text'] = text
    def set_lblProduct_text(self, text=''):
        self.lblProduct['text'] = text
    def set_lblTime_text(self, text=''):
        self.lblTime['text'] = text


    # Send button
    def btnSend(self):
        thread_pool_executor.submit(self.blocking_Send)
   
    # Xml order for the data to show
    def xmlOrder(self):
        global listOfOrders
        listOfOrders =[]
        self.listbox.delete(0,tk.END)
        orderList = ProductAccess.getOrderFromDataBase()
        for order in orderList:
            if(order[1] == '000000'):
                self.btnSend['state'] = 'disabled'
            else:
                self.btnSend['state'] = 'normal'
            self.after(0, self.listbox_insert,order[0] +' - '+ str(order[1]) +' - '+ str(order[2]) +' - '+ order[3] +' - '+ order[4] )
        listOfOrders = orderList
        return orderList

    
    def listbox_insert(self, item):
        self.listbox.insert(tk.END, item)
        
    #sendEmail(subject, message):
    def blocking_Send(self):
        curselectedOrder = listOfOrders[self.listbox.curselection()[0]]
        subject = " Dear Smarter Production inc. l would like to ordre:"
        print(curselectedOrder)
        sendEmail.sendEmail("New Order", message = self.listbox.get(self.listbox.curselection()))
        listOfOrders.pop(self.listbox.curselection()[0])
        self.listbox.delete(ACTIVE)

    def emailBuilder(order, companyName):
        curOrder = order
        curCompanyName = company
        subject = " Dear Smarter Production inc. l would like to ordre:"
        if(curOrder[2] == 1):
            "I would like to buy:" + []
        messageText = subject + + ""
        

if __name__ == '__main__':
    app = tk.Tk()
    app.title("Order Sender")
    app.geometry("650x300")
    app.resizable(width=False, height=False)
    main_frame = MainFrame()
    app.mainloop()