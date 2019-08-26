# HTTPDefaultErrorHandler 用于处理HTTP响应错误，错误会抛出HTTPError类型的错误
# HTTPRedirectHandler 用于处理重定向
# HTTPCookieProcessor: 用于处理Cookies
# ProxyHandler 用于设置代理，默认代理为空
# HTTPPasswordMgr: 用于管理密码
# HTTPBasicAuthHandler: 用于管理认证，如果一个链接打开时需要认证，那么可以用它来解决认证问题。

import http.cookiejar, urllib.request

#输出端直接打印cookie
def printCookie():
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name + "=" + item.value)


#cookie打印成文件
def CookieToFile():
    filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)

#保存cookie格式为LWP
def CookieToFileLWP():
    filename = 'cookie.lwp'
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)

#使用文件中的cookie，进行请求
def UsingCookieToReq():
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookie.lwp',ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))


UsingCookieToReq()