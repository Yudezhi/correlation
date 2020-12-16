# 本文件用来计算Flickr8K中人工打分的相关性


# 定义三个专家的分数list

import pandas as pd



score1 = []
score2 = []
score3 = []

mean_score = []

# 打开文件并获取分数
with open('data\ExpertAnnotations.txt','r') as ann:
    for line in ann.readlines():
        # print(line)

        _,_,tmp1,tmp2,tmp3 = line.strip().split("\t")
        # print(tmp1,tmp2,tmp3)
        mean_score.append((float(tmp1)+float(tmp2)+float(tmp3))/3)
        score1.append(float(tmp1))
        score2.append(float(tmp2))
        score3.append(float(tmp3))

        # input()

# 确保程序的正确性

assert len(score1) == len(score2) == len(score3) == len(mean_score)
print("len:",len(score1))

# 计算相关性
_scores = {'A':score1,'B':score2,'C':score3,'mean':mean_score}
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

# print("pearson:",(pearson['A'][1:].sum() + pearson['B'][2])/3)
# print("spearman:",(spearman['A'][1:].sum() + spearman['B'][2])/3)
# print("kendall:",(kendall['A'][1:].sum() + kendall['B'][2])/3)


# 手工计算
# BUG
# print('===\n')

# print(pd.Series(score1).astype(float).std())
# print(pd.Series(score2).astype(float).std())
# print(pd.Series(score3).astype(float).std())

# print(pd.Series(score1).astype(float).cov(pd.Series(score2).astype(float)))

# print(pd.Series(score1).astype(float).cov(pd.Series(score2).astype(float))/(pd.Series(score1).astype(float).std()*pd.Series(score2).astype(float).std()))


# 引用 improved Bert 中的Kendall计算方法进行计算：

# # to reproduce our results on Flickr dataset
# # 1. modify the value 'name' to 'flickr'
# # 2. uncomment these lines
# from scipy.stats import kendalltau

# sim_scores = []
# expert_scores = []
# for i in range(len(samples)):
#     sim_scores.append(samples[str(i)]['metric_result'])
#     expert_scores.append(samples[str(i)]['score'])

# Kendallta2, p_value = kendalltau(sim_scores, expert_scores)
# print(Kendallta2, p_value)


# 肯德尔和谐系数求解

from scipy.stats import kendalltau

Kendallta2, p_value = kendalltau(score3, mean_score)

print(Kendallta2, p_value)

# 按照 https://wiki.mbalib.com/wiki/%E8%82%AF%E5%BE%B7%E5%B0%94%E5%92%8C%E8%B0%90%E7%B3%BB%E6%95%B0  手动计算

# 终究是放弃了。。。

# N =  len(score1) # 被评价的个数
# K = 3 # 评价人员个数

# S = 0
# for i in range(N):
#     tmp1 = score1[i]+score2[i]+score3[i]
#     tmp2 = tmp1/3
#     tmp3 = (tmp1-tmp2) ** 2
#     S += tmp3

# # 假设没有相同等级评价

# W = 12 * S /((K**2 * (N**3 -N)))
# print (W)