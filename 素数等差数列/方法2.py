from math import sqrt
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def  f(n):
    lis=[]
    for i in range(1,n+1):
        if isprime(i):
            lis.append(i)
    return lis
def g(x):
    list1=[]
    list=[]
    lis=f(n)
    for i in range(len(lis)):
        for a in range(1,n//x):
            if lis[i]+x*a in lis:
                list.append(lis[i]+x*(a-1))
                if list[-1]+x*2 not in lis:
                    list.append(list[-1]+x)
                    list1.append(list)
                    list=[]
            else:
                break
        list=[]
    return list1
n=int(input("请输入整数n："))
len_max=0
for x in range(2,n):
    list2=g(x)
    #print(list2)
    for i in range(len(list2)):
        if len(list2[i]) > len_max:
            len_max=len(list2[i])
            result=list2[i]
print(result,len_max)
