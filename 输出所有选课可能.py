xuanke="物化生史政地技"
combs=[]
s=""
for i in range(5):
    t=i
    s=s+xuanke[t]
    for j in range(t+1,6):
        m=j
        s=s+xuanke[m]
        for k in range(m+1,7):
            n=k
            s=s+xuanke[n]
            combs.append(s)
            s=s[:-1]
        s=s[0]
    s=""
print("所有选课组合：",end="")
print(combs)
print("共有"+str(len(combs))+"种组合")
