from tkinter import *
from tkinter import ttk
import tkinter as tk
import xmlScript as xml
import math


WindowRun = True

while(WindowRun == True):
			# performing an infinite loop
		# for the window to display
	def xml_Save(wordXml, listOfWords):
		fileToWrite = listOfWords
		words = xml.readXml('blackList', 'main')
		if(listOfWords == 'blackList'):
			words.append(wordXml)
			

		xml.createXml(listOfWords,fileToWrite, 'main')
		if(listOfWords == 'blackList'):
			for word in words:
				
				xml.saveToXml(listOfWords,fileToWrite, word, 'main')
		else:
			xml.saveToXml(listOfWords,fileToWrite, wordXml, 'main')

	def xml_Read():
		listOfOptions = xml.readXml('ocr', 'main')
	
		try:
			blackListedWords = xml.readXml('blackList', 'main')
		except:
			xml.createXml('blackList','blackList', 'main')
			blackListedWords = xml.readXml('blackList', 'main')

		index = 0
		OptionsCheck = len(listOfOptions)
		blacklistCheck = len(blackListedWords)
		goodList = []
		while (index <OptionsCheck):
			fundt = False
			i = 0
			while(i < blacklistCheck):
				if(listOfOptions[index] == blackListedWords[i]):
					fundt = True
				i+= 1
			if(fundt == False):
				goodList.append(listOfOptions[index])
			index +=1
		return goodList

		# defining a function that will
		# get the name 
	def submit():

		
		name=name_var.get()
		choosenword = name
		
		xml_Save(choosenword, 'choosenword')
		
		WindowRun = False
		
		name_var.set("")
		
		quit()
		
			

	def blacklist():
		name=name_var.get()
		blackList = name

		xml_Save(blackList, 'blackList')
		
		name_var.set("")
		win.destroy()
	#Define a function to update the entry widget
	def entry_update(text):
		textold = name_var.get()
		name_entry.delete(0,END)
		if(len(textold)>0):
			name_entry.insert(0,textold+' '+text)
		else:
			name_entry.insert(0,text)
	win = Tk()
	array_frame = tk.Frame(win)
	toolbar = tk.Frame(win)

	# use pack for the toolbar and array frame, grid inside the array frame
	toolbar.pack(side="top", fill="x")
	array_frame.pack(side="top", fill="both", expand=True)

	name_var=tk.StringVar()
	name_label = tk.Label(win, text = 'ProductName', font=('calibre',10, 'bold'))
	name_entry = tk.Entry(win,textvariable = name_var, font=('calibre',10,'normal'))
	sub_btn=tk.Button(win,text = 'Submit', command = submit)
	sub_btn.pack()
	black_btn=tk.Button(win,text = 'BlackList', command = blacklist)
	black_btn.pack()
	name_entry.pack()

	option = xml_Read()
	array_size = len(option) #Array size = 33
	column_size = 10
	row_size = math.ceil(array_size/column_size)
	
	##for i in range(len(option)):
	for i in range(row_size):
		for j in range(column_size):
			index = j + (i * column_size)
			def func(x=index):
				return entry_update(option[x])
			if (array_size > index):
				button = tk.Button(array_frame, text=option[index], command= func)
				button.grid(row=i, column=j, sticky="nsew")

	win.mainloop()
