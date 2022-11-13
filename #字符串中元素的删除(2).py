#字符串中元素的删除
s=input("请输入字符串")
list1=list(s)
ss=input("请输入要删除的字符")
list2=list(ss)
# listname.pop(index)
for i in range(len(list2)):
    for j in range(len(list1)):
        if  list2[i] not in list1:
            break
        else:
            list1.remove(list2[i])
# print(list1)
print("".join(list1))