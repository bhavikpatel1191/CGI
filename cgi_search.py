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
Student_id = int(form.getvalue('studentid'))
Address = form.getvalue('address')
Emailid = form.getvalue('emailid')


query = "SELECT * FROM sampletable WHERE id = %d"% (Student_id)
cursor.execute(query)
row = cursor.fetchone()
print (row[0], row[1],row[2],row[3])
db.commit()
db.close()

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print("Name:<input type=text value='%s'>"% row[1])
print("StudentId:<input type=text value='%d'>"% row[0])
print("Address:<input type=text value='%s'>"%row[2])
print("Emailid:<input type=text value='%s'>"%row[3])
print("<input type=submit value=submit/>")
print("<input type=submit value=delete  formaction=cgi-bin/cgi_delete.py/>")
print("<input type=submit value=modify formaction=cgi-bin/cgi_modify.py/>")
print("<input type=submit value=search formaction=cgi-bin/cgi_search.py/>")
print ("</html>")

