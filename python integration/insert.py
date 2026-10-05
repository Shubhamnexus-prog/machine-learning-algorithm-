import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='1234',database='internshipdb')

mycursor = conn.cursor()

sql = 'insert into student (name,branch,id,) values(%s,%s,%s)'

val = [('rohit','cse','56'),('kholi','IT','78'),('rahul','me','80')]

mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')

# Check records
mycursor.execute("SELECT * FROM student")

print("\nRecords in student table:")

for record in mycursor.fetchall():
    print(record)

conn.close()
