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
@File:              presentation_tree.py
@Time:              17-12-26 下午11:56 
"""
"""
较为直观打印二叉树
"""
from binary_tree import Node


def presentation_print(tree):
    """
    直观遍历打印二叉树
    :type tree:Node
    :param tree:
    :return:
    """

    def print_special_inorder(node, depth, mark, space):
        """
        特殊中序遍历打印,右根左
        :type node:Node
        :type depth:int
        :type mark:str
        :type space:int
        :param node:
        :param depth:
        :param mark:
        :param space:
        :return:
        """
        if not node:
            return
        print_special_inorder(node.right, depth+1, "R", space)
        value = mark + node.value + mark
        len_value = len(value)
        len_left = (space - len_value)//2
        len_right = space - len_value - len_left
        value = " "*len_left + value + " "*len_right
        print(" "*(depth*space) + value)
        print_special_inorder(node.left, depth+1, "L", space)

    if not tree:
        return
    print("Binary Tree:")
    # int所能表示最大值9223372036854775807,应该设置19
    print_special_inorder(tree, 0, "H", 8)



if __name__ == "__main__":
    pass
