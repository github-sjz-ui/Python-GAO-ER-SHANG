def f(n):#阶乘
    result=1
    for i in range(2,n+1):
        result*=i
    return result
def g(n):#求和
    sum=0
    for i in range(1,n+1):
        sum+=f(i)
    return sum
n=int(input())
print(g(n))