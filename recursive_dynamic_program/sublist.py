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
@File:              sublist.py 
@Time:              18-1-7 下午9:45 
"""
"""
a.给定列表value,返回value的最长递增子列表,例如value=[2,1,5,3,6,4,8,9,7],返回的最长递增子列表为[1,3,4,8,9]
    思路：
        1.生成一个长度N的辅助列表auxiliary_list,auxiliary_list[i]表示以value[i]这个数为结尾的最长递增子序列
        2.初始创建auxiliary_list,赋值auxiliary_list[0]为1,接下来从左到右依次计算每个位置结尾的最长递增子序列
        3.计算到位置i,如果以value[i]结尾最长递增子序列,那么在value[0...i-1]中选择一个数作为倒数第二个数（该数最长递增子序列最长）
    方法1：未经过优化,时间复杂度O(N^2)
    方法2：使用二分法优化查找每个位置最长递增序列长度
        1.生成一个长度为N的ends列表,整型变量right
        2.在从左到右遍历过程中,ends[0...right]为有效区,ends[right+1,N-1]为无效区
"""


def generator_longest_incremental_sublist(value, auxiliary):
    """
    通过辅助列表获得最长递增子序列
    :type value:list
    :type auxiliary:list
    :param value:
    :param auxiliary:
    :return:
    """
    length = 0
    index = 0
    # 获得最长递增子序列长度及其结尾位置
    for i in range(len(auxiliary)):
        if auxiliary[i] > length:
            length = auxiliary[i]
            index = i
    result = [0 for i in range(length)]
    length -= 1
    result[length] = value[index]
    for i in range(index, -1, -1):
        if value[i] < value[index] and auxiliary[i] == auxiliary[index]-1:
            length -= 1
            auxiliary[length] = value[i]
            index = i
    return result


def longest_incremental_sublist(value):
    """
    最长递增子序列（未优化
    :type value:list）
    :param value:
    :return:
    """

    def get_auxiliary(value):
        """
        获得value_list的辅助列表,思路1中数据
        :type value:list
        :param value:
        :return:
        """
        auxiliary_list = [1 for i in range(len(value))]
        for i in range(len(value)):
            for j in range(i):
                if value[i] > value[j]:
                    auxiliary_list[i] = max(auxiliary_list[i], auxiliary_list[j]+1)
        return auxiliary_list

    if value is None or len(value) == 0:
        return 0
    auxiliary = get_auxiliary(value)
    return generator_longest_incremental_sublist(value=value, auxiliary=auxiliary)


def longest_incremental_sublist_optimization(value):
    """
    优化解决最长递增子序列
    :type value:list
    :param value:
    :return:
    """

    def get_auxiliary(value):
        """
        优化得到辅助列表
        :type value:list
        :param value:
        :return:
        """
        auxilary = [1 for i in range(len(value))]
        ends = [0 for i in range(len(value))]
        ends[0] = value[0]
        right = 0
        for i in range(1, len(value)):
            l = 0
            r = right
            while l <= r:
                m = (l + r)//2
                if value[i] > ends[m]:
                    l = m + 1
                else:
                    r = m - 1
            right = max(right, l)
            ends[l] = value[i]
            auxilary[i] = l + 1
        return auxilary

    if value is None or len(value) == 0:
        return 0
    auxilary = get_auxiliary(value)
    return generator_longest_incremental_sublist(value, auxilary)



if __name__ == "__main__":
    pass
