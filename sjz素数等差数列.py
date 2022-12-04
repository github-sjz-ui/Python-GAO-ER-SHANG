from math import sqrt
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def  k(n):
    lis=[]
    for i in range(1,n+1):
        if isprime(i):
            lis.append(i)
    return lis
def g(x):
    list1=[]
    list=[]
    lis=k(n)
    for i in range(len(lis)):
        for a in range(1,n//x):
            if lis[i]+x*a in lis :
                list.append(lis[i]+x*(a-1))
                if list[-1]+x*2 not in lis :
                    list.append(list[-1]+x)
                    list1.append(list)
                    list=[]
            else:
                break
        list=[]
    return list1
n=int(input("请输入整数n："))
len_max=0
with open('test.txt','w',encoding='utf-8') as f:
    for x in range(2,n):
        list2=g(x)
        print(list2)
        s1=(" ".join('%s' %id for id in list2))
        f.write(s1+'\n')
        for i in range(len(list2)):
            if len(list2[i]) > len_max:
                len_max=len(list2[i])
                result=list2[i]
    s2='['+(",".join('%s' %id for id in result))+']'
    f.write(s2)
    print(result,len_max)
    for x in range(2,n):
        list2=g(x)
        for i in range(len(list2)):
            if len(list2[i]) == len_max:
                result=list2[i]
                s2='['+(",".join('%s' %id for id in result))+']'
                f.write(s2)
                print(result,len_max)
f.close()
"""
n=100
[5, 11, 17, 23, 29] 5
[5, 17, 29, 41, 53] 5
n=1000
[7,37,67,97,127,157]
[107,137,167,197,227,257]
[359,389,419,449,479,509]
[541,571,601,631,661,691]
[11,71,131,191,251,311]
[53,113,173,233,293,353]
[641,701,761,821,881,941]
[13,103,193,283,373,463]
[503,593,683,773,863,953]
[239,359,479,599,719,839]
[281,401,521,641,761,881]
[73,223,373,523,673,823]
[157,307,457,607,757,907]
"""
