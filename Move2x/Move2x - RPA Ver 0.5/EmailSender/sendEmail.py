# Libs
import smtplib
from email.message import EmailMessage
msg = EmailMessage()

def sendEmail(subject, message):
        # The sender's E-mail
        sender = "move2ordre@gmail.com"
        # The sender's Password
        pWord = "nfoyyuadbnrxzbic"
        # The receiver's E-mail
        recepient ="move2produktion@gmail.com"
        # The subject of the E-mail
        sub = subject
        # The "body" of the E-mail
        #message = listbox.get(listbox.curselection())

        # The predefined text for the email
        msg.set_content(message)

        msg['Subject'] = sub
        msg['From'] = sender
        msg['To'] = recepient

        # smtp for the gmail server + the port number
        server = smtplib.SMTP(host='smtp.gmail.com' , port=587)
        # encrypts the message with Transport Layer Security
        server.starttls()
        # Gets the login details
        server.login(sender, pWord)
        # Sends the message
        server.send_message(msg)
        # Quits the session
        server.quit()
        print("Email sent successfully!")
        # After sending the email, deletes the subject, sender and recepient, so a new mail can be sent
        del msg['Subject']
        del msg['From']
        del msg['To']