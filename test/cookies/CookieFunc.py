import requests
def getCookie():
    url = "https://www.baidu.com"
    r = requests.get(url)
    print(r.cookies)
    for key, value in r.cookies.items():
        print(key + '= ' + value)

#模拟浏览器cookie登录，知乎网站
def enterZhiHu():
    headers = {
        'Cookie': '_zap=8d53437e-a20a-4c3c-88ab-626b98f04606; _xsrf=3bc194d5-77cc-4c01-a18a-2f344c94f4c2; d_c0="ACAhicCP9Q-PTujVUruZJV3LIU3u0O5Gdio=|1566957393"; tgw_l7_route=66cb16bc7f45da64562a077714739c11; capsion_ticket="2|1:0|10:1566980643|14:capsion_ticket|44:YmRhZjdkYWNkYWRiNGQxZGI1MzMxYzMxOWQ2MjM3YTI=|cc33f2fcdea8dbee194fa14835a11e286d04c71f7a7552e6fe3d6f8d51985dac"; z_c0="2|1:0|10:1566980663|4:z_c0|92:Mi4xMEJXZkF3QUFBQUFBSUNHSndJXzFEeVlBQUFCZ0FsVk5ONGhUWGdDLVNuY19lX0NsanlubmZFZGRCUVRzbmR0ZC13|407f90e98484f52db12ebbd37c6922fa2ac0d483f441a233f5fd52cdc0f2edfb"; unlock_ticket="AHCA4eH8wAomAAAAYAJVTT9BZl2m9MEXVCtd2pBBYzRNSB0d3wEwlw=="; tst=r',
        'HOST':'www.zhihu.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

    }
    r = requests.get('https://www.zhihu.com', headers=headers)
    print(r.text)

enterZhiHu()