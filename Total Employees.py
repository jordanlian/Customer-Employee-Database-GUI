<%
import mysql.connector

#CONNECTING TO THE MySQL SERVER
cnx = mysql.connector.connect(host='instruct.coe.neu.edu', user='3425jlian', password='havepsy', database='3425jlian')
cursor = cnx.cursor()

query1 = "SELECT count(EMP_ID) FROM EMPLOYEE;"

#query1
cursor.execute(query1)
result1 = cursor.fetchone()
result1 = "{}".format(result1[0])

#print
req.write("<b> The number of employees working for the business is " + str(result1) + "</b>")

%>
