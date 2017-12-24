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
@File:              convert.py 
@Time:              17-12-24 上午10:47 
"""
"""
对于搜索二叉树（该树左孩子都比头节点小,该树的右孩子都比头节点大）而言,有本身值域,也有指向左孩子（left）和右孩子（right）的指针,对于双向链表节点来说,
也有本身值域,以及指向上一个节点(pre)和下一个节点的指针(next)的指针,二叉树和双向链表在结构上有很打相似之处,请实现一个函数完成搜索二叉树到有序双向链表的转换
思路：
    1.使用递归函数,时间复杂度O(N),额外空间复杂度O(N)
    2.递归函数process将一颗二叉树转换为一个接口特殊的有序双向链表,该双向链表尾节点的next指向双向链表头节点,头节点的pre指向None,最终返回尾节点
    3.但将二叉树左右孩子使用process完成转换并拼接好后,需要将最终尾节点的next指向None
"""
from linked_list import DoubleNode


def convert_to_sequence(tree):
    """
    :type tree:DoubleNode
    :param tree:
    :return:
    """

    def process(children):
        """
        :type children:DoubleNode
        :param children:
        :return:
        """
        if children is None:
            return children
        left_tail = process(children.pre)
        right_tail = process(children.next)
        left_head = left_tail.next if left_tail else None
        right_head = right_tail.next if right_tail else None
        if left_tail and right_tail:
            left_tail.next = children
            children.pre = left_tail
            children.next = right_head
            right_head.pre = children
            right_tail.next = left_head
            return right_tail
        elif left_tail:
            left_tail.next = children
            children.pre = left_tail
            children.next = left_head
            return children
        elif right_tail:
            children.next = right_head
            right_head.pre = children
            right_tail.next = children
            return right_tail
        else:
            children.next = children
            return children

    if tree is None:
        return tree
    last = process(tree)
    result = last.next
    last.next = None
    return result






if __name__ == "__main__":
    pass
