# -*- coding:utf-8 -*-
import requests
import re
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_one_page(url):
    response=requests.get(url)
    return response.text



def parse_one_paeg(html):
    pattern=re.compile('class="board-index.*?">(\d+)</i>.*?"name">.*?>(.*?)</a></p>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?<dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '排名：':item[0],
            '片名':item[1],
            '主演':item[2],
            '发布时间':item,
            '评分':item[4]+item[5]
        }


def write_to_file(content):
    with open('dianyin.txt', 'a') as f:
        f.write(json.dumps(content)+'/n')
        f.close


def main():
    url='http://maoyan.com/board/4?'
    html=get_one_page(url)

    for item in parse_one_paeg(html):
        print (item)
        write_to_file(item)

if __name__ == '__main__':
    main()
