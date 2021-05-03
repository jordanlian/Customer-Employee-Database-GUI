<%
import mysql.connector

#CONNECTING TO THE MySQL SERVER
cnx = mysql.connector.connect(host='instruct.coe.neu.edu', user='3425jlian', password='havepsy', database='3425jlian')
cursor = cnx.cursor()

#get all name/value pairs, one by one, from web page
CUS_FNAME = form.get("CUS_FNAME", "Error in first name")
CUS_LNAME = form.get("CUS_LNAME", "Error in last name")
CUS_GENDER = form.get("CUS_GENDER", "Error in gender")
CUS_DOB = form.get("CUS_DOB", "Error in date of hire")


#convert to strings
CUS_FNAME = str(CUS_FNAME)
CUS_LNAME = str(CUS_LNAME)
CUS_GENDER = str(CUS_GENDER)
CUS_DOB = str(CUS_DOB)

query = "SELECT max(CUS_ID) FROM CUSTOMER;"
cursor.execute(query)

result = cursor.fetchone() #there is fetchall() function also
newPK = "{}".format(result[0] + 1)

insert1="INSERT INTO CUSTOMER(CUS_ID, CUS_FNAME, CUS_LNAME, CUS_GENDER, CUS_DOB) values (%s, %s, %s, %s, %s)"
data = (newPK, CUS_FNAME, CUS_LNAME, CUS_GENDER, CUS_DOB)
cursor.execute(insert1, data)
cnx.commit()
cursor.close()
cnx.close() 
%>
