import time
import turtle
# 绘制数码管间隔
def drawGap():
    turtle.penup()
    # turtle.fd(5)
# 绘制单段数码管
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
# 根据数字绘制七段数码管
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
# 调整下一个数字位置
    turtle.fd(20)
def drawDate(data):
    count = 0
    remain = 9
    while (remain >= count):
        turtle.pensize(5)
        turtle.color("red")
        dida = remain - count
        print("\r{}".format(dida),end='')
        drawDigit(dida)
        time.sleep(1)
        turtle.reset()
        # turtle.clear()
        # s=len(str(dida))
        # turtle.fd(-60*s)
        count +=1
# def drawDate(date):
#     for i in reversed(range(date)):
#         num = str(i)
#         for n in num:
#             print(n)
#             drawDigit(eval(n))   
#         turtle.clear()
#         s = len(num)
#         turtle.fd(-60*s)
def main():
    turtle.speed(0)
    turtle.penup()
    drawDate(10)
    turtle.done()
    turtle.exitonclick()
main()