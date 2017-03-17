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


query = "UPDATE sampletable " \
        "SET name='%s',address='%s',emailid='%s'" \
        " WHERE id = %d" % (Name,Address,Emailid,Student_id)
cursor.execute(query)
db.commit()
db.close()


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h1>Successfully Modify Student Id %d .... </h1>" % (Student_id))
print ("</body>")
print ("</html>")