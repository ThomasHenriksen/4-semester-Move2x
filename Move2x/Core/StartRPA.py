from tkinter import *
from tkinter import ttk
import tkinter as tk
import Move2xRPA as move
win = Tk()

# setting the windows size
win.geometry("200x100")

def run():
    move.main()
    #creating a Label
label = Label(win,  text="unchanged")
label.pack()
sub_btn=tk.Button(win,text = 'Run', command = run)
sub_btn.pack()
label.config(text="changed")


win.mainloop()


