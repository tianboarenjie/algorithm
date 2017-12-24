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
@File:              add.py 
@Time:              17-12-21 下午9:28 
"""
"""
1.链表中每个节点均为0-9之间的整数,链表即代表一个整数
  给定两个此种链表的头节点head1和head2,计算两个链表代表整数相加结果值的链表
  思路：
    1.得到两个链表代表的整数,直接相加后将结果创建为链表(结果可能会溢出)
    2.利用两个盏(列表)保存链表每个节点值,而后两个盏同位置整数相加将结果放到新链表中(注意进位)
    3.两链表反转,同位置节点整数相加将结果放到新链表中(注意进位)
2.一个环形单链表从头节点head开始降续,同时由尾节点指回头节点,给定这样单链表头节点head和整数num,生成值为num的新节点并插入到环形链表中,依旧有序
  思路：
    1.根据num生成节点node
    2.判断head是否为空,为空直接返回node
    3.遍历查找位置,pre=head,cur=pre.next,当pre.value>num且cur.value<num时,即node应该插入到pre的后面,cur的前面
    4.如果没有找到这样的位置,也即应该在环尾
"""
import math
from linked_list import Node


def add_depend_list(head1, head2):
    """
    利用列表(栈)实现链表节点值相加
    :type head1:Node
    :type head2:Node
    :param head1:
    :param head2:
    :return:
    """
    head1_list = []
    head2_list = []
    while head1:
        head1_list.append(head1.value)
        head1 = head1.next
    while head2:
        head2_list.append(head2.value)
        head2 = head2.next
    carry = 0
    result = None
    while head1_list or head2_list:
        h1 = head1_list.pop() if head1_list else 0
        h2 = head2_list.pop() if head2_list else 0
        sun = h1 + h2 + carry
        node = result
        result = Node(sun%10)
        result.next = node
        carry = math.floor(sun/10)
    # 最后可能有进位
    if carry:
        node = result
        result = Node(1)
        result.next = node
    return result


def add_depend_reverse(head1, head2):
    """
    利用链表翻转实现链表节点值相加
    :type head1:Node
    :type head2:Node
    :param head1:
    :param head2:
    :return:
    """
    head1_reverse = head1.reverse()
    head2_reverse = head2.reverse()
    carry = 0
    result = None
    while head1_reverse or head2_reverse:
        h1 = head1_reverse.value if head1_reverse else 0
        h2 = head2_reverse.value if head2_reverse else 0
        sun = carry + h1 + h2
        carry = math.floor(sun/10)
        node = result
        result = Node(sun%10)
        result.next = node
        head1_reverse = head1_reverse.next if head1_reverse else None
        head2_reverse = head2_reverse.next if head2_reverse else None
    # 最后可能有进位
    if carry:
        node = result
        result = Node(1)
        result.next = node
    return result


def ring_insert_num(head, num):
    """
    :type head:Node
    :param head:
    :param num:
    :return:
    """
    if num is None:
        return head
    node = Node(num)
    if head is None:
        node.next = node
        return node
    pre = head
    cur = pre.next
    while cur != head:
        if pre.value <= num and cur.value >= num:
            break
        pre = cur
        cur = pre.next
    node.next = cur
    pre.next = node
    return head if num < head.value else node


if __name__ == "__main__":
    pass
