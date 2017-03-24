import mysql.connector
import time
import datetime

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print timestamp
config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'test',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor1 = cnx.cursor()
#cursor1.execute("truncate table student")
#cursor1.execute("truncate table student")
#cursor1.execute("INSERT INTO student VALUES (11,'abcd'," + timestamp +")")
#sql = """ INSERT INTO student (id, name, sdate) VALUES (%s, %s, CURRENT_TIMESTAMP) """
#cursor1.execute(sql,(4, 'abcd'))
cursor1.execute('INSERT INTO student (id, name, sdate) VALUES (%s, %s, %s)', (4, 'abcd', timestamp))

cnx.commit()
#cursor1.execute("select * from student")

#cursor1.execute("select * from student")
#print cursor1.fetchall()


cnx.close()