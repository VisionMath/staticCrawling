import urllib.request
import json

client_id = "VjUOzhHTerOMHOWobCw3"  # 개발자센터에서 발급받은 Client ID 값
client_secret = "unhDIyf0fC"  # 개발자센터에서 발급받은 Client Secret 값

print("영어로 번역할 문장을 입력하시오.")
kor_str=input()
encText = urllib.parse.quote(kor_str)

data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    res_boy=json.loads(response_body.decode('utf-8'))
    eng_str=res_boy['message']['result']['translatedText']
    print(kor_str)
    print(eng_str)
else:
    print("Error Code:" + rescode)
