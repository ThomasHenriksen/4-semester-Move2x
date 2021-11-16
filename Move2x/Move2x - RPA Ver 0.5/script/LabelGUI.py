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
        self.label.pack(side="top", pady=5, padx=5, anchor="w")
        self.listbox = tk.Listbox(self)
        self.listbox.pack(side="left", padx=5, pady=5, anchor="nw")
        self.buttonDymo = tk.Button(
            self, text='Dymo Print', command=self.btnDymo)
        self.buttonDymo.place(y=230, x=45, anchor='s')
        self.buttonScanner = tk.Button(
            self, text='Scan order', command=self.btnWebcam)
        self.buttonScanner.place(y=260, x=45, anchor='s')
        backgroundImg = ImageTk.PhotoImage(Image.open("resources\\Label.png").resize((341, 198)))
        self.lblBgImg=tk.Label(self, image = backgroundImg)
        self.lblBgImg.image = backgroundImg
        self.lblBgImg.pack(side="top")
        self.lblCustomer = tk.Label(self, bg="white", text='Customer')
        self.lblCustomer.place(y=110, x=440, anchor='s') # y=120, x=470, anchor='s'
        self.lblTime = tk.Label(self, bg="white", text='Product')
        self.lblTime.place(y=141, x=471, anchor='s')
        self.lblProduct = tk.Label(self, bg="white", text='time', compound='center')
        self.lblProduct.place(y=110, x=511, anchor='s')
        self.pack(fill=BOTH, expand=1)
 
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