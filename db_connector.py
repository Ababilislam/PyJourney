import mysql.connector

mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'ab',
    password="Ababil@12",
    database ="mydatabase"

)

mycursor = mydb.cursor()
# mycursor.execute("create database mydatabase")
# mycursor.execute("show databases")
# drop = "DROP table customers"
# mycursor.execute(drop)
# for database in mycursor:
#     print(database)
"""table creating"""
mycursor.execute("create table customers (id int AUTO_INCREMENT primary key, name varchar(255),address varchar(255))")
"""table showing/seeing"""
# mycursor.execute("show tables")
# for table in mycursor:
#     print(table)

# mycursor.execute(" alter table customers add column id int auto_increment primary key")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('ab', 'tangail'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

# print(mycursor.lastrowid)
