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
@File:              copy.py 
@Time:              17-12-21 下午8:45 
"""
"""
Node类描述如下,value为节点值,next指针和正常单链表中next指针意义一样指向下一个节点,rand指针指向Node类中新曾值得指针,可能是链表中任意节点,也可能None
给定一个又此类型Node组成的链表头节点,实现一个函数完成将链表中所有结构的复制
要求：不使用额外数据结构,只能用有限几个变量在时间复杂度为O(N)下实现链表所有结构的复制
思路：
    1.普通解放：使用字典
        遍历两次,第一次遍历创建所有节点的拷贝并放入字典中,以原节点的键,拷贝节点为值,{node1:node1`,node2:node2`......}
        第二次遍历连接拷贝节点,next和rand均向字典中查询即可
    2.构建新链表：node1->node1`->node2->node2`......
        遍历三次,第一次遍历构建上面形式链表
        第二次遍历,完成拷贝节点的rand指向,即为cur.rand.next
        第三次遍历,完成拷贝节点的next指向,也即将新链表拆分成原链表和拷贝链表
"""


class Node:

    __slots__ = ["__value", "__next", "__rand"]

    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__rand = Node

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
    def next(self, follow):
        self.__next = follow

    @property
    def rand(self):
        return self.__rand

    @rand.setter
    def rand(self, rand):
        self.__rand = rand


def copy_rand_list(head):
    """
    以思路2完成该链表复制功能
    :type head:Node
    :param head:
    :return:
    """
    if head is None:
        return None
    cur = head
    while cur:
        # 每个节点后插入该节点的拷贝
        follow = cur.next
        cur.next = Node(cur.value)
        cur.next.next = follow
        cur = follow
    cur = head
    cur_copy = None
    while cur:
        # 开始第二次遍历,完成每个拷贝节点cur_copy的rand指向
        follow = cur.next.next
        cur_copy = cur.next
        cur_copy.rand = cur.rand.next if cur.rand else None
        cur = follow
    # 记录拷贝节点的头节点
    result = head.next
    cur = head
    while cur:
        # 第三次遍历,完成拷贝节点的next指向,拆分新构链表
        follow = cur.next.next
        cur_copy = cur.next
        cur_copy.next = follow.next if follow else None
        cur.next = follow
        cur = follow
    return result


if __name__ == "__main__":
    pass
