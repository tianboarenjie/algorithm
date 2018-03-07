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
@File:              intersection.py 
@Time:              17-12-21 下午10:49 
"""
"""
单链表可能有环也可能无环,给定两个单链表的头节点head1和head2,这两个单链表可能相交也可能不相交,如果两单链表相交则返回相交部分地一个节点,否则返回null
要求:head1长度N,head2长度M,时间复杂度为N(N+M),额外空间复杂度为N(1)
思路：
    1.首先思考如果两个单链表相交,要么都无环要么都有环,不肯能出现一个有环一个无环的单链表相交（单链表节点仅有一个next指向）
    2.如何判断一个单链表有环,有环返回进入环的第一个节点,否则返回None
        a.如果一个链表有环,遍历这个链表将无休止在环里转下去,可依据这个特性判断
        b.可设置两个指针slow和fast,每次移动slow向下移动一个位置,fast向下移动两个位置,若无环或是fast到达链表尾部,此时直接返回None
        c.若有环则会在环内某个位置fast与slow相遇,此时fast重新指向链表头节点
        d.接下来slow和fast指针每次都向后移动一个位置,slow和fast一定会再次相遇,这个相遇节点就是入环第一个节点
    3.如何判断两个无环单链表是否相交
        a.如果两个无环单链表会相交,则两个无环单链表最后一个节点必然相同,可依据从判断两个无环单链表是否相交
        b.两单链表相交部分相同,结尾都是最后一个节点,两节点较长节点长度为len1,较短节点为len2,较长单链表可直接先走len1-len2步,而后一起想下移动一个位置判断是否走到一起
    4.如何判断两个有环单链表是否相交
        a.通过判断单链表是否有环会的到第一次入环的节点,单两个单链表第一次入环节点相同时,此时转换为3相似（3遍历结束标志以None,此时遍历结束标志为入环节点）
        b.如果两单链表入环节点不同,此时两单链表可能相交也可能不相交,如果从一个入环节点向下移动(结束标志为返回原位置),可以到达另一个入环节点表明两有环单链表相交
          返回任意入环节点即可,如果不能到达另一入环节点,则两单链表没有相交,直接返回None
"""
from linked_list import Node


def get_loop_node(head_node):
    """
    根据上面思考完成对一个单链表入环的第一个节点
    :type head_node:Node
    :param head_node:
    :return:
    """
    if head_node is None or head_node.next is None or head_node.next.next is None:
        return None
    slow = head_node.next
    fast = head_node.next.next
    while fast != slow:
        if fast.next is None or fast.next.next is None:
            return None
        fast = fast.next.next
        slow = slow.next
    fast = head_node
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast


def get_node_with_noloop(head_node1, head_node2):
    """
    判断得到两个无环单链表相交的第一个节点
    :type head_node1:Node
    :type head_node2:Node
    :param head_node1:
    :param head_node2:
    :return:
    """
    if head_node1 is None or head_node2 is None:
        return None
    cur1 = head_node1
    cur2 = head_node2
    lnh = 0
    while cur1.next:
        cur1 = cur1.next
        lnh += 1
    while cur2.next:
        cur2 = cur2.next
        lnh -=1
    if cur1 != cur2:
        return None
    # 默认cur1指向较长单链表,cur2指向较短单链表
    cur1 = head_node1 if lnh > 0 else head_node2
    cur2 = head_node2 if cur1 == head_node1 else head_node1
    lnh = abs(lnh)
    while lnh:
        cur1 = cur1.next
        lnh -= 1
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1


def get_node_with_loop(head_node1, loop_node1, head_node2, loop_node2):
    """
    根据上面逻辑得到两个有环单链表相交地一个节点
    :type head_node1:Node
    :type loop_node1:Node
    :type head_node2:Node
    :type loop_node2:Node
    :param head_node1:第一个单链表头节点
    :param loop_node1:第一个单链表中入环的第一个节点
    :param head_node2:第二个单链表头节点
    :param loop_node2: 第二个单链表中入环的第一个节点
    :return:
    """
    cur1 = head_node1
    cur2 = head_node2
    if loop_node1 == loop_node1:
        lnh = 0
        while cur1 != loop_node1:
            lnh += 1
            cur1 = cur1.next
        while cur2 != loop_node2:
            lnh -= 1
            cur2 = cur2.next
        # cur1指向长单链表cur2指向短单链表
        cur1 = head_node1 if lnh > 0 else head_node2
        cur2 = head_node2 if cur1 == head_node1 else head_node1
        lnh = abs(lnh)
        while lnh:
            cur1 = cur1.next
            lnh -= 1
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = loop_node1.next
        while cur1 != loop_node1:
            if cur1 == loop_node2:
                return cur1
                # return cur2
            cur1 = cur1.next
        return None


def get_intersection_node(head_node1, head_node2):
    """
    通过判断两节点是否有环调用不同求解函数
    :type head_node1:Node
    :type head_node2:Node
    :param head_node1:
    :param head_node2:
    :return:
    """
    if head_node1 is None or head_node2 is None:
        return None
    loop_node1 = get_loop_node(head_node1)
    loop_node2 = get_loop_node(head_node2)
    if loop_node1 and loop_node2:
        return get_node_with_loop(head_node1, loop_node1, head_node2, loop_node2)
    if loop_node1 is None and loop_node2 is None:
        return get_node_with_noloop(head_node1, head_node2)
    return None


if __name__ == "__main__":
    pass
