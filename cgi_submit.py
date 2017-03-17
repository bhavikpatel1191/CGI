#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
import mysql.connector

cgitb.enable()
# Create instance of FieldStorage


db = mysql.connector.connect(host="localhost",user ="root",password = "root",database="studentdetails")
cursor = db.cursor()

form = cgi.FieldStorage()
# Get data from fields
Name = form.getvalue('name')
Student_id = int(form.getvalue('studentid'))
Address = form.getvalue('address')
Emailid = form.getvalue('emailid')


query = "INSERT INTO sampletable(id,name,address,emailid) VALUES('%d',' %s','%s', '%s')"%(Student_id,Name,Address,Emailid)
cursor.execute(query)
db.commit()
db.close()


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Successfully Registation...</h2>")
print ("</html>")

