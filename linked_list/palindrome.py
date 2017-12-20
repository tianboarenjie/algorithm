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
@File:              palindrome.py 
@Time:              17-12-20 下午10:06 
"""
"""
判断一个链表是否为回文
1.利用栈压入链表所有节点,判断栈和链表数据是否一致,一致则为回文,否则不是
2.也是利用栈,但是只压入一半,而后判断栈中数据和链表左半部分是否一致
3.不依赖栈及其它数据结构,仅使用原链表以及几个变量
    1.查找链表中间节点,反转右半部分数据节点,记为node2
    2.左半部分链表node1和右半部分链表node2同时向中间节点移动,比较节点值判断是否为回文
    3.不论是否为回文均恢复链表原来结构
"""
from linked_list import Node

def is_palindrome(head):
    """
    判断是否为回文
    :type head: Node
    :param head:
    :return: True or False
    """
    if head is None or head.next is None:
        return True
    node1 = head
    node2 = head.next
    while node2 is not None and node2.next is not None:
        # 若链表个数为奇数时,中间节点将不需要比较
        node1 = node1.next
        node2 = node2.next.next
    node2 = node1.next
    node1.next = None
    tmp = None
    while node2 is not None:
        # 链表右半部分反转
        tmp = node2.next
        node2.next = node1
        node1 = node2
        node2 = tmp
    node2 = node1
    tmp = head
    result = True
    while tmp is not None and node2 is not None:
        if tmp.value != node2.value:
            result = False
            break
        tmp = tmp.next
        node2 = node2.next
    node2 = node1.next
    node1.next = None
    while node2 is not None:
        node3 = node2.next
        node2.next = node1
        node1 = node2
        node2 = node3
    return result

if __name__ == "__main__":
    pass
