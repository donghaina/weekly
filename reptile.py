# coding = utf-8

import urllib.request
import ssl
import urllib.error
from bs4 import BeautifulSoup
import mysql.connector

context = ssl._create_unverified_context()

lesson_list_string = []


def getLessonList(page):
    response = urllib.request.urlopen('https://www.imooc.com/course/list?c=fe&page=' + str(page), context=context)

    html_content = response.read().decode('utf-8')

    soup = BeautifulSoup(html_content, 'lxml', from_encoding='uft-8')

    lesson_list = soup.select('.course-card-content .course-card-name')

    for lesson in lesson_list:
        lesson_list_string.append(lesson.string)
        # print(image.string)


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='reptile'
)

mycursor = mydb.cursor()

for page in range(1, 9):
    getLessonList(page)

for index in range(len(lesson_list_string)):
    # print(index, '-', lesson_list_string[index])
    sql = "INSERT INTO imooc_lesson_list(title) VALUES (%s)"
    val = (str(lesson_list_string[index]),)
    mycursor.execute(sql, val)

mydb.commit()
