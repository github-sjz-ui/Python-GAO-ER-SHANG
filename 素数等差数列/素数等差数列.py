from math import sqrt
def isprime(n):                    # 判断素数
    if n<=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def L(a):
    list=[]
    for j in range(1,a+1):
        if isprime(j):
            list.append(j)
    return list
def max_len(lis):
    max_len=0
    for i in lis:
        if len(i)>max_len:
            max_len=len(i)
    for i in lis:
        if len(i)==max_len:
            print(i)
n=int(input("请输入整数n："))
list1=L(n)
data=[]
r=[]
for i in range(1,n//2):# 定义公差
    for j in range(len(list1)):# 根据指针和公差遍历
        while True:
            if data!=[] and data[-1]+i in list1:
                data.append(data[-1]+i)
                continue
            if data != [] and data[-1]+i not in list1 :
                if len(data) >= 3:
                    r.append(data)
                break
            if list1[j]+i in list1:
                data.append(list1[j])
                data.append(list1[j]+i)
                continue
            else:
                break
            
        data=[]

print(r)
print('最长等差数列为：')
max_len(r)
