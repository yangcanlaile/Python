# parse解析URL地址
# urlparse  解析url为对象ParseResult
# urljoin  url连接
# urlencode  url编码

# urlunsplit  将链接各个部分组合成完整链接的方法
# data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# urlunsplit(data)
# urlsplit()

# parse_qs() GET请求参数，可以将其转回字典
# parse_qsl GET请求参数，可以将其转回元组组成的列表

# quote() 将内容转化为URL编码的格式
# unquote()实现URL编码后的解码

# robotparser  解析robot.txt协议。

from urllib.parse import urlparse, urlencode
from urllib.parse import parse_qs, parse_qsl, quote

params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
# print(url)

query = 'name=germey&age=22'
# print(parse_qsl(query))

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
