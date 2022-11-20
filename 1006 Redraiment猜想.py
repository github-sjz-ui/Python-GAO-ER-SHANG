"""
redraiment在家极度无聊，于是找了张纸开始统计素数的个数。
设函数f(n)返回从1->n之间素数的个数。
redraiment发现:

f(1) = 0
f(10) = 4
f(100) = 25
...

满足g(m) = 17 * m**2 / 3 - 22 * m / 3 + 5 / 3
其中m为n的位数。
他很激动，是不是自己发现了素数分布的规律了！"""
from math import *
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def f(n):
    count=0
    for i in range(1,n+1):
        if isprime(i):
            count+=1
    return count
def g(m):
    return 17 * m**2 / 3 - 22 * m / 3 + 5 / 3
print(f(100),g(len(str(100))))