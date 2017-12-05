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
__all__ = ["Node"]
import copy

class Node:

    __slots__ = ["_value", "_next"]

    def __init__(self, value):
        self._value = value
        self._next = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            self._value = value
        else:
            raise TypeError("must be int object!")

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

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
