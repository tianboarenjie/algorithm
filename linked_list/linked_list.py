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
@File:              linked_list.py 
@Time:              17-12-5 下午10:20 
"""
__all__ = ["Node", "DoubleNode"]
import copy
import math


class Node:

    __slots__ = ["__value", "__next"]

    def __init__(self, value):
        self.__value = value
        self.__next = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, int) and value in range(0, 10):
            self.__value = value
        else:
            raise TypeError("must be int object, greater than 0 and less than 10!")

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    def reverse(self):
        """
        实现时间复杂度为O(N),额外空间复杂度为O(1)的链表反转(不包括深拷贝)
        :return:
        """
        cp = copy.deepcopy(self)
        pre = None
        next = None
        while cp is not None:
            next = cp.next
            cp.next = pre
            pre = cp
            cp = next
        return pre

    def remove_middle(self):
        """
        删除链表中间节点,返回新链表
        定义两个遍历节点pre和cur,pre一个后移一个节点,cur一次后移两个节点
        :return:
        """
        if self is None or self.next is None:
            return self
        if self.next.next is None:
            return self.next
        result = copy.deepcopy(self)
        pre = result
        cur = result.next.next
        while cur.next is not None and cur.next.next is not None:
            pre = pre.next
            cur = cur.next.next
        pre.next = pre.next.next
        return result

    def remove_ratio(self, a, b):
        if a < 1 or a > b:
            return self
        size = 0
        cur = self
        while cur is not None:
            size += 1
            cur = cur.next
        k = math.ceil(a*size/b)
        if k == 1:
            return self.next
        if k > 1:
            result = copy.deepcopy(self)
            cur = result
            k -= 1
            while k != 1:
                k -= 1
                cur = cur.next
            cur.next = cur.next.next
            return result

    def remove_reciprocal(self, k):
        """
        删除单链表中倒数第k个节点（源链表不变）
        遍历单链表,同时k递减,根据遍历完成后的k值判断需要删除的倒数第k个节点,n为单链表长度
            1.k大于0,表明倒数第k个节点不存在,直接返回原单链表
            2.k等于0,表明倒数第k个节点就是单链表头节点,返回self.next即可
            3.k小于0,可知需要删除的节点的前一个节点是n-k-1个节点,第一次遍历k的值是k-n,故此第二次遍历到k不断加1直至为0时即可
        :type k: int
        :param k:
        :return:
        """
        if self is None or k < 1:
            return self
        cur = self
        while cur is not None:
            cur = cur.next
            k -= 1
        cur = copy.deepcopy(self)
        if k == 0:
            cur = cur.next
        if k < 0:
            tmp = cur
            while k+1 != 0:
                k += 1
                tmp = tmp.next
            tmp.next = tmp.next.next
        return cur


class DoubleNode:

    __slots__ = ["__value", "__pre", "__next"]

    def __init__(self, value):
        self.__value = value
        self.__pre = None
        self.__next = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            self.__value = value
        else:
            raise TypeError("must be int object!")

    @property
    def pre(self):
        return self.__pre

    @pre.setter
    def pre(self, pre):
        self.__pre = pre

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    def reverse_part(self, start, end):
        """
        部分反转,start为反转起始,end为反转结束
        1.判断1<=start<=end<=len,不满足直接返回self
        2.找到start-1个节点node_pre和end+1个节点node_next,node_pre标记需要反转部分的前一个节点,
          node_next标记需要反转部分的下一个节点,此时将整个链表分为头(末尾节点为node_pre),cur(需要反转部分)
          和尾(头节点为node_next)
        :param start:
        :param end:
        :return:
        """
        len = 0
        cp = copy.deepcopy(self)
        tmp = cp
        node_pre = None
        node_next = None
        while tmp is not None:
            len += 1
            node_pre = tmp if len == start-1 else node_pre
            node_next = tmp if len == end+1 else node_next
            tmp = tmp.next
        cur = cp if node_pre is None else node_pre.next
        node = cur.next
        cur.next = node_next
        tmp = None
        while node != node_next:
            tmp = node.next
            node.next = cur
            cur = node
            node = tmp
        if node_pre is not None:
            node_pre.next = cur
            return cp
        return cur

    def reverse(self):
        """
        实现时间复杂度为O(N),额外空间复杂度为O(1)的链表反转(不包括深拷贝)
        :return:
        """
        cp = copy.deepcopy(self)
        pre = None
        next = None
        while cp is not None:
            next = cp.next
            cp.next = pre
            cp.pre = next
            pre = cp
            cp = next
        return pre

    def remove_reciprocal(self, k):
        """
        删除双链表中倒数第k个节点,此次使用第二种方法快速删除链表中倒数第k个节点（原链表不变）
        设置两个指针,fast和slow,fast先走k步,而后slow再与fast同步后移
            1.如果fast走不到k步,表明双链表长度不够,直接返回
            2.如果fast走到第k个节点,且好是None,表明双链表长度且好为k,返回self.next
            3.fast和slow同步向后移动,直到fast移动到最后一个节点(不为None),
              此时slow就是倒数第k个节点的前一个节点
        :param k:
        :return:
        """
        if self is None or k < 1:
            return self
        # fast预先遍历到第k个节点
        fast = self
        while k > 0:
            if fast == None:
                return self
            else:
                fast = fast.next
            k -= 1
        if fast is None:
            cur = copy.deepcopy(self)
            cur = cur.next
            cur.pre = None
        cur = copy.deepcopy(self)
        slow = cur
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        if slow.next is not None:
            slow.next.pre = slow
        return cur
