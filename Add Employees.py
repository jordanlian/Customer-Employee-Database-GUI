<%
import mysql.connector

#CONNECTING TO THE MySQL SERVER
cnx = mysql.connector.connect(host='instruct.coe.neu.edu', user='3425jlian', password='havepsy', database='3425jlian')
cursor = cnx.cursor()

#get all name/value pairs, one by one, from web page
EMP_FNAME = form.get("EMP_FNAME", "Error in first name")
EMP_LNAME = form.get("EMP_LNAME", "Error in last name")
EMP_DOB = form.get("EMP_DOB", "Error in date of birth")
EMP_HIRE = form.get("EMP_HIRE", "Error in date of hire")
EMP_GENDER = form.get("EMP_GENDER", "Error in gender")

#convert to strings
EMP_FNAME = str(EMP_FNAME)
EMP_LNAME = str(EMP_LNAME)
EMP_DOB = str(EMP_DOB)
EMP_HIRE = str(EMP_HIRE)
EMP_GENDER = str(EMP_GENDER)

query = "SELECT max(EMP_ID) FROM EMPLOYEE;"
cursor.execute(query)

result = cursor.fetchone() #there is fetchall() function also
newPK = "{}".format(result[0] + 1)

insert1="INSERT INTO EMPLOYEE(EMP_ID, EMP_FNAME, EMP_LNAME, EMP_DOB, EMP_HIRE, EMP_GENDER) values (%s, %s, %s, %s, %s, %s)"
data = (newPK, EMP_FNAME, EMP_LNAME, EMP_DOB, EMP_HIRE, EMP_GENDER)
cursor.execute(insert1, data)
cnx.commit()
cursor.close()
cnx.close() 
%>
