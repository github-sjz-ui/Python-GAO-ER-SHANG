"""
https://www.tzcoder.cn/acmhome/problemdetail.do?method=showdetail&id=1172
"""
n=int(input('从键盘输入一个整数n(1≤n≤100)，打印出指定的菱形:'))
for i in range (1,n+1):
    k=(n-i)*' '
    t=(2*i-1)*'*'
    print(k+t)
for i in range(1,n):
    k=i*' '
    t=(-2*i+2*n-1)*'*'
    print(k+t)