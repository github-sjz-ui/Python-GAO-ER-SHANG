import sys
a=""
s=input("请输入两个数（用空格分隔）")
for i in s:
    if "0"<=i<="9":
        a+=i
    else:
        b=s[len(a)+1:]
        break
a=float(a)
b=float(b)
plus=a+b;minus=a-b;multiply=a*b
if b==0:
    divide="输入数据有误！"
else:
    divide=a/b#加减乘除
print("两数四则运算的结果为：")
print(a,"+",b,"=",plus)
print(a,"-",b,"=",minus)
print(a,"*",b,"=",multiply)
print(a,"/",b,"=",divide)