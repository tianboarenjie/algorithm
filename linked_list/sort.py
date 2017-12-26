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
1.给定一个无序单链表头节点head,实现单链表选择排序,要求额外空间复杂度为O(1)
  思考：
    1.默认开始整个单链表都是为排序部分,找到第一个最小节点,记为head
    2.每次找到最小节点,都将该节点保存并在原单链表中删除它,而后拼接到排序好的节点尾部
2.给定两个升序有序单链表head1和head2,合并两有序链表保证合并后的依旧有序,并返回合并后链表头节点
  思考：
    1.只要两个有序列表有一个为None则不需要合并,直接返回另一个链表即可
    2.head1和head2头节点更小的记为result,last记为result的尾节点
    3.便利head1和head2节点,将last的next指向较少值,该链表后移一个位置
    4.单两个链表有个一为空,将last的next指向另一个非空链表,返回result
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


def merge(head1, head2):
    """
    和并两升序有序链表
    :type head1:Node
    :type head2:Node
    :param head1:
    :param head2:
    :return:
    """
    if head1 is None or head2 is None:
        return head1 if head2 is None else head2
    result = head1 if head1.value < head2.value else head2
    last = result
    cur1 = head1
    cur2 = head2
    while cur1 and cur2:
        if cur1.value < cur2.value:
            last.next = cur1
            last = last.next
            cur1 = cur1.next
        else:
            last.next = cur2
            last = last.next
            cur2 = cur2.next
    last.next = cur1 if cur1 else cur2
    return result


if __name__ == "__main__":
    pass
