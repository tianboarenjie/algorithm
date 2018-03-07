#!/usr/bin/env python  
# -*-coding: utf-8 -*- 

""" 
@Version:           v0.1
@Author:            tianbaorenjie
@License:           GPL license  
@Contact:           tianbaorenjie@163.com
@Site:              https://github.com/tianbaorenjie 
@Software:          PyCharm 
@Project:           py363_algorithm
@File:              length.py 
@Time:              17-12-27 下午11:23 
"""
"""
给定一棵二叉树头节点head和一个整数sum,二叉树节点类型都为整数,求累加和为sum的最长路径长度,不考虑相加可能溢出情况
要求时间复杂度为O(N),额外空间复杂度O(h),h为二叉树高度
思路：
    1.已知二叉树头节点tree和sum,生成变量max_len记录累加和为sum的最长路径长度,sum2position头节点tree到节点累加和cur_sum到节点层数level的对应
      关系,pre_sum表示头节点到父节点累加和.
    2.遍历节点计算cur_sum,如果cur_sum在sum2position内,表明上层节点累加和已经出现过sum,不更新sum2position,如果没有,则将cur_sum:level更新进
      sum2position.
    3.计算cur_sum-sum是否在sum2position键中,如果在表明节点累加和cur_sum-sum的节点到当前节点中间累加和为sum,比较两节点间层数与max_len并更新
    4.递归遍历所有节点,利用2和3的判断更新max_len
"""
from binary_tree import Node


def max_length_with_sum_from_binary_tree(tree, sum):
    """
    获取tree中节点累加和为sum的最长路径长度
    :type tree:Node
    :type sum:int
    :param tree:
    :param sum:
    :return:
    """

    def preorder(head, sum, pre_sum, level, max_len, sum2position):
        """
        :type head:Node
        :type sum:int
        :type pre_sum:int
        :type level:int
        :type max_len:int
        :type sum2position:dict
        :param head: 当前节点
        :param sum:
        :param pre_sum: 头节点到父节点累加和
        :param level: 头节点到当前节点层数
        :param max_len: 节点累加和为sum的最长路径长度
        :param sum2position: 头节点到当前节点累加和到节点层数的对应关系
        :return:
        """
        if not head:
            return max_len
        cur_sum = pre_sum + head.value
        if not sum2position.get(cur_sum):
            sum2position[cur_sum] = level
        j = sum2position.get(cur_sum - sum)
        if sum2position.get(j):
            max_len = max(sum2position.get(j), max_len)
        max_len = preorder(head.left, sum, cur_sum, level+1, max_len, sum2position)
        max_len = preorder(head.right, sum, cur_sum, level + 1, max_len, sum2position)
        if level == sum2position.get(cur_sum):
            sum2position.pop(cur_sum)
        return max_len

    if not tree or not sum:
        return None
    tmp = {0:0}
    return preorder(tree, sum, 0, 1, 0, tmp)

if __name__ == "__main__":
    pass
