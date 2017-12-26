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
@File:              partition.py
@Time:              17-12-20 下午11:36 
"""
"""
将单向链表按某值划分成左边小,中间相等,右边大的形式
9->0->4->5->1 pivot=4   ----->   0->1->4->9->5
如果链表长度为N,要求时间复杂度达到O(N),额外空间复杂度达到O(1)

思路：将原链表拆分成三个链表,小值链表等值链表和大值链表,而后拼接起来
"""
import copy
from linked_list import Node

def partition_by_pivot(head, pivot):
    """
    将链表按照某个值划分成左边小,中间相等,右边大的形式
    :type head: Node
    :param head: 需要划分的链表
    :param pivot: 划分参考
    :return:
    """
    if head is None:
        return head
    ori = copy.deepcopy(head)
    cur = ori
    sma_head = None
    sma_tail = None
    equ_head = None
    equ_tail = None
    big_head = None
    while cur is not None:
        follow = cur.next
        cur.next = None
        if cur.value < pivot:
            if sma_head is None:
                sma_head = cur
                sma_tail = cur
            else:
                sma_head.next = cur
                sma_tail = cur
        elif cur.value == pivot:
            if equ_head is None:
                equ_head = cur
                equ_tail = cur
            else:
                equ_head.next = cur
                equ_tail = cur
        else:
            if big_head is None:
                big_head = cur
            else:
                big_head.next = cur
        cur = follow
    # 按照小值链表->等值链表->大值链表顺序拼接链表
    if sma_tail is not None:
        sma_tail.next = equ_head
        equ_tail = equ_tail if equ_tail is not None else sma_tail
    if equ_tail is not None:
        equ_tail.next = big_head
    # 判断返回链表的头
    if sma_head is not None:
        result = sma_head
    elif equ_head is not None:
        result = equ_head
    else:
        result = big_head
    return result

if __name__ == "__main__":
    pass
