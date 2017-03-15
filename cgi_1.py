#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
import mysql.connector

cgitb.enable()
# Create instance of FieldStorage


db = mysql.connector.connect(host="localhost",user ="root",password = "root@123",database="studentdetails")
cursor = db.cursor()

form = cgi.FieldStorage()
# Get data from fields
name = form.getvalue('txtname')
student_id = int(form.getvalue('txtstudentid'))
address = form.getvalue('txtaddress')
emailid = form.getvalue('txtemailid')


query1 = "INSERT INTO sampletable( StudentId,Name,Address,Emailid) VALUES('%d', '%s', '%s', '%s')"%(student_id,name ,address,emailid)
cursor.execute(query1)
db.commit()
db.close()


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello %s %d %s %s</h2>" % (name, student_id,address,emailid))
print ("</body>")
print ("</html>")

