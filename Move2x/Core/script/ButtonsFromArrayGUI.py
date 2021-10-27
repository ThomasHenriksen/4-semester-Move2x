from tkinter import *
from tkinter import ttk
import tkinter as tk
import xmlScript as xml
import math


win = Tk()
array_frame = tk.Frame(win)
toolbar = tk.Frame(win)

# use pack for the toolbar and array frame, grid inside the array frame
toolbar.pack(side="top", fill="x")
array_frame.pack(side="top", fill="both", expand=True)

##run_button = tk.Button(toolbar, text="Run")
##run_button.pack(side="left")

# setting the windows size
###win.geometry("600x400")

# declaring string variable
# for storing name
name_var=tk.StringVar()



    
    
def xml_Save(word, listOfWords):
	fileToWrite = listOfWords
	words = []
	if(listOfWords == 'blackList'):
		if(len(words.append(xml.readXml('blackList', 'main'))) > 0):
			words.append(xml.readXml('blackList', 'main'))
		if(len(words) == 0):
			words = word
		else:
			words.append(listOfWords)
		print(words)
	else:
		word = listOfWords
	xml.createXml(listOfWords,fileToWrite, 'main')
	if(listOfWords == 'blackList'):
		for word in words:
			print(word)
			xml.saveToXml(listOfWords,fileToWrite, word, 'main')
	else:
		xml.saveToXml(listOfWords,fileToWrite, word, 'main')

def xml_Read():
	listOfOptions = xml.readXml('ocr', 'main')
	
	try:
		blackListedWords = xml.readXml('blackList', 'main')
	except:
		xml.createXml('blackList','blackList', 'main')
		blackListedWords = xml.readXml('blackList', 'main')
	for item in listOfOptions:
		for blackListedWord in blackListedWords:
			if (item == blackListedWord):
				listOfOptions.remove(item)
	
	return xml.readXml('ocr', 'main')

	# defining a function that will
	# get the name 
def submit():

		
	name=name_var.get()
	choosenword = name
		
	xml_Save(choosenword, 'choosenword')

	
	name_var.set("")
	win.destroy()

def blacklist():

		
	name=name_var.get()
	blackList = name
		
	xml_Save(blackList, 'blackList')

	
	name_var.set("")
	win.update()


####Jeg skal lave 2 knapper her. Add to line knap og blacklist knap.
#### Add to line knappen sørger for at man kan tilføje et nyt ord til Label. Jeg bruger .get() og .set("") metoderne til dette
#### Get metoden skal ind i update metoden over delete og insert. Den skal måske wrappes i en if statement. 
word = '123'
new_word = 'new'
##print(word)
word += ' '+ new_word
print(word)	
	# creating a label for
	# name using widget Label
name_label = tk.Label(win, text = 'ProductName', font=('calibre',10, 'bold'))

	# creating a entry for input
	# name using widget Entry
name_entry = tk.Entry(win,textvariable = name_var, font=('calibre',10,'normal'))

	# creating a button using the widget
	# Button that will call the submit function
sub_btn=tk.Button(win,text = 'Submit', command = submit)
sub_btn.pack()
black_btn=tk.Button(win,text = 'BlackList', command = blacklist)
black_btn.pack()
name_entry.pack()



	#Define a function to update the entry widget
def entry_update(text):
	textold = name_var.get()
	name_entry.delete(0,END)
	if(len(textold)>0):
		name_entry.insert(0,textold+' '+text)
	else:
		name_entry.insert(0,textold+' '+text)


	#Create Multiple Buttons with different commands
button_dict={}
option = xml_Read()
array_size = len(option) #Array size = 33
column_size = 10
row_size = math.ceil(array_size/column_size)
##print(row_size)
#Jeg vil lave en funktion som f.eks. (20 * i) + j
print('Arraylist '+str (array_size))
print('RowSize '+str (row_size))


##for i in range(len(option)):
for i in range(row_size):
	for j in range(column_size):
		index = j + (i * column_size)
		def func(x=index):
			return entry_update(option[x])
		if (array_size > index):
			button = tk.Button(array_frame, text=option[index], command= func)
			button.grid(row=i, column=j, sticky="nsew")
		


	# performing an infinite loop
	# for the window to display
win.mainloop()

