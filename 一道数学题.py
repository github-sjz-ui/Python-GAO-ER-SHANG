'''
一道数学题：
a1=1,a1*a2*a3*a4*a5*a6*······*an=n^2
'''
n=int(input('输入n项'))
list1=[1]
for i in range(n-1):
    new=(len(list1)+1)**2
    for j in list1:
        new/=j
    list1.append(new)
print(list1,new)
#通项公式
print(1,end=' ')
for i in range(2,n+1):
    print(i**2/(i-1)**2,end=' ')