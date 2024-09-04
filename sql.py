import sqlite3

#Connect to sqlite3
connection=sqlite3.connect("student.db")

#Create a cursor object to insert ,retrieve ,create table
cursor=connection.cursor()

table_info="""
Create table STUDENT(
Name Varchar(25),
Class varchar(25),
Section varchar(25),
Marks INT
)

"""

#creating a table
cursor.execute(table_info)

# inserting data
cursor.execute("""Insert into Student values('Devesh','Machine Learning','A',80)""")
cursor.execute("""Insert into Student values('Devang','Data Analytics','B',91)""")
cursor.execute("""Insert into Student values('Rohit','Data Science','A',91)""")
cursor.execute("""Insert into Student values('Vinit','CA','B',84)""")
cursor.execute("""Insert into Student values('Shubhankar','Data Engineer','A',92.63)""")
cursor.execute("""Insert into Student values('Raj','Data Science','B',90)""")
cursor.execute("""Insert into Student values('Yash','Deep Learning','A',86)""")
cursor.execute("""Insert into Student values('Rishi','Web Developer','B',89)""")
cursor.execute("""Insert into Student values('Aditya','Java Developer','A',88.6549)""")

#Displaying all the records
print("The data is")
data=cursor.execute("""Select * from Student""")

for row in data:
    print(row)

connection.commit()
connection.close()



