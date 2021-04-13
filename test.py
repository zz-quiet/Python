#从键盘输入一个英文句子，除单词外句子中只包含英文逗号/句号/单双引号/感叹号，统计句子中包括的每个单词（不区分大小写字母）的词频
# 将结果存入字典中，按照词频排序后输出。
import re
import collections
str = input("input:")
s = re.split('\\,|\'|\"|\\.|\\: | |\\!',str)
#将列表中的空元素去掉
m = [i for i in s if i != '']
#转换成小写
new_m = []
for i in m:
    new_m.append(i.lower())
#计数
dic = collections.Counter(new_m)
for key in dic:
    print(key,dic[key])