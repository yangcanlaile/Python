# parse解析URL地址
# urlparse  解析url为对象ParseResult
# urljoin  url连接
# urlencode  url编码

# urlunsplit  将链接各个部分组合成完整链接的方法
# data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# urlunsplit(data)
# urlsplit()

from urllib.parse import urlparse, urlencode
from urllib.parse import parse_qs

params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

query = 'name=germey&age=22'
print(parse_qs(query))

