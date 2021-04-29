# 使用进度条设计函数优化带刷新的文本进度条
import time
scale = 50
#center(n,'-')表示有n个空位，前面的文字在中间，其余位置用‘-’代替
print("执行开始".center(scale//2,'-')) # / 表示浮点数除法,返回浮点结果; // 表示整数除法,返回不大于结果的一个最大的整数
# 调用一次 perf_counter()，从计算机系统里随机选一个时间点A，计算其距离当前时间点B1有多少秒。
# 当第二次调用该函数时，默认从第一次调用的时间点A算起，距离当前时间点B2有多少秒。
start = time.perf_counter()
for i in range(scale + 1):
# i 个长度的 * 符号
    a = '*' * i
# scale-i） 个长度的 . 符号
# 符号 * 和 . 总长度为50
    b = '.' * (scale - i)
# 显示当前进度，百分之多少
    c = (i/scale)*100
# 两个函数取差，即实现从时间点B1到B2的计时功能。
    dur = time.perf_counter() - start
# \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；
# {:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；
# {}，对应输出的数为a；
# {}，对应输出的数为b；
# {:.2f}，输出有两位小数的浮点数，对应输出的数为dur；
# end=''，用来保证不换行，不加这句默认换行。
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='') 
# 在输出下一个百分之几的进度前，停止0.2秒
    time.sleep(0.2)
print("\n"+"执行结束".center(scale//2,'-'))

'''
#修改，适当降低开始阶段的进展速度，适当加快末尾阶段的进展速度
import time
scale=50
print("执行开始".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
#pow是指数的意思，以下为f(x)=(i+(1-i)*0.03)^2
    fx=int(pow((i+(1-i)*0.03),2))
    a="*"*i    
    b='-'*(scale-i)
    c = (i/scale)*100
    # c=(fx/pow((50+(1-50)*0.03),2))*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.01)
print("\n"+"执行成功".center(scale//2,'-'))
'''