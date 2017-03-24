import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'test',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor1 = cnx.cursor()
cursor1.execute("truncate table student")
cursor1.execute("truncate table student")
cursor1.execute("INSERT INTO student VALUES (11,'abcd')")
cnx.commit()
cursor1.execute("select * from student")

#cursor1.execute("select * from student")
print cursor1.fetchall()


cnx.close()