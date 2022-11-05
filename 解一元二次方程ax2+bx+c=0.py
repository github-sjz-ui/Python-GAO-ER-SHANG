'''
输入有三行，分别是三个实数a,b,c的值，且a不等于0。

输出两个根X1和X2，用空格隔开，具体格式为：
X1 X2
其中大的根先输出，即X1>=X2。
结果保留两位小数。数据保证一定有实根。
'''
import math
import decimal
import sys
a=float(input("请输入a的值"))
if a==0:
    print("输入错误")
    sys.exit()
b=float(input("请输入b的值"))
c=float(input("请输入c的值"))
delta=b**2-4*a*c
if delta<0:
    print("该方程无实数根")
    sys.exit()
delta=math.sqrt(b**2-4*a*c)
x1=(-b+delta)/(2*a)
x2=(-b-delta)/(2*a)
x1 = decimal.Decimal(x1).quantize(decimal.Decimal("0.00"))#四舍五入
x2 = decimal.Decimal(x2).quantize(decimal.Decimal("0.00"))
print("x1="+str(x1),"x2="+str(x2),sep=" ")
