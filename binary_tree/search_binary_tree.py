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
@File:              search_binary_tree.py
@Time:              17-12-28 下午11:11 
"""
"""
搜索二叉树：若二叉树它的左子树不为空,则左子树所有节点的值均小于它的根节点,若它的右子树不为空,则右子树所有节点均大于根节点

a.给定一个二叉树头节点tree,已知所有节点值都不一样,找到含有节点最多的搜索二叉树
    要求：如果节点数N,则要求时间复杂度O(N),额外空间复杂度为O(h),h为二叉树高度
    思路：
        1.以tree为头的树中,如果tree.left和tree.right均满足搜索二叉树,且max(tree.left)<tree.value<min(tree.right)
          则表明整个二叉树都是搜索二叉树,否则最大搜索二叉树在tree的左子树或是右子树之中
        2.由于要先判断左子树,右子树情况,而后判断根,故此采用后序遍历方式
        3.遍历到cur节点,先遍历cur.left获得左子树4个信息：left_SBT(左子树上最大搜索二叉树头节点),left_size(左子树节点数),
          left_min(左子树最小节点值),left_max(左子树最大节点值),同样右子树
          也需要收集这4个信息right_SBT,right_size,right_min,right_max
        4.根据3收集信息判断是否符合1,符合返回cur,不符合判断left_size和right_size返回相应头节点
"""
from binary_tree import Node
import sys


def biggest_subSBT(tree):
    """
    获取tree中最大搜索二叉树头节点
    :type tree:Node
    :param tree:
    :return:
    """

    def postorder(head, records):
        """
        :type head:Node
        :type record:list
        :param head:
        :param record:
        :return:
        """
        if not head:
            records[0] = 0                      # size
            records[1] = sys.maxsize            # min
            records[2] = 0-sys.maxsize          # max
            return head

        value = head.value
        left_SBT = postorder(head.left, records)
        left_size, left_min, left_max = records
        right_SBT = postorder(head.right, records)
        right_size, right_min, right_max = records
        # 如果最大搜索二叉树不是本身,则records[1]和records[2]就没有用了
        records[1] = min(left_min, right_min)
        records[2] = max(left_max, right_max)
        if left_SBT == head.left and right_SBT == head.right and left_max < value and value < right_min:
            records[0] = left_size + right_size + 1
            return head
        records[0] = max(left_size, right_size)
        return left_SBT if left_size > right_size else right_SBT


    sbt_record = [0, 1, 2]
    return postorder(tree, sbt_record)



if __name__ == "__main__":
    pass
