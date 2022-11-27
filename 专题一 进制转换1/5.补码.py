#补码
x = abs(int(input("输入十进制数:")))
a=[0]*7
for i in range(7):
    a[i] = 1 - x % 2
    x = x // 2
i=0
a[0]=a[0]+1
while ？？:
    a[i]=0
    ？？
    i=i+1  
？？
for i in range(7):
    ans = ans + str(a[6 - i])
print(ans)
