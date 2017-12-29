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
@File:              edge.py 
@Time:              17-12-26 下午5:08 
"""
"""
给定一棵二叉树头节点tree,按照如下标准返回该二叉树边缘节点（逆时针次序）
标准一：
    1.头节点为边缘节点
    2.叶子节点为边缘节点
    3.如果节点在所在层中最左边或是最右边,那么该节点也是边缘节点
    思路：
        1.左边缘节点从头节点开始,一直访问左孩子,直到左孩子为空
        2.叶子节点从左至右
        3.右边缘节点从头节点开始,一直访问右孩子,直到右孩子为空(注意逆序保存)
标准二：
    1.头节点为边缘节点
    2.叶子节点为边缘节点
    3.树的左边界延伸下去的路径为边缘节点
    4.树的右边界延伸下去的路径为边缘节点
    思路：
        1.定义两个方法,get_left_edge获取左边界延伸路径边缘节点以及左子树的叶子节点,get_right_edge获取右边界延伸路径的边缘节点和右子树的叶子节点
        2.get_left_edge和get_right_edge需要考虑只有路径节点和叶子节点符合要求
"""
from binary_tree import Node


def get_edge1_with_anticlockwise(tree):
    """
    以标准一获取逆时针排序的二叉树边缘节点
    :type tree:Node
    :param tree:
    :return:
    """

    def get_height(head, depth):
        """
        获得二叉树深度
        :type head:Node
        :type depth:int
        :param head:
        :param depth:
        :return:
        """
        if head is None:
            return 1
        return max(get_height(head.left, depth+1), get_height(head.right, depth+1))

    def set_edge_map(head, depth, map):
        """
        :type head:Node
        :type depth:int
        :type map:list
        :param head:
        :param depth:
        :param map:
        :return:
        """
        if not head:
            return
        if map[depth][0] == None:
            map[depth][0] = head
        map[depth][1] = head
        set_edge_map(head.left, depth+1, map)
        set_edge_map(head.right, depth+1, map)

    def leaf_not_in_map(head, depth, map, result):
        """
        :type head:Node
        :type depth:int
        :type map:list
        :type result:list
        :param head:
        :param depth:
        :param map:
        :param result:
        :return:
        """
        if not head:
            return
        if not head.left and head.right and head != map[depth][0] and head != map[depth][1]:
            result.append(head)
        leaf_not_in_map(head.left, depth+1, map, result)

    if tree is None:
        return tree
    height = get_height(tree, 0)
    edge_map = [[None for i in range(2)] for j in range(height)]
    set_edge_map(tree, 0, edge_map)
    result = []
    # 获取左边缘节点
    for i in range(len(edge_map)):
        result.append(edge_map[i][0])
    leaf_not_in_map(tree, 0, edge_map, result)
    for i in range(len(edge_map)-1, -1, -1):
        if edge_map[i][0] != edge_map[i][1]:
            result.append(edge_map[i][1])


def get_edge2_with_anticlockwise(tree):
    """
    以标准二获取逆时针排序的二叉树边缘节点
    :type tree:Node
    :param tree:
    :return:
    """

    def get_left_edge(left, is_left,result):
        """
        获取左边界路径下节点和左子树叶子节点
        :type left:Node
        :type is_left:bool
        :type result:list
        :param left:
        :param is_left:
        :param result:
        :return:
        """
        if not left:
            return
        if is_left or (left.left is None and left.right is None):
            result.append(left)
        get_left_edge(left.left, True, result)
        get_left_edge(left.right, is_left and True if left.left is None else False, result)

    def get_right_edge(right, is_right, result):
        """
        获取右边界路径下节点和右子树叶子节点
        :type right:Node
        :type is_right:bool
        :type result:list
        :param right:
        :param is_right:
        :param result:
        :return:
        """
        if not right:
            return
        get_right_edge(right.left, is_right and True if right.right is None else False, result)
        get_right_edge(right.right, True, result)
        if is_right or (right.left is None and right.right is None):
            result.append(right)

    if not tree:
        return tree
    result = []
    get_left_edge(tree.left, True, result)
    get_right_edge(tree.right, True, result)
    return result


if __name__ == "__main__":
    pass
