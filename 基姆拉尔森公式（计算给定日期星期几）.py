while True:
    sw="日一二三四五六"
    y=int(input("请输入年份："))
    m=int(input("请输入月份："))
    d=int(input("请输入日期："))
    print(y,"年",m,"月",d,"日")
    #处理1月和2月
    if m==1 or m==2:
        m+=12
        y-=1
    week=(d+2*m+3*(m+1)//5+y+y//4-y//100+y//400+1)%7
    weekday=sw[week]
    print("星期",weekday)
