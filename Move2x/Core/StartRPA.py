from tkinter import *
from tkinter import ttk
import tkinter as tk
import Move2xRPA as move
win = Tk()

# setting the windows size
win.geometry("200x100")

def submit():
    move.main()

sub_btn=tk.Button(win,text = 'Submit', command = submit)
sub_btn.pack()

win.mainloop()


