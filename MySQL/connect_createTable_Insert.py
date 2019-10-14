import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="demodemo",
  database='demo',
  auth_plugin='mysql_native_password'
)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS MyTable (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(30) NOT NULL, lastname VARCHAR(30) NOT NULL, email VARCHAR(50))")

sql = "INSERT INTO MyTable (firstname, lastname, email) VALUES (%s, %s, %s)"
val = ("John", "Highway 21", "lol@fbi.com")
mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("SELECT * FROM MyTable")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
