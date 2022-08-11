from urllib import request, parse

url = "https://www.baidu.com"
f = request.urlopen(url)
print(f.read().decode("utf-8"))
