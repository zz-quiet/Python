# 用turtle表示蒙特卡罗计算圆周率
from random import random
import turtle

DARTS = 1000*1000
hits = 0
turtle.penup()
turtle.speed(0)
turtle.tracer(False)
for i in range(1,DARTS+1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    turtle.goto(x*600,y*600)
    turtle.pendown()
    if dist <= 1:
        hits += 1
        turtle.dot(2,'red')
    else:
        turtle.dot(2,'green')
    turtle.penup()
turtle.tracer(True)
pi = 4 * (hits/DARTS)
print("pi的值是: {}".format(pi))
turtle.goto(110,-30)
pi = 'pi='+str(4*(hits/DARTS))
turtle.write(pi,font=('consolas',15,'normal'))
turtle.exitonclick()


'''
# 网上例子
from random import random
import turtle as t
from math import sqrt

darts = 10000
hits = 0
t.penup()
t.speed(0)
t.tracer(False)
for i in range(1,darts + 1):
     x = random()
     y = random()
     dist = sqrt(x**2 + y**2)
     t.goto(x*300,y*300)
     t.pendown()
     if dist <= 1.0:
          hits += 1
          t.dot(2,'red')
     else:
          t.dot(2,'blue')
     t.penup()
t.tracer(True)
print(4*(hits/darts))
t.goto(110,-30)
pi = 'pi='+str(4*(hits/darts))
t.write(pi,font=('consolas',15,'normal'))
t.exitonclick()
'''



'''
# 蒙特卡罗圆周率计算
from random import random
from time import perf_counter
darts = 1000 * 1000 #虚拟一个1000*1000的正方形
hit = 0.0
start = perf_counter()
for i in range(1,darts+1):
    x,y = random(),random()
    dist = pow(x**2+y**2,0.5)#计算点x,y到圆心的距离
    if dist <= 1.0:
        hit = hit +1
pi = 4 * (hit/darts)
print("圆周率是：{}".format(pi))
end = perf_counter() - start
print("运行时间是：{:.2f}S".format(end))
'''