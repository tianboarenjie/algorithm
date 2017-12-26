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
@File:              knodesreverse.py 
@Time:              17-12-23 下午5:08 
"""
"""
给定一个单链表的头节点,实现一个调整单链表的函数,使得每k个节点之间逆序,如果一组不够k个节点则该组不逆序
输入：1->2->3->4->5->6->7->8->None    k=3
返回：3->2->1->6->5->4->7->8->None 
思路：
    1.利用栈（列表）保存每组k个节点,将每次遍历k个节点（不够直接返回）,将原单链表拆分成pre（已经按照要求完成了逆序）,cur_list（当前需要逆序的列表:k个节点）,next（还未进行逆序）,
      压入而后弹出拼接至对应位置（完成逆序pre的最后一个节点）,额外空间复杂度为O(N)
    2.直接在原单链表上处理,过程类似使用栈,不过只需要传入当前组的第一个节点的前一个节点和最后一个节点,额外空间复杂度O(1)
"""
from linked_list import Node


def reverse_depend_list(head_node, k):
    """
    :type head_node:Node
    :param head_node:
    :param k:
    :return:
    """

    def reverse_depend_list_resign(pre_node, cur_list, next_node):
        """
        :type pre_node:Node
        :type cur_list:list
        :type next_node:Node
        :param pre_node:
        :param cur_list:
        :param next_node:
        :return:
        """
        cur = cur_list.pop()
        if pre_node is not None:
            pre_node.next = cur
        while len(cur_list):
            follow = cur_list.pop()
            cur.next = follow
            cur = follow
        cur.next = next_node
        return cur

    if k < 2 or head_node is None:
        return head_node
    cur_list = []
    pre = None
    result = head_node
    cur = head_node
    while cur:
        next = cur.next
        cur_list.append(cur)
        if len(cur_list) == k:
            pre = reverse_depend_list_resign(pre, cur_list, next)
            # 获取需要返回的结果的头节点
            result = cur if result == head_node else result
        cur = next
    return result


def reverse(head_node, k):
    """

    :type head_node:Node
    :param head_node:
    :param k:
    :return:
    """
    def reverse_resign(pre_node, start_node, end_node):
        """
        :type pre_node:Node
        :type start_node:Node
        :type end_node:Node
        :param pre_node:
        :param start_node:
        :param end_node:
        :return:
        """
        cur = start_node.next
        start_node.next = end_node.next
        while cur != end_node:
            follow = cur.next
            cur.next = start_node
            start_node = cur
            cur = follow
        if pre_node is not None:
            pre_node.next = end_node

    if k < 2 or head_node is None:
        return head_node
    count = 0
    cur = head_node
    pre = None
    while cur:
        count += 1
        follow = cur.next
        if count == k:
            start = head_node if pre is None else pre.next
            reverse_resign(pre, start, follow)
            pre = start
            count = 0
        cur = follow
    return head_node


if __name__ == "__main__":
    pass
