#HTTPDefaultErrorHandler 用于处理HTTP响应错误，错误会抛出HTTPError类型的错误
#HTTPRedirectHandler 用于处理重定向
#HTTPCookieProcessor: 用于处理Cookies
#ProxyHandler 用于设置代理，默认代理为空
#HTTPPasswordMgr: 用于管理密码
#HTTPBasicAuthHandler: 用于管理认证，如果一个链接打开时需要认证，那么可以用它来解决认证问题。

from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import HTTPError
url = "http://localhost:5000"
username = 'username'
password = 'password'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decoode('utf-8')
    print(html)
except HTTPError as e :
    print(e.reason)