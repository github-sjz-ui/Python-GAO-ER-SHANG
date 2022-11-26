from math import sqrt
def su(x):
    if x<=1:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return False
    return True
def L(a):
    list=[]
    for j in range(1,a+1):
        if su(j):
            list.append(j)
    return list
def Y(b):
    li=[]
    k=2
    list=L(n)
    while k<=n:
        while k in list:
            li.append(k)
            k=k+b
        if len(li)>=3:
            return li
        else:
            li=[]
            k+=1
n=int(input("请输入正整数n："))
s=[]
q=0
for t in range(2,n):
    if Y(t)==None:
        continue
    if len(Y(t))>q:
        q=len(Y(t))
        s.append(Y(t))
print("列表最长长度为：",q,"其列表内容为",s[-1])