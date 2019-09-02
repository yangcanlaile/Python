###
# 获取猫眼的电影排名
####
import requests
import re
import json

# 获得一个页面
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.text
        pattern = re.compile(
            '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
            re.S)

        items = re.findall(pattern, content)
        i = 0
        dic = {
            'index': '',
            'image': '',
            'title': '',
            'actor': '',
            'time': '',
            'score': ''
        }
        dic = []
        for item in items:
            dic.append({
                'index': item[0],
                'image': item[1],
                'title': item[2].strip(),
                'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
                'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
                'score': item[5].strip() + item[6].strip()
            })

    return dic


# 页面内容写入到文件
def write_to_file(content):
    with open('result.js', 'a+', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False))


# 遍历所有页面
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    dicList = get_one_page(url)

    write_to_file(dicList)


# 主函数
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
