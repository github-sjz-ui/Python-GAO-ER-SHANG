#编写自定义函数：随机产生x个(0<x<26)不重复的大写字母。尝试写出两种办法。
#*拓展：随机产生x个(0<x<52)不重复的大小写字母

import random
def rndup1(x):
    res=[];i=1
    while i<=x:
        ch=chr(ord('A')+random.randint(0,25))
        if ch not in res:
            res.append(ch)
            i+=1
    return res

def rndup2(x):
    res='';i=0
    f=[False]*26
    code='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while i<x:
        ch=random.randint(0,25)
        if not f[ch]:    #或 f[ch]==False:
            res+=code[ch]
            f[ch]=True
            i+=1
    return res

def rndch(x):
    res='';i=1
    while i<=x:
        ch=chr(ord('A')+random.randint(0,25)+random.randint(0,1)*32)
        if ch not in res:
            res+=ch
            i+=1
    return res

print(rndup1(8),rndup2(8),rndch(10))
