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
@File:              sort.py 
@Time:              17-12-24 上午11:33 
"""
"""
给定一个无序单链表头节点head,实现单链表选择排序,要求额外空间复杂度为O(1)
思考：
    1.默认开始整个单链表都是为排序部分,找到第一个最小节点,记为head
    2.每次找到最小节点,都将该节点保存并在原单链表中删除它,而后拼接到排序好的节点尾部
"""
from linked_list import Node


def select_sort(head):
    """
    :type head:Node
    :param head:
    :return:
    """

    def get_min_pre_node(node):
        """
        找到最小值节点的前一个节点
        :param node:
        :return:
        """
        pre_min = None
        min = node
        pre_cur = node
        cur = node.nexlt
        while cur:
            if cur.value < min.value:
                pre_min = pre_cur
                min = cur
            pre_cur = cur
            cur = pre_cur.next
        return pre_min


    if head is None or head.next is None:
        return head
    tail = None
    cur = head
    while cur:
        min = cur
        min_pre = get_min_pre_node(cur)
        if min_pre:
            min = min_pre.next
            min_pre.next = min.next
        cur = cur if cur == min else cur.next
        if tail is None:
            head = min
        else:
            tail.next = min
        tail = min
    return head


if __name__ == "__main__":
    pass
