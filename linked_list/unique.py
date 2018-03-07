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
@File:              unique.py 
@Time:              17-12-23 下午10:37 
"""
"""
给定一个无序单链表头节点head,删除其中重复出现的节点
思路：
    1.使用列表存放节点值,遍历节点发现节点值在列表中即删除,不在则将节点值存入列表,继续遍历    时间复杂度O(N),额外空间复杂度O(N)
    2.每遍历一个节点,删除节点后与该节点值相同的节点                                   时间复杂度O(N^2),额外空间复杂度O(1)
"""
from linked_list import Node


def unique_depend_list(head_node):
    """
    依赖列表保存链表所有的惟一值
    :type head_node:Node
    :param head_node:
    :return:
    """
    if head_node is None or head_node.next is None:
        return head_node
    pre = head_node
    cur = head_node.next
    tmp = [pre.value]
    while cur:
        if cur.value in tmp:
            pre.next = cur.next
        else:
            tmp.append(cur.value)
            pre = cur
        cur = cur.next
    return head_node


def unique_by_sort(head_node):
    """
    :type head_node:Node
    :param head_node:
    :return:
    """
    if head_node is None or head_node.next is None:
        return head_node
    cur = head_node
    while cur:
        pre = cur
        follow = pre.next
        while follow:
            if follow.value == cur.value:
                pre.next = follow.next
            else:
                pre = follow
            follow = pre.next
        cur = cur.next
    return head_node

if __name__ == "__main__":
    pass
