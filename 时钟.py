from turtle import *  ## 导入turtle库
from datetime import *  ## 导入时间库
 
def Skip(step):
    penup()
    forward(step)
    pendown()
 
## 定义Turtle形状，建立指针Turtle
def mkHand(name, length): 
    reset()
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name, handForm) ## 定义3个指针的对象
 
def Init():
    global secHand, minHand, hurHand, printer
    mode("logo") ## 初始Turtle指向北
     
    ## 建立三个表针Turtle并初始化
    mkHand("secHand", 125)
    mkHand("minHand",  130)
    mkHand("hurHand", 90)
    secHand = Turtle()
    ## Turtle是turtle模块中的类，可将三个指针实例化
     
    secHand.shape("secHand")
    ## 定义秒针对象。shape是Turtle类中的方法
     
    minHand = Turtle()
    minHand.shape("minHand")
    ## 定义分针对象
     
    hurHand = Turtle()
    hurHand.shape("hurHand")
    ## 定义时针对象
     
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
        ## 速度设置
     
    ## 定义输出文字Turtle
    printer = Turtle()
    ##实例化，并输出文字为类的一个对象
     
    printer.hideturtle()
    printer.penup()
 
def SetupClock(radius):  ##定义表的外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius-20)
        else:
            dot(5)
            Skip(-radius)
        right(6)
 
def Week(t):    
    week = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    return week[t.weekday()]
 
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)
 
def Tick(): ## 定义指针的动态显示    
    t = datetime.today()
    second = t.second + t.microsecond*0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    secHand.setheading(6*second)
    ## 指针对象中的setheading方法接受参数，设定朝向的角度
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
 
    tracer(False)  
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 16, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 16, "bold"))
    printer.home()
    tracer(True)
 
    ontimer(Tick, 100) 
    ##设置为100毫秒后继续调用tick函数
 
def main():
    tracer(False)
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()
 
## 文件作为脚本直接执行才会被执行，
## 而import到其他脚本中是不会被执行的声明
if __name__ == "__main__":       
    main()