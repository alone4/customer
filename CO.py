import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kali",
    database="pets"
)

mycursor=mydb.cursor()
print("test")