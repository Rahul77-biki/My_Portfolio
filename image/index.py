import mysql.connector
import pandas as pd
conn=mysql.connector.connect(host='localhost',user='root',password='200659',database="opju2")
cursor=conn.cursor()
querry="select max(mark) from student where mark < (select max(mark) from student);"
df=pd.read_sql(querry,conn)
print(df)
# cursor.execute("select * from employee;")
# for db in cursor:
#     print(db)