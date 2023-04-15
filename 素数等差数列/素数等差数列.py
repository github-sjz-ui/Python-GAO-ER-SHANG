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
list1=L(100)
data=[]
r=[]
for i in range(1,100//2):# 定义公差
    for j in range(len(list1)):
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