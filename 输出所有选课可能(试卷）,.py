km='物化生史政地技'
combs=[]
for i in range(128):
    c=0
    s=""
    for j in range(7):
        c=c+i%2
        if i%2==1:
            s+=km[j]
        i=i//2
    if c==3:
        combs.append(s)
print(combs)
