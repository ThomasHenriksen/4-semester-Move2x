import tkinter as tk
from tkinter import *
from concurrent import futures
import time
import os 
from PIL import Image, ImageTk
import sendEmail
thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)
 
class MainFrame(tk.Frame):
 
    def __init__(self, *args, **kwargs):
        btnY = 225

        super().__init__(*args, **kwargs)

        

        sb = Scrollbar(self, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)

        self.listbox = tk.Listbox(self)
        self.listbox.bind('<<ListboxSelect>>')
        self.listbox.configure(yscrollcommand=sb.set)

        sb.config(command=self.listbox.yview)
        self.listbox.pack(side="left", padx=0, pady=0, anchor="nw", fill=tk.X,expand=True)


        self.btnSend = tk.Button(self, text='Send', command=self.btnSend)
        self.btnSend.place(y=btnY, x=100, anchor='s')
        self.pack(fill=BOTH, expand=1)
        
        

    def btnSend(self):
        thread_pool_executor.submit(self.blocking_Send)


    def listbox_insert(self, item):
        self.listbox.insert(tk.END, item)


    def blocking_Send(self):
        sendEmail.sendEmail("hey", "med dig")
    

if __name__ == '__main__':
    app = tk.Tk()
    app.title("Move2x")
    app.geometry("650x300")
    app.resizable(width=False, height=False)
    main_frame = MainFrame()
    app.mainloop()


