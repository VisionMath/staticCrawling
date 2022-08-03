import requests

url = 'http://apis.data.go.kr/6260000/FoodService/getFoodKr'
keys = '8AMRSkqU33Yx61a/COOd+m9c+236jK08BLKEYppsvvndL5tCISUNZwJLyPJSkJfCW1zM6cVdGcbr7YH0qBgZyQ=='
params = {'serviceKey': keys, 'pageNo': '1', 'numOfRows': '10', 'resultType': 'json', 'UC_SEQ': ''}

response = requests.get(url, params=params)
print(response.content)
