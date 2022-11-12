def r(a,n):
    a=a*10**n
    a=int(a+0.5)
    a=a/10**n
    return a
print(r(4.99999,3))
