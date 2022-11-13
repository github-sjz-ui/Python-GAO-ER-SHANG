#字符串中元素的删除
s=input("请输入字符串")
ss=input("请输入要删除的字符")
sss=""
for i in s:
    if i in ss:
        continue
    else:
        sss+=i
print(sss)