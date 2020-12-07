# 本文件用来计算Flickr8K中人工打分的相关性


# 定义三个专家的分数list

import pandas as pd



score1 = []
score2 = []
score3 = []

# 打开文件并获取分数
with open('data\ExpertAnnotations.txt','r') as ann:
    for line in ann.readlines():
        # print(line)

        _,_,tmp1,tmp2,tmp3 = line.strip().split("\t")
        # print(tmp1,tmp2,tmp3)

        score1.append(tmp1)
        score2.append(tmp2)
        score3.append(tmp3)

        # input()

# 确保程序的正确性

assert len(score1) == len(score2) == len(score3)
print("len:",len(score1))

# 计算相关性
_scores = {'A':score1,'B':score2,'C':score3}
# print("scores:",scores)
# scores = pd.DataFrame(list(zip(score1,score2,score3)),columns=['A','B','C'])
scores = pd.DataFrame(_scores)
# print(type(scores['A'][0]))

# 转换数据格式
scores = scores.astype(float)

# 输出全部的皮尔森相关系数
# print(scores.corr())
# # 输出A和B的皮尔森相关系数
# print(scores['A'].corr(scores['B']))

# # 计算三者之间的肯德尔相关系数

# AB_k = scores['A'].corr(scores['B'],'kendall')
# AC_k = scores['A'].corr(scores['C'],'kendall')
# BC_k = scores['B'].corr(scores['C'],'kendall')

# # 输出A和B的肯德尔相关系数
# print(AB_k)
# # 输出A和C的肯德尔相关系数
# print(AC_k)
# # 输出B和C的肯德尔相关系数
# print(BC_k)
# # 输出平均值
# print("AVG_kendall:",(AB_k+AC_k+BC_k)/3)

# 简单计算

pearson = scores.corr('pearson')
kendall = scores.corr('kendall')
spearman = scores.corr('spearman')

# print(kendall)
# print(spearman)
# print(pearson)
print("pearson:",(pearson['A'][1:].sum() + pearson['B'][2])/3)
print("spearman:",(spearman['A'][1:].sum() + spearman['B'][2])/3)
print("kendall:",(kendall['A'][1:].sum() + kendall['B'][2])/3)


# 手工计算
# BUG
# print('===\n')

# print(pd.Series(score1).astype(float).std())
# print(pd.Series(score2).astype(float).std())
# print(pd.Series(score3).astype(float).std())

# print(pd.Series(score1).astype(float).cov(pd.Series(score2).astype(float)))

# print(pd.Series(score1).astype(float).cov(pd.Series(score2).astype(float))/(pd.Series(score1).astype(float).std()*pd.Series(score2).astype(float).std()))