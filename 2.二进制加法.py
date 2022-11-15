x = input().strip()   #strip()函数是去除行末的空格与回车符
y = input().strip()
??       
if dis < 0:
    x, y = y,  x
    dis = -dis
for i in range(dis):
    y = "0" + y
jw = 0
ans = ""
for i in range(len(x) - 1, -1, -1):
    a = int(x[i])+int(y[i])+jw
    ??       
    ans =str(a % 2)+ans
if ??:
    ans = "1" + ans
print(ans)
