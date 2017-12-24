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
1.给定一个链表的头节点和一个字符串value,删除链表中所有节点值为value的节点
思路：
    1.使用列表保存所有节点值不为value的节点,而后由前至后弹出拼接                                      时间复杂度O(N),额外空间复杂度O(N)
    2.直接原链表修改,找到第一个节点值不为value的节点设为新链表头节点,而后遍历删除所有节点值为value的节点    时间复杂度O(N),额外空间复杂度O(1) 
2.给定一个链表的节点node,但是不给整个链表的头节点,如何在链表中删除node,并分析这么做会有那些问题
思路：
    1.将node的指复制为node.next的值,而后删除删除node.next
    2.单node为链表尾节点时,无法删除
    3.实际工程中每个节点可能代表很复杂的结构,节点值复制或是节点值改变都可能禁止,应该这可能涉及很多依赖关系
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


def remove_node(node):
    """
    :type node:Node
    :param node:
    :return:
    """
    if node is None:
        return
    next = node.next
    if next is None:
        node.value = None
    else:
        node.value = next.value
        node.next = next.next


if __name__ == "__main__":
    pass
