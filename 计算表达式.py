#https://www.tzcoder.cn/acmhome/problemdetail.do?method=showdetail&id=1482
from math import *
def f(x,n):
    if n==1:
        y=sqrt(n+x)
    else:
        y = sqrt(n+f(x,n-1))
    return y
print(f(0,3))