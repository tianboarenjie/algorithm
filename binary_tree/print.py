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
@File:              print.py 
@Time:              17-12-31 下午5:31 
"""
"""
a.给定一棵二叉树后节点tree,分别实现按层打印和ZigZag打印
按层打印：                       ZigZag打印
Level 1: 1                     Level 1 from left to right: 1
Level 2: 2 3                   Level 2 from right to left: 2 3
Level 3: 4 5 6                 Level 3 from left to right: 4 5 6
Level 4: 7 8                   Level 4 from right to left: 7 8
    按层打印：
        1.利用列表保存需要打印层的节点
        2.如何标记没一行打印完,利用last记录每一行最后一个节点
    ZigZag打印：
        1.利用双栈队列保存需要打印的下一层节点
        2.左到右：从node_deque头部弹出节点node,依次判断node的左孩子右孩子,存在则从队尾放入node_deque
        3.右到左：从node_deque尾部弹出节点node,以此判断node的右孩子左孩子,存在则从头部放入node_deque
        4.打印顺序改变：下一层最后打印的是单前层有孩子的节点最先进入node_deque的节点
"""
from binary_tree import Node
from collections import deque


def print_by_level(tree):
    """
    按层打印二叉树个节点
    :type tree:Node
    :param tree:
    :return:
    """
    if not tree:
        return
    tmp = [tree]
    last = tree
    level = 1
    node_last = None
    print("Level %s: " % level)
    while tmp:
        tree = tmp.pop(0)
        print("%s " % tree.value, end="")
        if tree.left:
            tmp.append(tree.left)
            node_last = tree.left
        if tree.right:
            tmp.append(tree.right)
            node_last = tree.right
        if tree == last and tmp:
            level += 1
            print("Level %s: " % level)
            last = node_last


def print_by_zigzag(tree):
    """
    曲折答应二叉树各层节点值
    :type tree:Node
    :param tree:
    :return:
    """

    if not tree:
        return
    node_deque = deque([tree])
    level = 1
    left = True
    last = tree
    level_last = None
    print("Level %s from %s:" % (level, "left to right: " if left else "right to left: "), end="")
    while node_deque:
        if left:
            tree = node_deque.popleft()
            if tree.left:
                level_last = tree.left if not level_last else level_last
                node_deque.append(tree.left)
            if tree.right:
                level_last = tree.right if not level_last else level_last
                node_deque.append(tree.right)
        else:
            tree = node_deque.pop()
            if tree.right:
                level_last = tree.right if not level_last else level_last
                node_deque.appendleft(tree.right)
            if tree.left:
                level_last = tree.left if not level_last else level_last
                node_deque.appendleft(tree.left)
        print("%s " % tree.value, end="")
        if tree == last and node_deque:
            left = not left
            last = level_last
            level_last = None
            level += 1
            print("")
            print("Level %s from %s:" % (level, "left to right: " if left else "right to left: "), end="")
            print("")


if __name__ == "__main__":
    pass
