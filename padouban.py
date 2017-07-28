#coding:utf-8

import re
import urllib

import threading
from Tkinter import *
from ScrolledText import ScrolledText

def getHtml (ID):
    var.set('已经获取到%s本书'%ID)
    html=urllib.urlopen('https://read.douban.com/tag/%E9%99%90%E6%97%B6%E7%89%B9%E4%BB%B7/?cat=article&sort=top&start=' + str(ID)).read()
    reg=r'<s class="original-tag">(.*?)元</s>.*?<div class="title".*?href=.*?>(.*?)</a>'
    content=re.compile(reg,re.S)
    items=re.findall(content,html)
    #print items[0]
    return items

def write():
    s=0
    a=[]
    ID=0
    while ID<=80:
        L=getHtml(ID)
        ID += 20
        for i in L:
            s+=1
            a.append(float(i[0]))
            text.insert(END,'书名：%s，                           价格:%s\n' %(i[1],i[0]))


    text.insert(END,'-----------------------------------割一下-----------------------------------\n')
    text.insert(END,'书本总数量为%s\n'%s)
    text.insert(END,'书本总价格为：%s\n'%(sum(a)))
    text.insert(END,'书本平均价格为：%.3f\n'%(sum(a)/s))
    var.set('全部处理完成')

def th():
    t1=threading.Thread(target=write)
    t1.start()






root=Tk()
root.title('爬豆瓣')
root.geometry('+300+200')
text=ScrolledText(root,font=('微软雅黑',10))
text.grid()
button=Button(root,text="按下吧骚年",font=('微软雅黑',10),command=th)
button.grid()
var=StringVar()
label=Label(root,font=('微软雅黑',10),fg='red',textvariable=var)
label.grid()
var.set('准备中....')
root.mainloop()
