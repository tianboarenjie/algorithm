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
@File:              serialization.py 
@Time:              17-12-27 上午9:00 
"""
"""
二叉树被记录为文件的过程称为二叉树的序列化,通过文件内容重建原来二叉树的过程叫做二叉树的反序列化.给定一个二叉树头节点tree
设计一种二叉树序列化和反序列化的方案.
1.先序遍历实现序列化和反序列化：
    a.初始化结果字符串result为"",而后先序遍历二叉树,遇到None则在result添加"#!","!"表示该节点值结束,遇到结果则添加
    b.反序列化类似
2.层遍历实现序列化和反序列化：
    序列化：
        a.以列表保存节点,以及结果result,首先将二叉树头借点放入列表,而后进入判断,只要列表不为空,弹出列表第一个元素,判断左右是否为None
        b.如果为空,则在result字符串后添加"#!",否则字符串后添加"value!",并把该借点放入列表末尾
"""
from binary_tree import Node


def serialize_tree_preorder(tree):
    """
    序列化tree二叉树
    :type tree:Node
    :param tree:
    :return:
    """
    if not tree:
        return "#!"
    result = tree.value + "!"
    result += serialize_tree_preorder(tree.left)
    result += serialize_tree_preorder(tree.right)
    return result


def deserialize_tree_preorder(value):
    """
    反序列化利用先序遍历保存的二叉树
    :type value:str
    :param value:
    :return:
    """

    def rebuild_tree(value_list):
        """
        利用列表保存的二叉树节点值重建二叉树
        :param value_list:
        :return:
        """
        if not len(value_list):
            return
        node_value = value_list.pop(0)
        if node_value == "#":
            return None
        node = Node(node_value)
        node.left = rebuild_tree(value_list)
        node.right = rebuild_tree(value_list)
        return node

    tree_list = value.split("!")[:-1]
    return rebuild_tree(tree_list)


def serialize_tree_layer(tree):
    """
    利用层遍历序列化二叉树
    :type tree:Node
    :param tree:
    :return:
    """
    if not tree:
        return "#!"
    tmp = [tree]
    result = tree.value + "!"
    while tmp:
        node = tmp.pop(0)
        if not node.left:
            result += node.left.value + "!"
            tmp.append(node.left)
        else:
            result += "#!"
        if not node.right:
            result += node.right.value + "!"
            tmp.append(node.right)
        else:
            result += "#!"
    return result


def deserialize_tree_layer(value):
    """
    反序列化利用层遍历保存的二叉树
    :type value:str
    :param value:
    :return:
    """

    def generate_node(node_str):
        """
        利用节点数据建立node
        :type node_str:str
        :param node_str:
        :return:
        """
        if node_str == "#":
            return None
        return Node(node_str)

    value_list = value.split("!")[:-1]
    head = generate_node(value_list.pop(0))
    if not head:
        return head
    node_list = [head]
    while node_list:
        node = node_list.pop(0)
        node.left = generate_node(value_list.pop(0))
        node.right = generate_node(value_list.pop(0))
        if node.left:
            node_list.append(node.left)
        if node.right:
            node_list.append(node.right)
    return head


if __name__ == "__main__":
    pass
