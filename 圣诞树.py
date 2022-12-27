'''
https://www.tzcoder.cn/acmhome/problemdetail.do?method=showdetail&id=5141
'''
import sys
while True:
    n=int(input('偶数（6<=n<=100），表示圣诞树的高度'))
    if n==0:
            sys.exit()
    for i in range (1,n+1):
        k=(n-i)*' '
        t=(2*i-1)*'*'
        print(k+t)
    for i in range(n):
        print((n-2)*' '+'***'+(n-2)*' ')