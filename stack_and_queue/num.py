#!/usr/bin/env python  
# -*-coding: utf-8 -*- 

""" 
@Version:           v0.1
@Author:            tianbaorenjie
@License:           GPL Licence  
@Contact:           tianbaorenjie@163.com
@Site:              https://github.com/tianbaorenjie 
@Software:          PyCharm 
@Project:           py363_algorithm
@File:              num.py 
@Time:              17-12-5 下午7:25 
"""
"""
给定列表ori_list和整数num,共返回有多少个子列表满足：max(ori_list[i..j])-min(ori_list[i..j)<=num,max表示子列表中最大值
思路：利用双端列表max_list和min_list,当子列表为sub_list[i..j],max_list维护窗口子列表sub_list[i..j]的最大下标更新,
    同理min_list维护最小下标更新,如果sub_list[i..j]满足,则sub_list[a..b]也满足,其中（i<=a<=b<=j）
    1.生成变量i和j表示子列表的左右范围,生成result记录符合满足条件的子列表数量
    2.i保持不变,j向右扩张,max_list和min_list维护子列表最大最小下标更新一旦出现不满足则停止扩张,result=result+j-i
    3.i向右扩张1位,同时重复第2步操作
"""


def get_sublist_nums(ori_list, num):
    """
    计算满足条件：max(ori_list[i..j])-min(ori_list[i..j)<=num的子列表的数量
    :param ori_list: 原始列表
    :param num: 限定值
    :return: 满足条件的子列表数量
    """
    if ori_list is None or len(ori_list) == 0 or num <= 0:
        return 0
    max_list = []
    min_list = []
    result = 0
    i = 0
    j = 0
    while i < len(ori_list):
        while j < len(ori_list):
            while min_list and ori_list[min_list[-1]] >= ori_list[j]:
                min_list.pop()
            min_list.append(j)
            while max_list and ori_list[max_list[-1]] <= ori_list[j]:
                max_list.pop()
            max_list.append(j)
            if ori_list[max_list[0]] - ori_list[min_list[0]] > num:
                break
            j += 1
        if min_list[0] == i:
            min_list.pop(0)
        if max_list[0] == i:
            max_list.pop(0)
        result += j - i
        i += 1
    return result
