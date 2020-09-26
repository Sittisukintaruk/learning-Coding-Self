import mysql.connector
from pprint import pprint


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

lista = []
for x in myresult:
    # print(x)
    lista.append(x)
    # print(type(x))
    
pprint(lista)


