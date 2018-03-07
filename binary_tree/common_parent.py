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
@File:              common_parent.py 
@Time:              18-1-2 上午11:17 
"""
"""
a.给定一棵二叉树头节点tree,以及这棵树两个节点node1和node2
    普通：返回node1和node2最近公共祖先节点
        思路：
            1.发现cur为None或是为node1或是node2,返回cur
            2.如果左右孩子都为空,说明在cur这棵树上没有发现node1和node2,返回None
            3.利用后序遍历查询cur的左右孩子,如果都有返回说明左右子树分别发现node1或是node2,返回cur
            4.如果查询左右孩子有一个返回节点一个返回None,说明node1和node2有一个为公共祖先
    进阶：如果查询两个节点最近公共祖先操作十分频繁,想法让单条查询的查询时间减少
        思路：
            1.第一次遍历时建立记录方便后续查询,建立node_dict字典,以node为键node的父节点为值,采用前序遍历方便建立
            2.按照node_dict方式建立node1的父节点对应node1_parent,而后以此查询node2的父节点,只要在node1_parent返回
    再进阶：二叉树节点数量为N,查询条目为M,请在时间复杂度为O(N+M)内完成查询并返回结果
    
b.一个Query实例表示一条查询语句,表示想要查询node1和node2最近公共祖先节点,给定一棵二叉树头节点tree一个Query类型列表,返回Node类型的数组result
  以此表示query[i].node1和query[i].node2的最近公共祖先.如果而茶树节点数为N,查询语句条数M,整个处理过程时间复杂度要求达到O(N+M)
  
"""
from binary_tree import Node


class Query:
    """
    # TODO (programme at 18-1-2): 利用Trajan算法和并查集解决,后续补充
    """

    __slots__ = ["__node1", "__node2"]

    def __init__(self, node1, node2):
        self.__node1 = node1
        self.__node2 = node2

    @property
    def node1(self):
        return self.__node1

    @property
    def node2(self):
        return self.__node2

def lowest_ancestor(tree, node1, node2):
    """
    在tree中找到node1和node2的最近公告祖先
    :type tree:Node
    :type node1:Node
    :type node2:Node
    :param tree:
    :param node1:
    :param node2:
    :return:
    """

    def ancestor(cur, n1, n2):
        """
        :type cur:Node
        :type n1:Node
        :type n2:Node
        :param cur:
        :param n1:
        :param n2:
        :return:
        """
        if cur is None or cur == n1 or cur == n2:
            return cur
        left = ancestor(cur.left, n1, n2)
        right = ancestor(cur.right, n1, n2)
        if left and right:
            return cur
        return left if left else right

    return ancestor(tree, node1, node2)


def lowest_ancestor_depend_record1(tree, node1, node2):
    """
    以来记录在tree中找到node1和node2的最近公告祖先
    :return:
    :type tree:Node
    :type node1:Node
    :type node2:Node
    :param tree:
    :param node1:
    :param node2:
    :return:
    """

    def records(cur, record):
        """
        建立记录
        :type cur:Node
        :type record:dict
        :param cur:
        :param record:
        :return:
        """
        if cur is None:
            return
        if cur.left:
            record[cur.left] = cur
        if cur.right:
            record[cur.right] = cur
        records(cur.left, record)
        records(cur.right, record)

    if tree is None:
        return tree
    node_dict = {}
    records(tree, node_dict)

    node1_parent = {}
    while node1:
        node1_parent[node1] = node_dict.get(node1)
        node1 = node1_parent.get(node1)
    while node1 not in node1_parent.keys():
        node2 = node_dict.get(node2)
    return node2

if __name__ == "__main__":
    pass
