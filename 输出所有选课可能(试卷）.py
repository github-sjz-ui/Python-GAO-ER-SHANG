km='物化生史政地技'
combs=[]
for i in range(128):
    t=i
    c=0
    s=""
    for j in range(7):
        c=c+t%2
        if t%2==1:
            s+=km[j]
        t=t//2
    if c==3:
        combs.append(s)
print(combs)
