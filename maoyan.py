
# -*- coding:cp936 -*-
import requests
import re
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import string

def get_one_page(url):
    response=requests.get(url)
    return response.text



def parse_one_paeg(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        it=item
        yield {
            'rank':it[0],
            'name':it[1],
            'actor':it[2],
            'time':it[3],
            'score':it[4]+it[5]
        }


def write_to_file(content):
    with open('dianyin.txt', 'a') as f:
        line=json.dumps(content,encoding='UTF-8', ensure_ascii=False)+'/n'
        f.write(line)
        f.close


def main():
    url='http://maoyan.com/board/4?'
    html=get_one_page(url)

    for item in parse_one_paeg(html):
        #item=str(item)
        print item
        #for t in item:
            #print t.encode('utf-8')
        write_to_file(item)

if __name__ == '__main__':
    main()
