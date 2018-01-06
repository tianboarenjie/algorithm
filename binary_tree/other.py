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
@File:              other.py 
@Time:              18-1-1 下午10:56 
"""
"""
a.给定新二叉树节点定义如下,给定一个这样二叉树中的某个节点node,请实现返回node的后续节点函数(中序遍历下node的下一个节点)
    思路：
        1.如果node有右子树,则后续节点为右子树最左节点
        2.如果node没有右子树,判断node是否是node父节点的左孩子,是的话后续节点直接是父节点,否则向上寻找后续节点,s为node
          父节点,s的父节点为p,判断s是否为p左孩子,是的话后续节点为p,否则s和p一直向上移动
        3.在2中如果p一直移动到None都不符合,表明node为中序遍历末尾节点,没有后序节点
b.给定一棵二叉树头节点tree,求整棵树上节点间最大距离
    思路：
        1.最大距离可能来源于左子树上最大距离,右子树最大距离,左子树最远距离加右子树最远距离加1
c.先序,中序,后序列表两两结合重构二叉树
    先序+后序：一棵二叉树除了叶子节点外其他节点都有左右孩子,这样的二叉树先序后序遍历结果才能用于重构二叉树
d.利用先序和中序遍历列表生成后序遍历列表
"""
from binary_tree import Node

class PNode:

    __slots__ = ["__value", "__left", "__right", "__parent"]

    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None
        self.__parent = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__value = v

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, v):
        self.__left = v

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, v):
        self.__right = v

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, v):
        self.__parent = v

    def add_left(self, node):
        if node is None:
            return
        self.left = node
        node.parent = self

    def add_right(self, node):
        if node is None:
            return
        self.right = node
        node.parent = self

def next(node):
    """
    返回中序遍历下node的下一个节点
    :type node:PNode
    :param node:
    :return:
    """
    # TODO (programme at 18-1-1): 不利用常规找到头节点而后中序遍历找到node的下一个节点,思考新的更优解

    def get_left_most(cur):
        """
        获取cur的最左边节点
        :type cur:PNode
        :param cur:
        :return:
        """
        if cur is None:
            return cur
        while cur.left:
            cur = cur.left
        return cur

    if node is None:
        return node
    # 第1种情况
    if node.right:
        return get_left_most(node.right)
    else:
        parent = node.parent
        if parent and parent.left != node:
            node = parent
            parent = node.parent
        return parent


def max_distance(tree):
    """
    二叉树tree节点间最大距离
    :type tree:Node
    :param tree:
    :return:
    """
    def postorder(head, record):
        """
        后序遍历得到以head为头节点的左右最大距离
        :type head:Node
        :type record:list
        :param head:
        :param record:
        :return:
        """
        if head is None:
            record[0] = 0
            return 0
        left_max = postorder(head.left, record)
        max_from_left = record[0]
        right_max = postorder(head.right, record)
        max_from_right = record[0]
        # 经过head节点的最大距离
        cur_max = max_from_left + 1 + max_from_right
        record[0] = max(max_from_left, max_from_left) + 1
        return max(max(left_max, right_max), cur_max)

    record = [0]


def preinf_to_tree(pre, inf):
    """
    利用先序中序遍历重构二叉树
    :type pre:list
    :type inf:list
    :param pre:
    :param inf:
    :return:
    """

    def preinf(p, ps, pe, i, ii, ie, n):
        """
        :type p:list
        :type ps:int
        :type pe:int
        :type i:list
        :type ii:int
        :type ie:int
        :type n:dict
        :param p:
        :param ps:
        :param pe:
        :param i:
        :param ii:
        :param ie:
        :param n:
        :return:
        """
        if ps > pe:
            return n
        head = Node(p[ps])
        index = n.get(p[ps])
        head.left = preinf(p, ps+1, ps+index-ii, i, ii, index-1, node)
        head.right = preinf(p, ps+index+1-ii, pe, i, index+1, ie, node)
        return head

    if pre is None or inf is None or len(pre) == 0 or len(inf) == 0:
        return None
    node = {}
    for i in range(len(inf)):
        node[inf[i]] = i
    return preinf(pre, 0, len(pre)-1, inf, 0, len(pre)-1, node)


def infpost_to_tree(inf, post):
    """
    利用中序后续遍历重建二叉树
    :param inf:
    :param post:
    :return:
    """

    def infpost(i, ii, ie, p, ps, pe, n):
        """
        :type i:list
        :type ii:int
        :type ie:int
        :type p:list
        :type ps:int
        :type pe:int
        :type n:dict
        :param i:
        :param ii:
        :param ie:
        :param p:
        :param ps:
        :param pe:
        :param n:
        :return:
        """
        if ii > ie or ps > pe:
            return n
        head = Node(p[pe])
        index = n.get(p[pe])
        head.left = infpost(i, ii, index-1, p, ps, ps+index-1-ii, node)
        head.right = infpost(i, index+1, ie, p, ps+index-ii, pe-1, node)
        return head

    if inf is None or post is None or len(inf) == 0 or len(post) == 0:
        return None
    node = {}
    for i in range(len(inf)):
        node[inf[i]] = i
    return infpost(inf, 0, len(inf)-1, post, 0, len(post)-1, node)


def prepost_to_tree(pre, post):
    """
    以来先序后序遍历结果重构二叉树
    :type pre:list
    :type post:list
    :param pre:
    :param post:
    :return:
    """
    # TODO (programme at 18-1-2): 由于特定二叉树才能使用先序后序遍历结果重建二叉树
    def prepost(pr, pr_s, pr_e, po, po_s, po_e, n):
        """
        :type pr:list
        :type pr_s:int
        :type pr_e:int
        :type po:list
        :type po_s:int
        :type po_e:int
        :type n:dict
        :param pr:
        :param pr_s:
        :param pr_e:
        :param po:
        :param po_s:
        :param po_e:
        :param n:
        :return:
        """
        if pr_s > pr_e or po_s > po_e:
            return None
        head = Node(pr[pr_s])
        index = n.get(pr[pr_s+1])
        head.left = prepost(pr, pr_s+1, pr_s+1+index-po_s, po, po_s, index, n)
        head.right = prepost(pr, pr_s+2+index-po_s, po, index+1, po_e-1, n)
        return head

    if pre is None or post is None or len(pre) == 0 or len(post) == 0:
        return None
    node = {}
    for i in range(len(post)):
        node[post[i]] = i
    return prepost(pre, 0, len(pre)-1, post, 0, len(post)-1, node)


def get_post_from_pre_inf(pre, inf):
    """
    利用先序遍历和中序遍历得到后序遍历
    :type pre:list
    :type inf:list
    :param pre:
    :param inf:
    :return:
    """

    def post(p, p_s, p_e, i, i_s, i_e, n, r):
        """
        :type p:list
        :type p_s:int
        :type p_s:int
        :type i:list
        :type i_s:int
        :type i_e:int
        :type n:dict
        :type r:list
        :param p:
        :param p_s:
        :param p_e:
        :param i:
        :param i_s:
        :param i_e:
        :param n:
        :param r:list
        :return:
        """
        if p_s > p_e or i_s > i_e:
            return r
        r.insert(0, p[p_s])
        index = n.get(p[p_s])
        # 左子树长度index-1-i_s右子树长度i_e-index
        r = post(p, p_e+1-index-i_s, p_e, i, index+1, i_e, n, r)
        return post(p, p_s+1, p_s+index-i_s, i, i_s, index-1, n, r)

    if pre is None or inf is None or len(pre) == 0 or len(inf) == 0 or len(pre) != len(inf):
        return None
    result = []
    node = {}
    for i in range(len(pre)):
        node[inf[i]] = i
    return post(pre, 0, len(pre)-1, inf, 0, len(inf)-1, node, result)



if __name__ == "__main__":
    pass
