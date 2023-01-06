'''
沃利斯公式
【题目描述】
使用沃利斯公式求圆周率 π。
【输入】（无）
【输出】一行一个浮点数，表示圆周率 π。精确到小数点后4位。
【输入样例】（无）
【输出样例】3.1415

'''
count=1#判断奇、偶位
result=1
while count<=1000000:
    if count%2==0:
        a=count#分子
        b=a+1#分母
    else:
        a=count+1
        b=count
    new=a/b
    count+=1
    result*=new
print(round(result*2,4))
