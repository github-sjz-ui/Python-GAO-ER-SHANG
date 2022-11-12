s=input("输入两个数a和n（其中1<=a,n<=9）,分别用空格分隔:")
list=s.split()
a=list[0]
n=int(list[1])
sum=0
for i in range(1,n+1):
    sum+=int(a*i)
print(sum)
