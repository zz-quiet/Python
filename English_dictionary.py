# 查询
def search():
    w = input("请输入要查询的单词：")
    f1 = open("词典.txt",'r')
    dic = {}
    # 读取所有行并返回列表
    for line in f1.readlines():
        # 去除每一行末尾的换行符
        line = line.replace("\n","")
        # 将每行的英文和中文分开，分隔符是空格英
        line = list(line.split(' '))
        # 每行开头的英文为键，后面的中文为值
        key = line[0]
        value = line[1:]
        dic[key] = value
    if w in dic.keys():
        print(dic[w])
    else:
        print('字典库中未找到这个单词')
    f1.close()
    exit()

# 添加
def add():
    ww = input("请输入你要添加的单词：")
    flag = 0
    dic = {}
    f2 = open("词典.txt",'r')
    for line in f2.readlines():
        line = line.replace("\n","")
        line = list(line.split(' '))
        key = line[0]
        value = line[1:]
        dic[key] = value
        if ww in dic.keys():
            f2.close()
            flag = 1
            print("该单词已添加到字典库")
            break
        else:
            f2.close()
    if flag != 1:
        f3 = open("词典.txt",'a')
        mean = input("该单词释义为（多个意思用中文逗号隔开）：")
        f3.write(ww + ' ' + mean + '\n')
        f3.close
        exit()

# 返回
def back():
    exit('In [24]')

# 运行
if __name__ == '__main__':
    print("1-添加  2-查询  3-退出")
    www = int(input("请输入数字选择操作："))
    if www == 1:
        add()
    if www == 2:
        search()
    if www == 3:
        back()
    else:
        print('输入错误')