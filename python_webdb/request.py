from urllib.parse import urlencode
from urllib.request import urlopen, Request

# get
# get 방식은 request 객체를 사용할 필요가 없다.
http_response = urlopen('https://www.example.com')
body = http_response.read()
print(body)

# post
# post 방식에서 데이터는 body에 붙어서 온다.
data = {
    'email': 'salem@naver.com',
    'password': '123',
    'name': '추추추',
}

data = urlencode(data).encode('utf-8')

request = Request('http://www.example.com', data)
request.add_header("Content-Type", "text/html")
request.add_header("cookies:jsessionID=3212548121")

http_response = urlopen(request)
print(http_response.read())
