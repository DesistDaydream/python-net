import requests

url = "https://www.baidu.com"
r = requests.get(url)
print("状态码：", r.status_code)
print("访问 r.text 时用于解码的编码规范：", r.encoding)
print("响应体：", r.text)
