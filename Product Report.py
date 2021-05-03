<%
import mysql.connector
#CONNECTING TO THE MySQL SERVER
cnx = mysql.connector.connect(user='3425jlian',password='havepsy', host='instruct.coe.neu.edu', database='3425jlian')
cursor = cnx.cursor()

#Get product records
query="SELECT PROD_CODE, PROD_NAME, PROD_PRICE FROM PRODUCT;"
cursor.execute(query)

#Output results to Web page
req.write("<h3>Product Report</h3>")
req.write("<table border='2'>")
req.write("<tr>")
req.write("<th>Product Code</th>")
req.write("<th>Product Name</th>")
req.write("<th>Product Price</th>")
req.write("</tr>")

#output results to the Web page
for (PROD_CODE, PROD_NAME, PROD_PRICE) in cursor:
	req.write("<tr>")
	req.write ("<td> {} </td>".format(PROD_CODE))
	req.write ("<td> {} </td>".format(PROD_NAME))
	req.write ("<td> {} </td>".format(PROD_PRICE))
req.write("</tr>")
req.write("</table>")
cursor.close()
cnx.close()
%>
