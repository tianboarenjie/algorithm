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
@File:              maxrec.py 
@Time:              17-12-4 下午10:51 
"""
"""
给定一个矩阵,其中值只有0和1两种,求其中全是1的所有矩形区域中,最大的矩形区域中1的数量
思路：
1.遍历矩阵,每次遍历生成一个一维列表height,每个数表示当前列最多连续1的个数,计算该一维列表最大1个个数
2.如何快速计算一个一维列表中表示的1的最大数量
    1)遍历height,利用一个栈记录这个一维数组的下标stack
    2）入栈规则：
        当这个栈为空;
        通过栈顶值查找height[stack[j]],如果当前值height[i]小于height[stack[j]],i入栈
    3）否则,盏顶元素出栈,计算单前1最大数量,重复该判断
        计算1最大数量：height[stack[j]]*(i-k-1);k为当前盏顶元素
    4)遍历完成,stack不为空
        以此记录弹出的值j,弹出后栈顶元素k,通过height[j]*(len(height)-k-1)
"""


def get_max_rec(ori_rec):

    def max_rec_from_bottom(ori_height):
        """
        计算类似[3,4,5,1,6]这样的列表表示的1的最大数量
        :param ori_height:
        :return:
        """
        if ori_height is None or len(ori_height) == 0:
            return 0
        stack = []
        max_area = 0
        for i in range(len(ori_height)):
            while stack and ori_height[stack[-1]] <= ori_height[i]:
                j = stack.pop()
                k = stack[-1] if stack else -1
                max_area = max(max_area, (i-k-1)*ori_height[j])
            stack.append(i)
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            max_area = max(max_area, (len(ori_height)-k-1)*ori_height[j])
        return max_area

    if ori_rec is None or len(ori_rec) == 0 or len(ori_rec[0]) == 0:
        return 0
    max_area =0
    height = [0 for i in range(len(ori_rec[0]))]
    for i in range(len(ori_rec)):
        for j in range(len(ori_rec[0])):
            height[j] = 0 if ori_rec[i][j] == 0 else height[j]+1
        max_area = max(max_area, max_rec_from_bottom(height))
    return max_area

