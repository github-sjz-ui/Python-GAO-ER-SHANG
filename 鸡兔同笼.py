list1=input('输入数据有一行，共2个整数n和m，以空格分隔。').split(' ')
n=int(list1[0]);m=int(list1[1])
x=2*n-0.5*m#鸡的数量
y=0.5*m-n#兔的数量
print(x,y)