# 文件中写入100个1~1000范围内的随机数
import random
a = []
fp = open('data.txt','w')
for i in range(100):
    b = random.randint(1,1000)
    a.append(b)
    x = str(b)
    if i<99:
        fp.write(x)
        fp.write(',')
    else:
        fp.write(x)
print('success')


#文件内的随机数按升序排序
a.sort()  #升序
print(a)
f1 = open('data_asc.txt','w')
for k in range(100):
    out = a[k]
    out = str(out)
    if k<99:
        f1.write(out)
        f1.write(',')
    else:
        f1.write(out)
print('success')
f1.close()
fp.close()