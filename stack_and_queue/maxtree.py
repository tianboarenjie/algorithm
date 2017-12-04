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
@File:              maxtree.py 
@Time:              17-12-4 下午9:25 
"""
"""
数组中没有重复元素,设计一个方法,创建一个二叉数tree,tree的没一个节点对应一个数组一个值,包括tree在内的每一棵二叉树在内,最大节点都是数的头
思路：
每一个数的父节点是它左边第一个比它的数和它右边第一个比它大的数中较小的那一个
"""

class Node:
    """
    二叉树节点
    """

    __slots__ = ["__value", "__left", "__right"]

    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right

    def value(self):
        return self.__value


def get_max_tree(ori_list):
    nodes = [Node(ori_list[i]) for i in range[len(ori_list)]]
    lb_dict = {}
    rb_dict = {}
    stack = []
    for i in range(len(nodes)):
        cur_node = nodes[i]
        while stack and stack[-1].value() < cur_node.value():
            # cur = stack.pop()
            # lb_dict[cur] = stack[-1] if stack else None
            # rb_dict[cur] = cur_node
            pop_stack_to_map(stack, lb_dict)
        stack.append(cur_node)
    while stack:
        # cur = stack.pop()
        # lb_dict[cur] = stack[-1] if stack else None
        # rb_dict[cur] = None
        pop_stack_to_map(stack, lb_dict)

    for i in range(len(nodes)-1,-1,-1):
        cur_node = nodes[i]
        while stack and stack[-1].value() < cur_node.value():
            pop_stack_to_map(stack, rb_dict)
        stack.append(cur_node)
    while stack:
        pop_stack_to_map(stack, rb_dict)

    head = None
    for i in range(len(nodes)):
        cur_node = nodes[i]
        left = lb_dict.get(cur_node)
        right = rb_dict.get(cur_node)
        if left is None and right is None:
            head = cur_node
        elif left is None:
            if right.left is None:
                right.set_left(cur_node)
            else:
                right.set_right(cur_node)
        elif right is None:
            if right.left is None:
                right.set_left(cur_node)
            else:
                right.set_right(cur_node)
        else:
            parent = left if left.value() < right.value() else right
            if parent.left is None:
                parent.set_left(cur_node)
            else:
                parent.set_right(cur_node)
    return head


def pop_stack_to_map(tmp_stack, tmp_dict):
    pop_node = tmp_stack.pop()
    tmp_dict[pop_node] = tmp_stack[-1] if tmp_stack else None
