<%
import mysql.connector
#CONNECTING TO THE MySQL SERVER
cnx = mysql.connector.connect(host='instruct.coe.neu.edu', user='3425jlian', password='havepsy', database='3425jlian')
cursor = cnx.cursor()
#get form input
#get all name/value pairs, one by one, from web page
PROD_NAME = form.get("PROD_NAME", "Error in product name")
PROD_PRICE = form.get("PROD_PRICE", "Error in product price")

#convert to strings
PROD_NAME = str(PROD_NAME)
PROD_PRICE = str(PROD_PRICE)

query = "SELECT max(PROD_CODE) FROM PRODUCT;"
cursor.execute(query)

result = cursor.fetchone() #there is fetchall() function also
newPK = "{}".format(result[0] + 1)

insert1="INSERT INTO PRODUCT(PROD_CODE, PROD_NAME, PROD_PRICE) values (%s, %s, %s)"
data = (newPK, PROD_NAME, PROD_PRICE)
cursor.execute(insert1, data)
cnx.commit()
cursor.close()
cnx.close() 
%>
