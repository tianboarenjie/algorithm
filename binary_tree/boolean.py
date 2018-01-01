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
@File:              boolean.py 
@Time:              18-1-1 下午8:32 
"""
"""
完全二叉树：除了最后一层外,每一层上节点书均达到最大值,最后一层上只缺少右边若干节点
a.给定一棵二叉树头节点tree,已知其中没有重复节点,实现方法判断这个二叉树是否是搜索二叉树和完全二叉树
    搜索二叉树：
        1.利用morris算法中序遍历二叉树各节点,如果是升序排列则是搜索二叉树
    完全二叉树：
        1.按层遍历二叉树,每层由坐向右依次遍历所有节点
        2.如果当前节点有右孩子没有左孩子,直接返回False
        3.如果当前节点不是左右孩子全都有,那之后的节点全市叶子节点,否则返回False
        4.如果遍历过程中没有返回False,最后返回True
        5.利用列表保存孩子节点
"""
from binary_tree import Node


def isSBT_by_morris(tree):
    """
    利用morris中序遍历检验tree是否是搜索二叉树
    :type tree:Node
    :param tree:
    :return:
    """
    if tree is None:
        return False
    pre = None
    cur1 = tree
    while cur1:
        cur2 = cur1.left
        if cur2:
            while cur2.right and cur2.right != cur1:
                cur2 = cur2.right
            if cur2.right is None:
                cur2.right = cur1
                cur1 = cur1.left
                continue
            else:
                cur2.right = None
        if pre and pre.value > cur1.value:
            return False
        pre = cur1
        cur1 = cur1.right
    return True


def isCBT(tree):
    """
    检验tree是否是完全二叉树
    :type tree:Node
    :param tree:
    :return:
    """
    if tree is None:
        return True
    leaf = False
    leaf_list = [tree]
    while leaf_list:
        tree = leaf_list.pop(0)
        left = tree.left
        right = tree.right
        if (leaf and (left or right)) or (left is None and right):
            return False
        if left:
            leaf_list.append(left)
        if right:
            leaf_list.append(right)
        else:
            leaf = True
    return True


if __name__ == "__main__":
    pass
