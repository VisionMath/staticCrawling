# import requests
from bs4 import BeautifulSoup
import urllib.request as req

busNum=360
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
savename2='buspos.xml'
# req.urlretrieve(url2, savename2)

xml = open(savename2, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'xml')

busPos=[]
for itemList in soup.findAll('itemList'):
    gpsX=itemList.find('gpsX').string
    gpsY=itemList.find('gpsY').string
    busPos.append((gpsX, gpsY))

print(f"{busNum} 버스가 {len(busPos)} 대 운행중입니다.")
for i in busPos:
    print(i)