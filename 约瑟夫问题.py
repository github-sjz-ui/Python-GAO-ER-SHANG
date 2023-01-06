'''
约瑟夫问题
【题目描述】
N个人围成一圈，从第一个人开始报数，数到M的人出圈；再由下一个人开始报数，数到M的人出圈；…输出依次出圈的人的编号。
【输入】输入N和M。
【输出】输出一行，依次出圈的人的编号。
【输入样例】8 5
【输出样例】5 2 8 7 1 4 6 3

'''
n=8
m=5
s=''
index=0
for i in range(1,n+1):
    s+=str(i)
while len(s)!=0:
    result=s[(index+m-1)%len(s)]
    print(result,end=' ')
    index=(index+m-1)%len(s)
    ss=result
    sss=""
    for i in s:
        if i in ss:
            continue
        else:
            sss+=i
    s=sss
