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