import os
import random
from string import digits
import datetime

print("-----------诗词填空-----------")
path = "出题诗词"
files = os.listdir(path)
positions = []
for file in files:
    # 构造绝对路径，"\\"，其中一个'\'为转义符
    position = path+'\\'+file
    positions.append(position)

i = random.randrange(0,4)
positions = positions[i]
print(positions)
txt = []
count = 0
error_count = 0
null_count = 0
number = int(input('选择题数:'))
score = 100 / number
remain = datetime.datetime.now() + datetime.timedelta(seconds=90)  # 限时90秒完成
print('做题开始时间（限时90秒）：' + str(remain))

with open(positions,'r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        # 删除行头的序号
        line = line.strip(digits)
        line = line.strip("、")
        # 以____作为分隔符分三部分，分隔符前子串，分隔符，分隔符后自创
        head, sep, tail = line.partition('____')
        txt.append(head)

    for j in range(number):
        time_is = (remain - datetime.datetime.now()).seconds
        print('还剩时间' + str(time_is) + '秒')
        if time_is > 90:  # 答题时间超过90秒 游戏结束
            print("答题超过90秒答题时间，退出答题！")
            break
        conten = str(random.choice(txt))
        index = random.randrange(len(conten))
        # 排除挖空在标点符号处
        if (conten[index]=='，')|(conten[index]=='。')|(conten[index]=='?'):
            new_str = conten.replace(conten[index-1],"____",1)
        else:
            # 构建一个带空白的句子
            new_str = conten.replace(conten[index],"____",1)
        print(str(j+1) + '、' + new_str )
        word = input("输入(回车表示跳过): ")
        if word == '':
            print("过！")
            null_count +=1
        else:
            if new_str.replace("____", word) == conten:
                print("正确，你真棒～")
                count +=1
            else:
                # 'f'为格式化操作
                print(f"错了，正确答案: {conten[index]}")
                error_count +=1
print('正确' + str(count) + '道，' + '错误' + str(error_count) + '道，' + '放弃' + str(null_count) + '道')
print("你的得分为：" + str(count*score)) 