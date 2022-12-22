import psycopg2

conn = psycopg2.connect(database="test", user = "cliu", password = "Qq..1234", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

cur.execute("select * from person;")
rows = cur.fetchall()

'''
for row in rows:
   print ("ID = ", row[0])
   print ("NAME = ", row[1]+" "+row[2])
   print ("GENDER = ", row[3])
   print ("date_of_birth = ", row[4])
   print ("email = ", row[5], "\n")
'''

print(rows[0])

conn.close()
