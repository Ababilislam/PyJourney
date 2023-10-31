import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='ab',
    password="Ababil@12",
    database="mydatabase"
)
mycursor = mydb.cursor()

query = "select * from customers order by name desc "
# adr = ("tangail", )
mycursor.execute(query)

myresult = mycursor.fetchall()

for data in myresult:
    print(data)
