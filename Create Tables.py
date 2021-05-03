<html>
<head>
<title>Final Project Tables</title>
</head>
<body>
<%
import mysql.connector
#connect to the mysql server
cnx=mysql.connector.connect(host='instruct.coe.neu.edu', user='3425jlian', password='havepsy', database='3425jlian')
cursor=cnx.cursor()

#CUSTOMER table
CUSTOMER="CREATE TABLE IF NOT EXISTS CUSTOMER(CUS_ID int(2) not null, CUS_FNAME varchar(20), CUS_LNAME varchar(20), CUS_GENDER varchar(2), CUS_DOB date, primary key(CUS_ID));"
cursor.execute(CUSTOMER)

#EMPLOYEE table
EMPLOYEE="CREATE TABLE IF NOT EXISTS EMPLOYEE(EMP_ID int(2) not null, EMP_FNAME varchar(20), EMP_LNAME varchar(20), EMP_DOB date, EMP_HIRE date, EMP_GENDER varchar(2), primary key(EMP_ID));"
cursor.execute(EMPLOYEE)

#PRODUCT table
PRODUCT="CREATE TABLE IF NOT EXISTS PRODUCT(PROD_CODE int(2) not null, PROD_NAME varchar(30), PROD_PRICE decimal(6, 2), primary key(PROD_CODE));"
cursor.execute(PRODUCT)

#NORTHEASTERN SCHOOL table
NORTHEASTERN_SCHOOL="CREATE TABLE IF NOT EXISTS NORTHEASTERN_SCHOOL(SCH_ID varchar(4) not null, SCH_NAME varchar(50), primary key(SCH_ID));"
cursor.execute(NORTHEASTERN_SCHOOL)

#LINE table 
LINE="CREATE TABLE IF NOT EXISTS LINE(ORD_NUM int(2) not null, ORD_DATE date, PROD_CODE int(2), PROD_PRICE decimal(6, 2), ORD_UNITS int(2), ORD_SUBTOTAL decimal(6, 2), ORD_TAX decimal(6, 2), ORD_TOT decimal(6, 2), primary key(ORD_NUM), foreign key(PROD_CODE) references PRODUCT(PROD_CODE));"
cursor.execute(LINE)

#MANAGER table
MANAGER="CREATE TABLE IF NOT EXISTS MANAGER(MAN_ID int(2) not null, MAN_FNAME varchar(20), MAN_LNAME varchar(20), MAN_DOB date, MAN_HIRE date, MAN_GENDER varchar(2), EMP_ID int(2), primary key(MAN_ID), foreign key(EMP_ID) references EMPLOYEE(EMP_ID));"
cursor.execute(MANAGER)

#ORDERS table
ORDERS="CREATE TABLE IF NOT EXISTS ORDERS(ORD_NUM int(2), CUS_ID int(2), foreign key(ORD_NUM) references LINE(ORD_NUM), foreign key(CUS_ID) references CUSTOMER(CUS_ID));"
cursor.execute(ORDERS)

#EMPLOYEE SCHOOL table
EMPLOYEE_SCHOOL="CREATE TABLE IF NOT EXISTS EMPLOYEE_SCHOOL(EMP_ID int(2), SCH_ID varchar(4), foreign key(EMP_ID) references EMPLOYEE(EMP_ID), foreign key(SCH_ID) references NORTHEASTERN_SCHOOL(SCH_ID));"
cursor.execute(EMPLOYEE_SCHOOL)

%>
</body>
</html>
