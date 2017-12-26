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
@File:              convert.py 
@Time:              17-12-24 上午10:47 
"""
"""
1.对于搜索二叉树（该树左孩子都比头节点小,该树的右孩子都比头节点大）而言,有本身值域,也有指向左孩子（left）和右孩子（right）的指针,对于双向链表节点来说,
  也有本身值域,以及指向上一个节点(pre)和下一个节点的指针(next)的指针,二叉树和双向链表在结构上有很打相似之处,请实现一个函数完成搜索二叉树到有序双向链表的转换
  思路：
    1.使用递归函数,时间复杂度O(N),额外空间复杂度O(N)
    2.递归函数process将一颗二叉树转换为一个接口特殊的有序双向链表,该双向链表尾节点的next指向双向链表头节点,头节点的pre指向None,最终返回尾节点
    3.但将二叉树左右孩子使用process完成转换并拼接好后,需要将最终尾节点的next指向None
2.给定单链表头节点head,链表长度为N,如果N为整数,那么前N/2为左半区后N/2为右半区,如果N为奇数,那么前N/2为左半区后N/2+1为右半区,左半区由左至右记为L1->L2...
  右半区由左至右记为R1->R2...,将单链表调整为L1->R1->L2->R2...的形式            
  要求：时间复杂度为O(N),额外空间复杂度为N(1)
  思路：
    1.找到中间节点min,及右半区开始节点right为中间节点的next,也即right=mid.next,再将mid.next置None将左半区和右半区隔开
    2.左半区left从头节点开始遍历直到None,每次从左半区拼接一个节点再从右半区拼接一个节点
"""
from linked_list import Node
from linked_list import DoubleNode


def convert_to_sequence(tree):
    """
    :type tree:DoubleNode
    :param tree:
    :return:
    """

    def process(children):
        """
        :type children:DoubleNode
        :param children:
        :return:
        """
        if children is None:
            return children
        left_tail = process(children.pre)
        right_tail = process(children.next)
        left_head = left_tail.next if left_tail else None
        right_head = right_tail.next if right_tail else None
        if left_tail and right_tail:
            left_tail.next = children
            children.pre = left_tail
            children.next = right_head
            right_head.pre = children
            right_tail.next = left_head
            return right_tail
        elif left_tail:
            left_tail.next = children
            children.pre = left_tail
            children.next = left_head
            return children
        elif right_tail:
            children.next = right_head
            right_head.pre = children
            right_tail.next = children
            return right_tail
        else:
            children.next = children
            return children

    if tree is None:
        return tree
    last = process(tree)
    result = last.next
    last.next = None
    return result


def relocate(head):
    """
    :type head:Node
    :param head:
    :return:
    """

    def mergeLR(left, right):
        """
        :type left:Node
        :type right:Node
        :param left:
        :param right:
        :return:
        """
        while left.next:
            follow = right.next
            right.next = left.next
            left.next = right
            left = right.next
            right = follow
        left.next = right

    if head is None or head.next is None:
        return head
    mid = head
    right = mid.next
    while right.next and right.next.next:
        mid = mid.next
        right = right.next.next
    right = mid.next
    mid.next = None
    mergeLR(head, right)


if __name__ == "__main__":
    pass
