#输入一个包含数字的字符串，如："辞22旧岁迎23新年，心想事成666"
#取出字符串中包含的数字子串进行求和：22+23+666，输出711
#要求：写成自定义函数；至少写出两种方法；

def sum1(s):#单个取值，累乘相加
    s=s+'.'
    t=res=0
    for i in s:
        if '0'<=i<='9':
            t=t*10+int(i)
        else:
            res+=t
            t=0
    return res

def sum2(s):#统计数字子串的数字字符个数k
    k=res=0
    for i in range(len(s)):
        if '0'<=s[i]<='9':
            k+=1
        elif k!=0:
            res+=int(s[i-k:i])
            k=0
    if k!=0:
        res+=int(s[i+1-k:])  #或 s[len(s)-k:]
    return res

def sum3(s): #标记数字子串起始位置j
    j=res=i=0
    while i < len(s):
        if not('0'<=s[i]<='9'):
            if i!=j:
                res+=int(s[j:i])
            j=i+1
        i+=1
    if j!=len(s):
        res+=int(s[j:i])
    return res

ss="辞22旧岁迎23新年，心想事成666" #input('请输入一个包含数字的字符串：')
print(sum1(ss),sum2(ss),sum3(ss))
