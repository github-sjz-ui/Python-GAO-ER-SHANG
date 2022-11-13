for i in range(0,10):
    s=str(i)
    s=chr(ord("0")+(ord(s)-ord("0")-2)%10)
    #-(ord("A")-ord(s)+2)%19)
    print(s)