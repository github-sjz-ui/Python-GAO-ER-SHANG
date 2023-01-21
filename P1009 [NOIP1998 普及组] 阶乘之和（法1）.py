'''
https://www.luogu.com.cn/problem/P1009
'''
def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
def g(n):
    if n==1:
        return 1
    else:
        return f(n)+g(f(n-1))
n=int(input())
print(g(n))
