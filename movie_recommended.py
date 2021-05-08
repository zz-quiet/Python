'''
问题产生：假设已有若干用户名字及其喜欢的电影清单（历史数据），现有
某用户，已看过并喜欢一些电影，现在想找个新电影看看，又不知道看什么好。
需求：根据历史清单，查找与该用户爱好最相似的用户，也就是看过并喜欢
的电影与该用户最接近，然后从那个用户喜欢的电影中选取一个当前用户还没看
过的电影，进行推荐。
'''
from random import randrange
# 其他用户喜欢看的电影清单
data = {'user'+str(i):{'film'+str(randrange(1, 10))\
                        for j in range(randrange(15))}\
        for i in range(10)}
# 待测用户曾经看过并感觉不错的电影
user = {'film1', 'film2', 'film3'}
# 查找与待测用户最相似的用户和Ta喜欢看的电影
similarUser, films = max(data.items(), key=lambda item: len(item[1]&user))
print('历史数据：')
for u, f in data.items():
    print(u, f, sep=':')
print('和您最相似的用户是：', similarUser)
print('Ta最喜欢看的电影是：', films)
print('Ta看过的电影中您还没看过的有：', films-user)