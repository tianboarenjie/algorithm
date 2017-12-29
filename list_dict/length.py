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
@File:              length.py 
@Time:              17-12-27 下午11:48 
"""
"""
原题：给定一个无序整数列表value_list,其中元素可正可负可0,给定一个整数k,求value_list中所有子列表中累加和为k的最长子数组长度,以及开始和结尾
原题思路：
    核心：设定s(i)表示value_list[0...i]的累加和,则可知s(i)-s(j-1)=value_list[0...i]-value_list[0...j-1]=value[j...i](j<=i)
    1.建立初始变量sum(value_list遍历元素和)和sum2position(字典,表示列表元素和最早出现出现sum的位置),遍历value_list,得到sum
    2.判断sum-k在sum2position键中是否存在,不存在说明以value_list[i]结尾累加没有等于k的子数组
    3.如果在,考虑sum=s(i),sum-k如果存在假设位置是j,在s(j)=sum-k,k=sum-(sum-k)=(i)-s(j),也即从j+1到i和为k,判断length和i-j大小
    4.判断sum是否在sum2position中,不存在添加在sum2position中sum:position对应关系,存在则什么也不用做
"""


def get_max_length_of_sublist_with_sum(value_list, value):
    """
    查找value_list中列表和为value的最长子列表
    :type value_list:list
    :type value:int
    :param value_list:
    :param value:
    :return:
    """
    sum = 0
    sum2position = {}
    length = 0
    start = 0
    end = 0
    for i in range(len(value_list)):
        sum += value_list[i]
        j = sum2position.get(sum-value)
        if j:
            if i-j > length:
                length = i-j
                start = j+1
                end = i
        if not sum2position.get(sum):
            sum2position[sum] = i
    return (length, start, end)


if __name__ == "__main__":
    pass
