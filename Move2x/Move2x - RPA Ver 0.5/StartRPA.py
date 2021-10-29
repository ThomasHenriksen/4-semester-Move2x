from tkinter import *
from tkinter import ttk
import tkinter as tk
import Move2xRPA as move
import webcamController as WC
import labelController as LB

win = Tk()

# setting the windows size
win.geometry("200x100")

def run():
    label.config(text="is running")
    move.main()
    label.config(text="is not running")
    #creating a Label
label = Label(win,  text="is not running")
label.pack()
sub_btn=tk.Button(win,text = 'Run', command = run)
sub_btn.pack()



win.mainloop()


