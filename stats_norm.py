#coding:utf-8
from scipy.stats import norm
import numpy as np

list_num = [1,2,2,1,2,3,0,1,2,4,0]
list_num2 = [2,4,6,3,1,5,7,4,2,4,1]
print(norm.mean(list_num))
print(norm.mean(list_num2))
print('均值:')
print(np.mean(list_num))
print(np.mean(list_num2))
print('方差:')
print(np.var(list_num))
print(np.var(list_num2))
print('标准差:')
print(np.std(list_num))
print(np.std(list_num2))
print('协方差:')
print(np.cov(list_num, list_num2))
print(np.cov(list_num2, list_num))
print('相关系数:')
print(np.correlate(list_num, list_num2))
print(np.correlate(list_num2, list_num))
print(np.correlate(list_num2, list_num2))
print(np.correlate(list_num, list_num))
