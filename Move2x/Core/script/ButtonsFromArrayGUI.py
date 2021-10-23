from tkinter import *
from tkinter import ttk
import tkinter as tk
import xmlScript as xml

win = Tk()

# setting the windows size
win.geometry("600x400")

# declaring string variable
# for storing name
name_var=tk.StringVar()

choosenword = ''
def xml_Save(word):
    fileToWrite = 'choosenword'
    xml.createXml('choosenword',fileToWrite)
    xml.saveToXml('choosenword',fileToWrite, word)

def xml_Read():
	return xml.readXml('ocr')

	# defining a function that will
	# get the name 
def submit():

		
	name=name_var.get()
	choosenword = name
		
	xml_Save(choosenword)

	
	name_var.set("")
	win.destroy()
		
		
	
	# creating a label for
	# name using widget Label
name_label = tk.Label(win, text = 'Username', font=('calibre',10, 'bold'))

	# creating a entry for input
	# name using widget Entry
name_entry = tk.Entry(win,textvariable = name_var, font=('calibre',10,'normal'))

	# creating a button using the widget
	# Button that will call the submit function
sub_btn=tk.Button(win,text = 'Submit', command = submit)

name_entry.pack()
sub_btn.pack()


	#Define a function to update the entry widget
def entry_update(text):
	   name_entry.delete(0,END)
	   name_entry.insert(0,text)


	#Create Multiple Buttons with different commands
button_dict={}
option = xml_Read()

for i in option:
		def func(x=i):
			return entry_update(x)

		button_dict[i]=ttk.Button(win, text=i, command= func)
		button_dict[i].pack()

	# performing an infinite loop
	# for the window to display
win.mainloop()

