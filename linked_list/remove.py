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
@File:              remove.py 
@Time:              17-12-23 下午11:08 
"""
"""
给定一个链表的头节点和一个字符串value,删除链表中所有节点值为value的节点
思路：
    1.使用列表保存所有节点值不为value的节点,而后由前至后弹出拼接                                      时间复杂度O(N),额外空间复杂度O(N)
    2.直接原链表修改,找到第一个节点值不为value的节点设为新链表头节点,而后遍历删除所有节点值为value的节点    时间复杂度O(N),额外空间复杂度O(1)   
"""
from linked_list import Node


def remove_depend_list(head, value):
    """
    :type head:Node
    :param head:
    :param value:
    :return:
    """
    if head is None or value is None:
        return head
    tmp = []
    while head:
        if head.value != value:
            tmp.append(head)
        head = head.next
    while tmp:
        tmp[-1].next = head
        head = tmp.pop()
    return head


def remove(head, value):
    """
    :type head:Node
    :param head:
    :param value:
    :return:
    """
    if head is None or value is None:
        return head
    while head:
        if head.value != value:
            break
        head = head.next
    pre = head
    cur = pre.next
    while cur:
        if cur.value == value:
            pre.next = cur.next
        else:
            pre = cur
        cur = pre.next
    return head


if __name__ == "__main__":
    pass
