# create multiple Tkinter buttons using a dictionary:

import tkinter as tk
#Laver et grid vindue hvor man måske nemmere kan placere de to ekstra knapper, ved siden af tekstfeltet
#master=tk.Tk()
#master.title("grid() method")
#master.geometry("600x400")
def text_update(Words):
    text.delete(0, tk.END)
    text.insert(0, Words) 

root = tk.Tk()

text = tk.Entry(root, width=35, bg='yellow')
text.grid(row=0, column=0, columnspan=5)
#Måden man ville placere f.eks. en knap i grid vinduet
#B = tk.Button(master, text="button1")
#B.grid(row=0, column=0)




btn_dict = {}
col = 0 
words = ["Order", "Black 1 fuse L", "Timestamp", "Customer", "Product"] 
for Words in words:
    # pass each button's text to a function
    action = lambda x = Words: text_update(x)
    # create the buttons and assign to Words:button-object dict pair
    btn_dict[Words] = tk.Button(root, text=Words, command=action) 
    btn_dict[Words].grid(row=1, column=col, pady=5) 
    col += 1 

# run the GUI event loop
root.mainloop()

