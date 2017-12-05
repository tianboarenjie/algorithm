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
@File:              common.py 
@Time:              17-12-5 下午9:51 
"""
"""
给定两个有序链表头指针head1和head2,打印两个链表共有部分
"""
from linked_list import Node


def print_common_part(head1, head2):
    """
    :type head1: Node
    :type head2: Node
    :param head1:
    :param head2:
    :return:
    """
    if head1 is None or head2 is None:
        return
    print("Common Part:")
    while head1 is not Node or head2 is not Node:
        if head1.value < head2.value:
            head1 = head1.next
        elif head1.value > head2.value:
            head2 = head2.next
        else:
            print(head2.value, end=" ")
            head1 = head1.next
            head2 = head2.next
    print("Common Part End")
