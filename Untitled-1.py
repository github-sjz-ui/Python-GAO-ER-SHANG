s=input("请输入英文字符串：")#1234567890
sn=""
for i in range(len(s)//2):
    sn=sn+s[i]+s[-1-i]
if len(s)%2!=0:
    sn=sn+s[len(s)//2]
print(sn)