# requests库请求网页获取内容
# get,poost, put, delete, head, options
#####requests.codes状态码########
# 100: continue
# 101: switching_protocols
# 102: processing
# 103: checkpoint
# 122: uri_too_long, request_uri_too_long
# 200: ok, okay, all_ok, all_okay, all_good, \o/, ✓
# 201: created
# 202: accepted
# 203: non_authoritative_info, non_authoritative_information
# 204: no_content
# 205: reset_content, reset
# 206: partial_content, partial
# 207: multi_status, multiple_status, multi_stati, multiple_stati
# 208: already_reported
# 226: im_used
# 300: multiple_choices
# 301: moved_permanently, moved, \o-
# 302: found
# 303: see_other, other
# 304: not_modified
# 305: use_proxy
# 306: switch_proxy
# 307: temporary_redirect, temporary_moved, temporary
# 308: permanent_redirect, resume_incomplete, resume
# 400: bad_request, bad
# 401: unauthorized
# 402: payment_required, payment
# 403: forbidden
# 404: not_found, -o-
# 405: method_not_allowed, not_allowed
# 406: not_acceptable
# 407: proxy_authentication_required, proxy_auth, proxy_authentication
# 408: request_timeout, timeout
# 409: conflict
# 410: gone
# 411: length_required
# 412: precondition_failed, precondition
# 413: request_entity_too_large
# 414: request_uri_too_large
# 415: unsupported_media_type, unsupported_media, media_type
# 416: requested_range_not_satisfiable, requested_range, range_not_satisfiable
# 417: expectation_failed
# 418: im_a_teapot, teapot, i_am_a_teapot
# 421: misdirected_request
# 422: unprocessable_entity, unprocessable
# 423: locked
# 424: failed_dependency, dependency
# 425: unordered_collection, unordered
# 426: upgrade_required, upgrade
# 428: precondition_required, precondition
# 429: too_many_requests, too_many
# 431: header_fields_too_large, fields_too_large
# 444: no_response, none
# 449: retry_with, retry
# 450: blocked_by_windows_parental_controls, parental_controls
# 451: unavailable_for_legal_reasons, legal_reasons
# 499: client_closed_request
# 500: internal_server_error, server_error, /o\, ✗
# 501: not_implemented
# 502: bad_gateway
# 503: service_unavailable, unavailable
# 504: gateway_timeout
# 505: http_version_not_supported, http_version
# 506: variant_also_negotiates
# 507: insufficient_storage
# 509: bandwidth_limit_exceeded, bandwidth
# 510: not_extended
# 511: network_authentication_required, network_auth, network_authentication
##################################


import requests
import re
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb2312')

# 测试Requests Get ,传递params, headers
from requests import RequestException


def testRequestsGet():
    url = 'http://httpbin.org/get'
    r = requests.get(url)
    # 加入提交参数
    data = {
        'name': 'germey',
        'age': 22
    }

    # 传递headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    r = requests.get('https://www.zhihu.com/explore')
    print(r.text)
    # pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)

    # titles = re.findall(pattern, r.text)
    # print(titles)

    # r = requests.get(url, params=data)
    # print(r.text)


# 测试获取二进制图片
def testRequestsImage():
    r = requests.get('http://github.com/favicon.ico')
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)
    print(type(requests.codes.ok))


# 文件上传
def uploadFiles():
    files = {'file': open('favicon.ico', 'rb')}
    r = requests.post("http://httpbin.org/post", files=files)
    print(r.text)


# 保持会话
def keepSession():
    s = requests.session()
    url = 'http://httpbin.org/cookies/set/number/123456789'
    s.get(url)
    r = s.get('http://httpbin.org/cookies')
    print(r.text)


# SSL证书验证
def SSLVerifyReq():
    response = requests.get('http://www.12306.cn')
    print(response.status_code)


# SSL忽略证书验证
def SSLUnVerifyReq():
    response = requests.get('http://www.12306.cn', verify=False)
    print(response.status_code)


# SSL证书验证，并指定特定文件
def SSLVerifyFileReq():
    response = requests.get('http://www.12306.cn', cert=('path/server.crt', '/path/key'))
    print(response.status_code)


# 代理设置
def usingProxiesReq(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=1l5vavpm905cc1okesbqobh5rs; Hm_lvt_a3c0d937c858fbe264753596e485cd38=1565703497,1565782337,1565782903,1567004371; MEIQIA_TRACK_ID=1PMyruQzaBLLntKCOT2RtACarCv; Hm_lpvt_a3c0d937c858fbe264753596e485cd38=1567005430',
        'Host': 'www.w3cschool.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', }
    proxies = {  # 切换成你可用的代理
        "http": "http://192.99.203.93:35289",
        "https": "http://192.99.203.93:35289"
    }

    response = requests.get(url, headers=headers)
    # print(response.text.encode('gb2312', 'ignore'))
    print(response.encoding)
    print(response.apparent_encoding)
    # r1 = response.encoding = 'gb2312'
    # response.content 为bytes类型，
    # response.text为UNICODE编码后的文本
    r = str(response.content, encoding=requests.utils.get_encodings_from_content(response.text)[0])
    # print(requests.utils.get_encodings_from_content(r))

    with open('1.html', 'w', encoding='utf-8') as file:
        file.write(r)


url = 'http://www.w3cschool.cn'
usingProxiesReq(url)
