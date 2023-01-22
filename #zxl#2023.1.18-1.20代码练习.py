n="辞22旧岁迎23新年，心想事成666.8"+' '
x=""
y=[]
for i in n:
    if i.isdigit():
        x+=i
    elif i==".":
        if x=="":
            continue
        elif x.isdigit():
            x+='.'
    else:
        if x!="":
            y.append(x)
            x=""
def sum(list):
    sum=0
    for i in list:
        sum+=float(i)
    return sum
if len(y)!=0:
    print(sum(y))
else:
    print("没有找到数字")
