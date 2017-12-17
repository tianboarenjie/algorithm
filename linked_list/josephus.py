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
@File:              josephus.py 
@Time:              17-12-17 下午9:55 
"""
"""
据说著名犹太历史学家Josephus有过如下故事：在罗马人占领乔塔帕特后,39个犹太人和Josephus及他的朋友躲进一个洞里,
39个犹太人决定宁愿死也不要被敌人抓到,于是决定了一个自杀方式,41个人排成一个圆圈,由第一个人开始报数,报数到3的人就自杀,
再由下一个人重新报1,报数到3的人就自杀,这样依次下去,直到剩下最后一个人时,那个人可以自由选择自己的命运.这就是著名的约瑟夫问题.
现在请用单向链表描述该结构并呈现整个自杀过程
    1.环形链表为空,链表节点个数为1时或是m小于1,不用调整直接返回
    2.环形链表中遍历每个节点,不断让每个节点报数,当到达m时，删除该节点
    3.删除之后把剩下节点继续连成环状,继续报数删除(重复1和2步),直到只剩下1个节点
进阶：如果链表节点数为N,想在时间复杂度为O(N)时完成原问题的要求,该怎么实现？
    1.普通解法时间复杂度为O(n*m),需要遍历m次删除节点数为n-1,之所以花费这么多时间是因为不知道最终哪个节点会存活下来,所以改进
    解法就是快速找到最总存货的节点,直接返回即可.
    2.
"""
import copy
from linked_list import Node


def common_josephus(head, m):
    """
    约瑟夫问题普通解决方法,没有优化的方案
    :type head:Node
    :param head: 环状Node链表
    :param m:
    :return:
    """
    if head is None or head.next is head or m == 1:
        return head
    tmp = copy.deepcopy(head)
    last = tmp
    while last.next != tmp:
        last = last.next
    count = 0
    while tmp != last:
        count += 1
        if count == m:
            print("%s will be killed" % tmp.value)
            last.next = tmp.next
            count = 0
        else:
            last = last.next
        tmp = last.next
    return tmp


def advance_josephus(head, m):

    def get_result(l, i):
        if l == 1:
            return 1
        return (get_result(l-1, m) + m - 1) % i + 1

    if head is None or head.next is head or m < 1:
        return head
    cur = head.next
    size = 1
    while cur is not None:
        size += 1
        cur = cur.next
    result = get_result(size, m)-1
    while result != 0:
        head = head.next
    head.next = head
    return head


if __name__ == "__main__":
    pass
