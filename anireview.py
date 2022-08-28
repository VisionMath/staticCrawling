import pymysql
import pandas as pd

df=pd.read_csv('data/anireview.csv')
review_list = df.values.tolist()
# print(df)
# print(review_list)

def insert_movie(review_list):
    conn=pymysql.connect(host='35.230.21.125', user='root', password='vm28283', db='AniFamily', charset='utf8')
    cursor=conn.cursor()
    sql='''insert into story(title, content, link) values(%s, %s, %s)'''
    cursor.executemany(sql, review_list)
    conn.commit()
    conn.close()

def select_all():
    conn=pymysql.connect(host='35.230.21.125', user='root', password='vm28283', db='AniFamily', charset='utf8')
    cursor=conn.cursor()
    sql='select convert(content using utf8mb4) from story'
    cursor.execute(sql)
    for movie in cursor:

        print(movie)
    conn.commit()
    conn.close()

# insert_movie(review_list)
select_all()