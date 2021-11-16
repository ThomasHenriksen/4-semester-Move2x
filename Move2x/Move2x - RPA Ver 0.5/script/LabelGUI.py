import tkinter as tk
from tkinter import *
from concurrent import futures
import time
import os 
from PIL import Image, ImageTk
from pathlib import Path

thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)
 
class MainFrame(tk.Frame):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = tk.Label(self, text='not running')
        self.label.pack(side="top", pady=5, anchor="nw")
        self.listbox = tk.Listbox(self)
        self.listbox.pack(side="left", padx=20, pady=20, anchor="n")
        self.buttonDymo = tk.Button(
            self, text='Dymo Print', command=self.btnDymo)
        self.buttonDymo.pack( anchor="s", side="left", pady=5)
        self.buttonScanner = tk.Button(
            self, text='Scan order', command=self.btnWebcam)
        self.buttonScanner.pack( anchor="s",side="left", pady=5,)
        backgroundImg = ImageTk.PhotoImage(Image.open("resources\\Label.png").resize((341, 198)))
        self.lblBgImg=tk.Label(self, image = backgroundImg)
        self.lblBgImg.image = backgroundImg
        self.lblBgImg.pack(side="top")
        self.lblCustomer = tk.Label(self, bg="gray", text='test')
        self.lblCustomer.pack(side="top", pady=20, padx= 50)
        self.lblTime = tk.Label(self, bg="gray", text='test på hvor meget der kan være af text i et label')
        self.lblTime.place(relx=0.5, rely=0.5, anchor='s')
        self.lblProduct = tk.Label(self, text='Some Plain Text', compound='center')
        self.lblProduct.pack(pady=59, anchor="n")
        self.pack(fill='none', expand=1)
 
    def btnDymo(self):
        
        thread_pool_executor.submit(self.blocking_Dymo)
    def btnWebcam(self):
        
        thread_pool_executor.submit(self.blocking_Scanner)
 
    def set_label_text(self, text=''):
        self.label['text'] = text
 
    def listbox_insert(self, item):
        self.listbox.insert(tk.END, item)
 
    def blocking_Dymo(self):
        self.buttonScanner['state'] = 'disabled'
        self.listbox.delete(0,tk.END)
        self.after(0, self.set_label_text, 'running')
        
        for number in range(5):
            self.after(0, self.listbox_insert, number)
            
            time.sleep(1)
        self.buttonScanner['state'] = 'normal'
        self.after(0, self.set_label_text, ' not running')

    def blocking_Scanner(self):
        self.buttonDymo['state'] = 'disabled'
        self.listbox.delete(0,tk.END)
        self.after(0, self.set_label_text, 'running')
        
        for number in range(5):
            self.after(0, self.listbox_insert, 'test ' + str(number))
            
            time.sleep(1)
        self.buttonDymo['state'] = 'normal'
        self.after(0, self.set_label_text, ' not running')    
 
if __name__ == '__main__':
    app = tk.Tk()
    app.geometry("650x350")
    main_frame = MainFrame()
    app.mainloop()