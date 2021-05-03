<html>
<head>
<title>Feedback</title>
</head>
<body>
<%
#get all name/value pairs, one by one, from web page
fName = form.get("fName", "Error in first name")
mName = form.get("mName", "Error in middle name")
lName = form.get("lName", "Error in last name")
year = form.get("year", "Error in year")
tab = form.get("tab", "Error in tab")
AbeZeid = form.get("AbeZeid", "Error in Zeid")
feedback = form.get("feedback", "Error in feedback")

req.write("<h2>Feedback</h2>")
req.write("First Name: " + fName + "<br/>")
req.write("Middle Name: " + mName + "<br/>")
req.write("Last Name: " + lName + "<br/>")
req.write("year: " + year + "<br/>")
req.write("Tab(s): " + tab + "<br/>")
req.write("Zeid: " + AbeZeid + "<br/>")
req.write("Feedback: " + feedback + "<br/>")
%>
</body>
</html>
