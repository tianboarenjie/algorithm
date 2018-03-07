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
@File:              balance_binary_tree.py 
@Time:              18-1-1 下午12:38 
"""
"""
平衡二叉树：要么是一棵空树,要么任何一个节点的左右子树高度差绝对值不超过1
a.给定一棵二叉树头节点tree,判断这棵树是否为平衡二叉树
    思路：
        1.利用递归收集tree左右孩子信息,包括是否为平衡二叉树,各自最深深度为多少,而后判断
        2.如果左右子树有一个不是平衡二叉树,则整棵树都不是平衡二叉树,如果左右子树最深深度相差绝对值超过1,该数也不是平衡二叉树
b.给定有序列表value_list,其中没有重复值,用这个有序列表生成一棵平衡搜索二叉树,该搜索二叉树中序遍历结果与value_list一致
    思路：
        1.搜索二叉树中序遍历结果为递增
        2.设mid为列表元素个数,利用列表中间值value_list[mid]生成头节点,value_list[0...mid-1]为左孩子,value_list[mid+1...end]为右孩子
        3.利用递归遍历生成
        
"""
from binary_tree import Node


def is_balance(tree):
    """
    给定一棵二叉树头节点tree,判断这棵树是否为平衡二叉树
    :type tree:Node
    :param tree:
    :return:
    """

    def get_height(head, level, res):
        """
        获得head二叉树深度,通过head左右子树高度判断该数是否为平衡二叉树
        :type head:Node
        :type level:int
        :type res:bool
        :param head:
        :param level:
        :param res:
        :return:
        """
        if head is None:
            return level
        left_level = get_height(head.left, level+1, res)
        if res is False:
            return level
        right_level = get_height(head.right, level+1, res)
        if res is False:
            return level
        if abs(left_level-right_level) > 1:
            res = False
        return max(left_level, right_level)

    result = True
    height = get_height(tree, 1, result)
    print("tree depth is %8s" % height)
    return result


def generate_balance_search_binary_tree(value_list):
    """
    利用有序列表生成平衡搜索二叉树
    :type value_list:list
    :param value_list:
    :return:
    """

    def generate(value, start, end):
        """
        利用value[start,end]生产平衡搜索二叉树
        :type value:list
        :type start:int
        :type end:int
        :param value:
        :param start:
        :param end:
        :return:
        """
        if start > end:
            return None
        mid = (start+end)//2
        head = Node(value[mid])
        head.left = generate(value, start, mid-1)
        head.right = generate(value, mid+1, end)
        return head

    if value_list is None or len(value_list) == 0:
        return None
    generate(value_list, 0, len(value_list)-1)


if __name__ == "__main__":
    pass
