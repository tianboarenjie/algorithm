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
@File:              contain.py 
@Time:              18-1-1 上午11:51 
"""
"""
a.给定彼此独立两棵二叉树头节点tree1和tree2,判断tree1树是否包含tree2
    思路：
        1.利用递归判断依次tree1头节点和tree2判断,而后tree1左孩子树与tree2判断最后tree1右孩子树与tree2判断
        
b.给定彼此独立两棵二叉树头节点tree1和tree2,判断tree1中是否含有tree2树拓扑结构完全相同的子树（一定要是完整子树）
    思路1：
        1.利用递归判断依次tree1头节点和tree2判断,而后tree1左孩子树与tree2判断最后tree1右孩子树与tree2判断,必须与子树完全相等
    思路2：
        1.利用序列化和反序列化,将tree1转换为序列化字串tree1_str,将tree2转换为u序列化字串tree2_str,判断tree2_str是否在tree1_str内即可
"""
from binary_tree import Node


def contain_topology(tree1, tree2):
    """
    判断tree1中是否包含tree2全部拓扑结构
    :type tree1:Node
    :type tree2:Node
    :param tree1:
    :param tree2:
    :return: bool
    """

    def check(head1, head2):
        """
        判断head1是否包含head2拓扑结构
        :type head1:Node
        :type head2:Node
        :param head1:
        :param head2:
        :return:
        """
        if head2 is None:
            return True
        if head1 is None or head1.value != head2.value:
            return False
        return check(head1.left, head2.left) and check(head1.right, head2.right)

    return check(tree1, tree2) or contain_topology(tree1.left, tree2) or contain_topology(tree1.right, tree2)


def contain_subtree_method1(tree1, tree2):
    """
    判断tree1中是否含有tree2树拓扑结构完全相同的子树,与拓扑不一样,一定要是tree1某个节点的完整子树
    :type tree1:Node
    :type tree2:Node
    :param tree1:
    :param tree2:
    :return:
    """

    def check(head1, head2):
        """
        判断head1是否与head2拓扑结构一样
        :type head1:Node
        :type head2:Node
        :param head1:
        :param head2:
        :return:
        """
        if head1 is None and head2 is None:
            return True
        if (head1 is None and head2) or (head1 and head2 is None) or head1.value != head2.value:
            return False
        return check(head1.left, head2.left) and check(head1.right, head2.right)
    if tree1 is None:
        return False
    return check(tree1, tree2) or contain_subtree_method1(tree1.left, tree2) or contain_subtree_method1(tree1.right, tree2)


def contain_subtree_method2(tree1, tree2):
    """
    判断tree1中是否含有tree2树拓扑结构完全相同的子树,与拓扑不一样,一定要是tree1某个节点的完整子树,利用序列化将tree转换为字串而后判断
    :param tree1:
    :param tree2:
    :return:
    """

    def serialize(head):
        """
        序列化字符串
        :type head:Node
        :param head:
        :return:
        """
        if head is None:
            return "#!"
        result = head.value + "!"
        result += serialize(head.left)
        result += serialize(head.right)
        return result

    tree1_str = serialize(tree1)
    tree2_str = serialize(tree2)
    return tree2_str in tree1_str



if __name__ == "__main__":
    pass
