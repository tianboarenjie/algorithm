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

class Node:

    __slots__ = ["__value", "__next"]

    def __init__(self, value):
        self.value = value
        self.next = None

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
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    def remove_reciprocal(self, k):
        """
        删除单链表中倒数第k个节点
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
        self.value = value
        self.pre = None
        self.next = None

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

    def remove_reciprocal(self, k):
        """
        删除双链表中倒数第k个节点,此次使用第二种方法快速删除链表中倒数第k个节点
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
