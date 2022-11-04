def gcd(m,n):
    if m<n:
        m,n=n,m
    for i in range(n,0,-1):
        if m%i==0 and n%i==0:
            return i
while True:
    a=int(input())
    b=int(input())
    print(gcd(a,b))
