<%
import mysql.connector
#CONNECTING TO THE MySQL SERVER
cnx = mysql.connector.connect(user='3425jlian',password='havepsy', host='instruct.coe.neu.edu', database='3425jlian')
cursor = cnx.cursor()

#Get product records
query="SELECT MAN_ID, MAN_FNAME, MAN_LNAME, MAN_DOB, MAN_HIRE, MAN_GENDER, EMP_ID FROM MANAGER;"
cursor.execute(query)

#Output results to Web page
req.write("<h3>Manager Report</h3>")
req.write("<table border='2'>")
req.write("<tr>")
req.write("<th>Manager ID</th>")
req.write("<th>Mananger First Name</th>")
req.write("<th>Manager Last Name</th>")
req.write("<th>Manager Date of Birth</th>")
req.write("<th>Manager Date of Hire</th>")
req.write("<th>Manager Gender</th>")
req.write("<th>Employee ID</th>")
req.write("</tr>")

#output results to the Web page
for (MAN_ID, MAN_FNAME, MAN_LNAME, MAN_DOB, MAN_HIRE, MAN_GENDER, EMP_ID) in cursor:
	req.write("<tr>")
	req.write ("<td> {} </td>".format(MAN_ID))
	req.write ("<td> {} </td>".format(MAN_FNAME))
	req.write ("<td> {} </td>".format(MAN_LNAME))
	req.write ("<td> {} </td>".format(MAN_DOB))
	req.write ("<td> {} </td>".format(MAN_HIRE))
	req.write ("<td> {} </td>".format(MAN_GENDER))
	req.write ("<td> {} </td>".format(EMP_ID))
req.write("</tr>")
req.write("</table>")
cursor.close()
cnx.close()
%>
