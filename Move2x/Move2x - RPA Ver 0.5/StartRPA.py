import tkinter as tk
from concurrent import futures
import time
import webcamController as scan
import labelController as dymo

thread_pool_executor = futures.ThreadPoolExecutor(max_workers=3)
 
class MainFrame(tk.Frame):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = tk.Label(self, text='not running')
        self.label.pack()
        self.listbox = tk.Listbox(self)
        self.listbox.pack()
        self.buttonScanner = tk.Button(self, text='Scan order', command=self.btnWebcam)
        self.buttonScanner.pack(pady=5)
        self.buttonRead = tk.Button(self, text='Scan read order', command=self.btnRead)
        self.buttonRead.pack(pady=5)
        self.buttonDymo = tk.Button(self, text='Dymo Print', command=self.btnDymo)
        self.buttonDymo.pack(pady=5)
        
      
        self.pack()
 
    def btnDymo(self):
        #print('Button clicked')
        thread_pool_executor.submit(self.blocking_Dymo)
    def btnWebcam(self):
       # print('Button clicked')
        thread_pool_executor.submit(self.blocking_Scanner)
    def btnRead(self):
       # print('Button clicked')
        thread_pool_executor.submit(self.blocking_Read)
    def set_label_text(self, text=''):
        self.label['text'] = text
 
    def listbox_insert(self, item):
        self.listbox.insert(tk.END, item)
 
    def blocking_Dymo(self):
        self.buttonDymo['state'] = 'disabled'
        self.buttonScanner['state'] = 'disabled'
        self.listbox.delete(0,tk.END)
        self.after(0, self.set_label_text, 'running')
        
        text = dymo.dymo()
        self.after(0, self.listbox_insert, text)
        text = dymo.labelMaker()
        self.after(0, self.listbox_insert, text)
        
        

        self.buttonDymo['state'] = 'normal'
        self.buttonScanner['state'] = 'normal'
        self.after(0, self.set_label_text, ' not running')

    def blocking_Scanner(self):
        self.buttonDymo['state'] = 'disabled'
        self.buttonScanner['state'] = 'disabled'
        self.listbox.delete(0,tk.END)
        self.after(0, self.set_label_text, 'running')

        text = scan.webcam()   
        self.after(0, self.listbox_insert, text)

        text = scan.takePicture()
        self.after(0, self.listbox_insert, text)
        text = scan.alignPicture()
        self.after(0, self.listbox_insert, text)
       
        self.buttonDymo['state'] = 'normal'
        self.buttonScanner['state'] = 'normal'
        self.after(0, self.set_label_text, ' not running')   
        
    def blocking_Read(self):
        self.buttonDymo['state'] = 'disabled'
        self.buttonScanner['state'] = 'disabled'
        self.listbox.delete(0,tk.END)
        self.after(0, self.set_label_text, 'running')

        text = scan.ocr()
        self.after(0, self.listbox_insert, text)
        

        self.buttonDymo['state'] = 'normal'
        self.buttonScanner['state'] = 'normal'
        self.after(0, self.set_label_text, ' not running')    
if __name__ == '__main__':
    app = tk.Tk()
    main_frame = MainFrame()
    app.geometry("200x300+1685+685")
    app.title("Start")
    app.wm_attributes("-topmost", 1)
    app.mainloop()