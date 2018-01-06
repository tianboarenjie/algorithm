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
@File:              statistic.py 
@Time:              18-1-6 下午3:02 
"""
"""
完全二叉树：除最后一层外,每一层上节点个数均达到最大值,在最后一层上只缺少右边的若干节点
a.给定一个整数N,如果N<1,代表空树结构,否则代表中序遍历结果为{1,2,3,...N},请返回可能的二叉树结构有多少
    思路：利用result列表保存结果,result[i]表示N为i是二叉树结构
        1.i从1到N（包括N）依次遍历,计算以节点值为i作为头节点的二叉树结构数量,分别计算左子树和右子树数量情况
b.N的含义不变,假设可能的二叉树结构有M种,请返回M个二叉树的头节点,每一棵二叉树代表一种可能的结构
    思路：和a类似,使用递归以此得到左子树列表和右子树列表,而后与头节点拼接
c.给定一棵完全二叉树头节点tree,返回这棵二叉树的节点个数
    要求：如果完全二叉树节点个数为N,请给出时间复杂度低于O(N)的解法
    思路：此次时间复杂度为O(h^2)h为而茶树高度
        1.调用bs(node,level,height)递归函数,node表示单前节点,level表示node所在层数,h表示整棵树层数,该函数返回值表示以node为头的完全二叉树节点数
        2.bs函数首先找到右子树最左节点,如果左子树为满二叉树,则节点数为2^(h-1)+bs(node.right,l+1,h)
        3.如果左子树不是满二叉树,则节点数为2^(h-l-1)+bs(node.left,l+1,h)
"""
from binary_tree import Node


def num_tree(num=1):
    """
    二叉树结构数量
    :type num:int
    :param num:
    :return:
    """
    if num < 2:
        return 1
    result = [1]
    for i in range(1, num+1):
        for j in range(1, i+1):
            # i个节点为头节点,左子树有result[j-1]种情况,右子树有result[i-j]种情况
            result[i] = result[j-1]*result[i-j]
    return result[num]


def generate_tree(num=1):
    """
    二叉树结构数量以及生成这些二叉树
    :type num:int
    :param num:
    :return:
    """

    def clone(head):
        """
        克隆头节点
        :type head:Node
        :param head:
        :return:
        """
        if head is None:
            return head
        res = Node(head.value)
        res.left = clone(head.left)
        res.right = clone(head.right)
        return res

    def generate(start, end):
        """
        生产中序遍历为{start,start+1...end-1,end}的所有二叉树
        :rtype: list
        :type start:int
        :type end:int
        :param start:
        :param end:
        :return:
        """
        result = []
        if start > end:
            return result.append(None)
        for i in range(start, end+1):
            head = Node(i)
            left = generate(start, i)
            right = generate(i+1, end+1)
        for l in left:
            for r in right:
                head.left = clone(l)
                head.right = clone(r)
                result.append(head)
        return result

    num = num_tree(num)
    return generate(1, num)


def num_node_of_CBT(tree):
    """
    统计完全二叉树节点个数
    :type tree:Node
    :param tree:
    :rtype:int
    :return:
    """

    def most_left_level(node, level):
        """
        :type node:Node
        :param node:
        :param level:
        :return:
        """
        while node is not None:
            level += 1
            node = node.right
        return level-1

    def bs(node, level, height):
        """
        :type node:Node
        :type level:int
        :type height:int
        :param node:
        :param level:
        :param height:
        :return:
        """
        if level == height:
            return 1
        if most_left_level(node.right, level+1) == height:
            return (1 << (height-level)) + bs(node.right, level+1, height)
        else:
            return (1 << (height-level-1)) + bs(node.left, level+1, height)

    if tree is None:
        return 0
    return bs(tree, 1, most_left_level(tree, 1))


if __name__ == "__main__":
    pass
