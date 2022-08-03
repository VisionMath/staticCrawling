# import requests
from bs4 import BeautifulSoup
import urllib.request as req

busNum=52
# keys = 'bz6p9J0zjOTIbSrGsm6BH3B4i9IEW29rnGC6LNchn750ZVUpKW3HKr211MoqBZhOy02OyMRxsN60JqwPc0KpXQ=='

# url=f'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?serviceKey={keys}&strSrch={busNum}'
# url = 'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid'
# savename = 'businfo.xml'
# params = {'serviceKey': keys, 'busRouteId': '100100057'}

# req.urlretrieve(url, savename)

# xml = open(savename, 'r', encoding='utf-8').read()
# soup = BeautifulSoup(xml, 'xml')

# routeId = None
# for itemList in soup.findAll('itemList'):
#     busRouteId=itemList.find('busRouteId').string
#     busRouteNm=itemList.find('busRouteNm').string
#     if busRouteNm==str(busNum):
#         routeId=busRouteId
#         break
#
# print(routeId)
#
# url2=f'http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={keys}&busRouteId={routeId}'
savename='busComeInfo.xml'
# req.urlretrieve(url2, savename2)

xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'xml')

busCome=[]
for item in soup.findAll('item'):
    lineno=item.find('lineno').string
    m1=item.find('min1')
    min1=m1.string if m1 else ''
    busCome.append((lineno, min1))
    if min1 !='':
        print(f"{lineno}번 버스가 {min1}분 후에 도착 예정입니다.")
    else:
        print(f"{lineno}번 버스에 대한 도착정보가 없습니다.")