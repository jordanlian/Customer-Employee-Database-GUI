<%
import mysql.connector

#CONNECTING TO THE MySQL SERVER
cnx = mysql.connector.connect(host='instruct.coe.neu.edu', user='3425jlian', password='havepsy', database='3425jlian')
cursor = cnx.cursor()

query1 = "SELECT min(PROD_PRICE) FROM PRODUCT;"
query2 = "SELECT max(PROD_PRICE) FROM PRODUCT;"

#query1
cursor.execute(query1)
result1 = cursor.fetchone()
result1 = "{}".format(result1[0])

#query2
cursor.execute(query2)
result2 = cursor.fetchone()
result2 = "{}".format(result2[0])

#print
req.write("<b> The most cheapest product offered is $" + str(result1) + "</b></br>")
req.write("<b> The most expensive product offered is $" + str(result2) + "</b></br>")

%>
