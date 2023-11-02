import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user = "ab",
    password = "Ababil@12",
    database = "mydatabase"
)
mycursor = mydb.cursor()
"""seeing the data table"""
# mycursor.execute("select * from customers")
# for i in mycursor:
#     print(i)

# sql_query = "select * from customers limit 5 offset 3"
# adr = ("Yellow garden 2",)
# mycursor.execute(sql_query,adr)
mycursor.execute(sql_query)
my_result = mycursor.fetchall()
for x in my_result:
    print(x)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

sql_query = ("select user.name as user, product.name as favorite\
             from users \
             inner join products on user.fav = product.id")

mycursor.execute(sql_query)
myresult =mycursor.fetchall()
for x in myresult:
    print(x)
