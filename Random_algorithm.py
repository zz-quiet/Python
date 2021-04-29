#根据输入出题数量随机输出 100 以内混合加减法的计算题，将题目格式化输出
import random
#input生成的是字符串，用eval返回一个表达式的值，看输入的是整数就是整数，小数就是浮点数；
# int(input())返回的是整数
x = eval(input("算法题数:"))
for i in range(x):
    a = random.randint(1,100)
    b = random.randint(1,100)
    op = random.choice("+-")
    if op == "+":
        print("%2d+%2d=%3d" %(a,b,a+b),end="  ")
    if op == "-":
        if a>b:
            print("%2d-%2d=%3d" %(a,b,a-b),end="  ")
        else:
            print("%2d-%2d=%3d" %(b,a,b-a),end="   ")
    if (i+1)%2 == 0:
        print('')