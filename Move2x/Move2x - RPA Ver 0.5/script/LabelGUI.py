import tkinter as tk
from concurrent import futures
import time
import os 
from ..script.xmlScript import readXml
thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)
 
class MainFrame(tk.Frame):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = tk.Label(self, text='not running')
        self.label.pack()
        self.listbox = tk.Listbox(self)
        self.listbox.pack()
        self.buttonDymo = tk.Button(
            self, text='Dymo Print', command=self.btnDymo)
        self.buttonDymo.pack(pady=5)
        self.buttonScanner = tk.Button(
            self, text='Scan order', command=self.btnWebcam)
        self.buttonScanner.pack(pady=5)
        self.pack()
 
    def btnDymo(self):
        print('Button clicked')
        thread_pool_executor.submit(self.blocking_Dymo)
    def btnWebcam(self):
        print('Button clicked')
        thread_pool_executor.submit(self.blocking_Scanner)
 
    def set_label_text(self, text=''):
        self.label['text'] = text
 
    def listbox_insert(self, item):
        self.listbox.insert(tk.END, item)
 
    def blocking_Dymo(self):
        self.buttonScanner['state'] = 'disabled'
        self.listbox.delete(0,tk.END)
        self.after(0, self.set_label_text, 'running')
        print(os.getcwd())
        for number in range(5):
            self.after(0, self.listbox_insert, number)
            print(number)
            time.sleep(1)
        self.buttonScanner['state'] = 'normal'
        self.after(0, self.set_label_text, ' not running')

    def blocking_Scanner(self):
        self.buttonDymo['state'] = 'disabled'
        self.listbox.delete(0,tk.END)
        self.after(0, self.set_label_text, 'running')
        
        for number in range(5):
            self.after(0, self.listbox_insert, 'test ' + str(number))
            print(number)
            time.sleep(1)
        self.buttonDymo['state'] = 'normal'
        self.after(0, self.set_label_text, ' not running')    
 
if __name__ == '__main__':
    app = tk.Tk()
    main_frame = MainFrame()
    app.mainloop()