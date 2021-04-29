# 实现九九乘法表不同规格的输出
# 左下三角形
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2d' %(i,j,i*j),end=' ')
    print('')  #换行

# 右下三角形
for i in range(1,10):
    for j in range(1,10-i):
        print(end='       ')  #每个算法长度为6,加上空格一共是7
    for k in range(1,i+1):
        print('%d*%d=%2d' %(k,i,k*i),end=' ')
    print('')

# 左上三角形
for i in range(9,0,-1):
    for j in range(1,i+1):
        print('%d*%d=%2d' %(i,j,i*j),end=' ')
    print('')

# 右上三角形
for i in range(9,0,-1):
    for j in range(1,i+1):
        print('%d*%d=%2d' %(i,j,i*j),end=' ')
    print('')
    for k in range(i,10):
        print(end='       ')