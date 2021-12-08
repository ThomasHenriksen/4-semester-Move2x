import cgi, cgitb
import sendEmailController as sendEmail
import ProductAccessMysql as ProductAccess
import generateEmailDetails
cgitb.enable()
def getOrderFromDatabase(self):
        orderlist = self.listOfOrders
        self.listbox.delete(0,tk.END)
        
        for order in orderlist:
            self.after(0, self.listbox_insert,order[0] +' - '+ str(order[1]) +' - '+ str(order[2]) +' - '+ order[3] +' - '+ order[4] )
        
        
        return orderlist



print("Content-type: text/html\n\n ")
print("<html><head><title>Thomas tester</title></head>")
print("<body><h1>Thomas tester")
for b in orderlist:
    print("<h2>"+b+"</h2>")
print("</h1></body>")
print("</html> ")
