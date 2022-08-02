from bs4 import BeautifulSoup as bs
import requests as req
import regex as re

base = 'https://movie.naver.com'
res = req.get('https://movie.naver.com/movie/running/current.naver')
soup = bs(res.content, 'html.parser')

li_list = soup.select('dl.lst_dsc')

for li in li_list:
    score = li.select_one('span.num').text

    hr = li.select_one('dt.tit > a')
    res = req.get(base + hr['href'])
    soup = bs(res.content, 'lxml')

    title = soup.select('h3.h_movie > a')[0].text
    g = soup.select_one("a[href*=grade]")
    grade = g.text if g else '관람불가'
    gen= soup.select_one("a[href*=genre]")
    nat= soup.select_one("a[href*=nation]")

    genre = gen.text if gen else nat.text

    runtime = li.find(text=re.compile('\d[분]'))
    op = soup.select("a[href*=open]")
    open_date = op[0].text + op[1].text

    info = soup.select('dl.info_spec > dd')

    di = info[1].findAll('a')
    di_str = []
    for i in di:
        di_str.append(i.text)
    director = ', '.join(di_str)

    step3=soup.select_one('dt.step3')
    if step3:
        ac = info[2].findAll('a')
        ac_str = []
        for i in ac:
            ac_str.append(i.text)
        ac_str.remove('더보기')
        actor = ', '.join(ac_str)
    else:
        actor = None

    gr = soup.select('strong.graph_percent')
    pe=[]
    for i in gr:
        pe.append(i.text)
    percent=', '.join(pe)
    print(title, percent)



