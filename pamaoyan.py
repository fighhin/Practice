#coding:utf-8

import re
import urllib

import threading
from Tkinter import *
from ScrolledText import ScrolledText

def getHtml (ID):
    var.set('已经获取到%s本书'%ID)
    html=urllib.urlopen('http://maoyan.com/board/4?offset=' + str(ID)).read()
    reg=r'class="name"><a href=.*?>(.*?)</a>.*?class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i>'
    content=re.compile(reg,re.S)
    items=re.findall(content,html)
    #print items[0]
    return items

def write():
    s=0
    a=[]
    ID=0
    while ID<=100:
        L=getHtml(ID)
        ID += 10
        for i in L:
            s+=1
            a.append(float(i[1]+i[2]))
            text.insert(END,'片名：%s\t，                           评分:%s\n' %(i[0],i[1]+i[2]))


    text.insert(END,'-----------------------------------割一下-----------------------------------\n')
    text.insert(END,'电影总数量为%s\n'%s)
    text.insert(END,'电影总评分为：%s\n'%(sum(a)))
    text.insert(END,'平均评分为：%.2f\n'%(sum(a)/s))
    var.set('全部处理完成')

def th():
    t1=threading.Thread(target=write)
    t1.start()






root=Tk()
root.title('爬猫眼')
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
