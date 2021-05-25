# 多文件操作
import os
# 得到文件夹下的所有文件
path = "诗"
files = os.listdir(path)
# 遍历文件夹,计算每个文件中内容行数
for file in files:
    txt = []
    # 构造绝对路径，"\\"，其中一个'\'为转义符
    position = path+'\\'+file
    # print(position)
    with open(position,'r',encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            txt.append(line)
    # 将文件名和扩展名分开
    file = os.path.splitext(file)
    print(file[0] + ':' + str(len(txt)) + '行')

#遍历文件夹，在每个文件内头部插入题目
for file in files:
    position = path+'\\'+file
    file = os.path.splitext(file)
    with open(position,'r+',encoding='utf-8') as f:
        conten = f.read()
        # file.seek(off, whence=0)在文件中移动文件指针, 从 whence ( 0 代表文件其始, 1 代表当前位置, 2 代表文件末尾)偏移 off 字节
        f.seek(0,0)
        f.write(file[0]+'\n')
        f.write(conten)
    print(file[0] + '成功')