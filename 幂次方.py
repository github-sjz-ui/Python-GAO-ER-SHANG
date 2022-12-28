'''
https://www.luogu.com.cn/problem/P1010
'''
def f(x):
    if n!=0:
        a=1;k=0
        print('2',end='')
        while a<=x:
            a*=2
            k+=1
        a/=2
        k-=1
        if k==2 or k==0:
            print('('+str(k)+')',end='')
        if k>=3:
            print('(',end='')
            f(k)
            print(')',end='')
        x-=a
        if x :
            print('+',end='')
            f(x)
    return ''
n=int(input('输入一个正整数n'))
print(f(n))