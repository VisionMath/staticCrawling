import requests
from bs4 import BeautifulSoup as bs
import requests as req
import regex as re
import numpy as np
import pandas as pd

base = 'https://movie.naver.com'
res = req.get('https://movie.naver.com/movie/running/current.naver')
soup = bs(res.content, 'html.parser')

li_list = soup.select('dl.lst_dsc')
temp_list=[]

for li in li_list:
    score = li.select_one('span.num').text

    hr = li.select_one('dt.tit > a')
    res = req.get(base + hr['href'])
    soup = bs(res.content, 'html.parser')

    title = soup.select('h3.h_movie > a')[0].text
    g = soup.select_one('a[href*=grade]')
    grade = g.text if g else '관람불가'

    gen = soup.select_one("a[href*=genre]")
    genre = gen.text if gen else ''

    runtime = li.find(text=re.compile('\d[분]'))
    op = soup.select("a[href*=open]")
    open_date = op[0].text + op[1].text

    info = soup.select('dl.info_spec > dd')

    di = info[1].findAll('a')
    di_str = []
    for i in di:
        di_str.append(i.text)
    director = ', '.join(di_str)

    step3 = soup.select_one('dt.step3')
    if step3:
        ac = info[2].findAll('a')
        ac_str = []
        for i in ac:
            ac_str.append(i.text)
        ac_str.remove('더보기')
        actor = ', '.join(ac_str)
    else:
        actor = None

    st = soup.find('p', {"class": "con_tx"})
    sto = st.findAll(text=True) if st else []
    story=''
    for s in sto:
        story+=s.text.strip()

    gr = soup.select('div.mv_info > div.viewing_graph > div > div.bar_graph > div> strong.graph_percent')
    pe = []
    for i in gr:
        pe.append(i.text)
    percent = ', '.join(pe)

    image_link=soup.select_one('div.mv_info_area > div.poster > a > img')['src']
    # image_name=image_link.split('/')[4].replace('_JPEG', '')+'.jpg'
    #
    # res=req.get(image_link)
    # if res.status_code==200:
    #     with open('images/'+image_name, 'wb') as f:
    #         f.write(res.content)

    temp_list.append((title, grade, score, genre, runtime, open_date, director, actor, story, percent, image_link))

df=pd.DataFrame(temp_list, columns=['title', 'grade', 'score', 'genre', 'runtime', 'open_date', 'director', 'actor', 'story', 'percent', 'image_link'])
print(df)
