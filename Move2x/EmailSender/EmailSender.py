# Libs
from tkinter import *
import tkinter.font as font
from tkinter import scrolledtext
import smtplib
from email.message import EmailMessage
msg = EmailMessage()

# tkinter for the geometry, title and font
app = Tk()
app.geometry('550x400')
app.title("Simple E-mail sender")
myFont = font.Font(size=16)
large_font = ('Verdana',16)

# StringVar for editing the widget text
account = StringVar()
password = StringVar()
receiver = StringVar()
subject = StringVar()
msgbody = StringVar()

# smtp for the gmail server + the port number
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.starttls()

# Method for sending the mail
def sendemail():
    # The sender's E-mail
    sender = "move2ordre@gmail.com"
    # The sender's Password
    pWord = "nfoyyuadbnrxzbic"
    # The receiver's E-mail
    recepient ="move2produktion@gmail.com"
    
    # The subject of the E-mail
    sub = subject.get()
    print(sub)
    # The "body" of the E-mail
    message = list_Area.get(list_Area.curselection())
    print(message)
    # The predefined text for the email

    # message = 
    # Dear Smarter Production inc.
    # l would like to ordre:

    #list_Area.get(list_Area.curselection())
    
    # Best regards 
    # Name Surname (Customer number)

    msg.set_content(message)

    msg['Subject'] = sub
    msg['From'] = sender
    msg['To'] = recepient

    # Send the message via port 465.
    server = smtplib.SMTP_SSL('smtp.gmail.com' , 465)
    server.login(sender, pWord)
    server.send_message(msg)
    server.quit()

# All Labels in the program

# Label for the banner in the middel, that seperates the login credentials with the details for the email they are sending
Label(app, text = "================E-mail Content=================", font = "Verdana 10 bold").grid(row = 3, column = 0, columnspan = 2,padx = 10, pady = 10)

# Label and text field for typing the adress that the E-mail needs to go to
lbl_To = Label(app, text = "To", justify = LEFT, padx = 30, font = "Verdana 10 bold")
lbl_To.grid(row = 4, column = 0)
receiver_Entry = Entry(app,  width = 30, font=large_font, textvariable = receiver)
receiver_Entry.grid(row = 4, column = 1)

# Label and text field for typing the subject to the E-mail
lbl_Subject = Label(app, text = "Subject", justify = LEFT, padx = 10, font = "Verdana 10 bold")
lbl_Subject.grid(row = 5, column = 0)
subject_Entry = Entry(app,  width = 30, font=large_font, textvariable = subject)
subject_Entry.grid(row = 5, column = 1)

# List area for the messages also known as the message_body
list_Area = Listbox(app, width=50, height=10, font=("Times New Roman",15))
list_Area.grid(row = 6, columnspan = 2, pady=10, padx = 10)

list_Area.insert(1,"00:55 - 10017 - 3 - black 1 fuse r (1213)")
list_Area.insert(2,"01:00 - 10018 - 1 - blue phone (6002)")
list_Area.insert(3,"01:10 - 10019 - 1 - white phone (6001)")
list_Area.insert(4,"01:10 - 10019 - 1 - blue phone (6002)")

# The send button
send_Button = Button(app, text = "Send",  relief='groove', width  = 10, command = sendemail)
send_Button.grid(row = 7, column = 0)


app.mainloop()
