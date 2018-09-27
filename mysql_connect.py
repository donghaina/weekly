# python 链接数据库

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='reptile'
)

mycursor = mydb.cursor()

sql = "INSERT INTO imooc_lesson_list(title) VALUES (%s)"
val = ('PHP——从入门到放弃',)
# mycursor.execute("INSERT INTO imooc_lesson_list(title) VALUES ('Python——从入门到放弃')")
mycursor.execute(sql, val)

mydb.commit()

# print(mycursor.rowcount, 'record inserted')
