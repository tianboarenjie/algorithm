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
@File:              traversal.py 
@Time:              17-12-24 下午9:51 
"""
"""
使用递归和非递归方式遍历二叉树,分别按照二叉树先序、中序后序打印所有节点.规定先序遍历顺序：根左右;中序：左根右；后序：左右根
思路：
    1.使用递归比较简单,先序中序后序只需要调整输出节点值及相应递归函数调用次序
    2.不使用递归函数需要使用列表或是栈,
        先序遍历逻辑
            a.将二叉树头节点压入列表或是栈
            b.弹出输出弹出的节点值,先判断如果弹出节点右孩子不为None则右孩子压入栈,后判断如果弹出节点左孩子不为None则左孩子压入栈
            c.一直到列表或是栈为空 
        中序遍历逻辑
            a.使用列表保存二叉树节点,使用tree表示当前需要打印的节点,
            b.如果tree不为None,将tree放入队列末尾,将tree赋值为tree.left,重复判断b,
            c.如果tree为None,将tree赋值为list的队列末尾节点,答应tree的节点值,将tree赋值为tree.right
            d.重复,知道tmp为空且tree为空
        后序遍历逻辑
            a.使用一个列表保存二差树节点,使用tree表示最近一次弹出并打印的二叉树节点,head表示栈顶节点,初始tree为binary_tree,head为None
            b.每次head为当前列表末尾节点但是不从列表弹出,如果head的左孩子不为None,且tree不为head的左孩子,则把head的左孩子放入列表末尾
            c.如果head的右孩子不为None,且tree不为head的右孩子,则把head的右孩子放入列表末尾
            d.如果head的左右孩子都为None,则输出当前tree节点的值,并把tree赋值为head
        
    3.Morris时间复杂度为O(N),额外空间复杂度为O(1):使用叶子节点的左右空指针指向前驱节点和后继节点
        先序遍历：
            a.如果当前节点左孩子为空,输出当前节点并将其右孩子作为当前节点
            b.如果当前节点左孩子不为空,则在当前节点左子树中找到当前节点在中序遍历下前驱节点
                1.如果前驱节点右孩子为空,则将右孩子设置为当前节点,输出当前节点,更新当前节点为当前节点左孩子
                2.如果前驱节点右孩子为当前节点,将它的右孩子重新设置为空,当前节点更新为当前节点右孩子
                3.重复直到当前节点为空
        中序遍历：
            a.如果当前节点左孩子为空,输出当前节点并将当前节点右孩子更新为当前节点
            b.如果当前节点左孩子不为空,在当前节点左子数中找到当前节点在中序遍历下的前驱节点
                1.如果前驱节点右孩子为空,将它的右孩子设置为当前节点,当前节点更新为当前节点左孩子
                2.如果前驱节点的右孩子为当前节点,将它的右孩子设为None,输出当前节点,将当前节点更新为当前节点右孩子
                3.重复直到当前节点为空
        后序遍历：
            a.建立临时节点tmp,令tmp的左孩子为root,
            b.如果当前节点左孩子为空,更新其右孩子为当前节点
            c.如果当前节点左孩子不为空,在当前节点左子树中找到当前节点中序遍历下的前驱节点
                1.如果前驱节点右孩子为空,将它的右孩子更新为当前节点,将当前节点更新为当前节点的左孩子
                2.如果前驱节点右孩子为当前节点,将它的右孩子更新为None,同时倒序输出左孩子到前驱节点这条路经上所有节点,将当前节点更新为当前节点右孩子
                3.重复直到当前节点为空
"""
__all__ = ["Node", ]


class Node:
    
    __slots__ = ["__value", "__left", "__right"]
    
    def __init__(self, value):
        if value is None or isinstance(value, str):
            raise ValueError("Must specify the value of Node, actually the type of string!")
        self.__value = value
        self.__left = None
        self.__right = None
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value_string):
        self.__value = value_string
    
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, left_node):
        self.__left = left_node
        
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, right_node):
        self.__right = right_node
        

def preorder_traversal_recursion(binary_tree):
    """
    使用递归函数实现二叉树的先序遍历,根左右
    :type binary_tree:Node
    :param binary_tree: 
    :return: 
    """
    if binary_tree is None:
        return 
    print("Node's value is:%10.10s" % binary_tree.value)
    preorder_traversal_recursion(binary_tree.left)
    preorder_traversal_recursion(binary_tree.right)
    

def inorder_traversal_recursion(binary_tree):
    """
    使用递归函数实现二叉树的中序遍历,左根右
    :type binary_tree:Node
    :param binary_tree: 
    :return: 
    """
    if binary_tree is None:
        return 
    inorder_traversal_recursion(binary_tree.left)
    print("Node's value is:%10.10s" % binary_tree.value)
    inorder_traversal_recursion(binary_tree.right)
    
    
def postorder_traversal_recursion(binary_tree):
    """
    使用递归函数实现二叉树的后序遍历,左右根
    :type binary_tree:Node
    :param binary_tree: 
    :return: 
    """
    if binary_tree is Node:
        return 
    postorder_traversal_recursion(binary_tree.left)
    postorder_traversal_recursion(binary_tree.right)
    print("Node's value is:%10.10s" % binary_tree.value)
    

def preorder_traversal_depend_list(binary_tree):
    """
    以来列表而不是递归实现二叉树先序遍历
    :type binary_tree:Node
    :param binary_tree: 
    :return: 
    """
    tree = binary_tree
    if tree is None:
        return 
    print("preorder traversal begin")
    tmp = [tree]
    while tmp:
        tree = tmp.pop()
        print("Node value: %10.10s" % tree.value)
        if tree.right:
            tmp.append(tree.right)
        if tree.left:
            tmp.append(tree.left)
    print("preorder traversal end")
    

def inorder_traversal_depend_list(binary_tree):
    """
    以来列表而不是递归实现二叉树中序遍历,左根右
    :type binary_tree:Node
    :param binary_tree: 
    :return: 
    """
    tree = binary_tree
    if tree is None:
        return 
    print("inorder traversal begin")
    while tree:
        tmp = []
        while tmp or tree:
            if tree:
                tmp.append(tree)
                tree = tree.left
            else:
                tree = tmp.pop()
                print("Node value: %10.10s" % tree.value)
                tree = tree.right
    print("inorder traversal end")


def postorder_traversal_depend_list1(binary_tree):
    """
    以来列表而不是递归实现二叉树后序遍历,左右根
    :type binary_tree:Node
    :param binary_tree:
    :return:
    """
    tree = binary_tree
    if tree is None:
        return
    print("postorder traversal begin")
    tmp1 = [tree]
    tmp2 = []
    while tmp1:
        tree = tmp1.pop()
        tmp2.append(tree)
        # 注意判断的先后顺序
        if tree.left:
            tmp1.append(tree.left)
        if tree.right:
            tmp1.append(tree.right)
    while tmp2:
        print("Node value: %10.10s" % tmp2.pop().value)
    print("postorder traversal end")


def postorder_traversal_depend_list2(binary_tree):
    """
    以来列表而不是递归实现二叉树后序遍历,左右根
    :type binary_tree:Node
    :param binary_tree:
    :return:
    """
    tree = binary_tree
    if tree is None:
        return
    print("postorder traversal begin")
    tmp = [tree]
    while tmp:
        head = tmp[-1]
        if head.left and tree != head.left and tree != head.right:
            tmp.append(head.left)
        elif head.right and tree != head.right:
            tmp.append(head.right)
        else:
            print("Node value: %10.10s" % tmp.pop().value)
            tree = head
    print("postorder traversal end")


def preorder_traversal_morris(binary_tree):
    """
    额外空间复杂度O(1)
    :type binary_tree:Node
    :param binary_tree:
    :return:
    """
    if binary_tree is None:
        return binary_tree
    cur = binary_tree
    while cur:
        if cur.left is None:
            print("Node value: %10.10s" % cur.value)
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            if pre.right is None:
                print("Node value: %10.10s" % cur.value)
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                cur = cur.right


def inorder_traversal_morris(binary_tree):
    """
    额外空间复杂度O(1)
    :type binary_tree:Node
    :param binary_tree:
    :return:
    """
    if binary_tree is None:
        return binary_tree
    cur = binary_tree
    while cur:
        if cur.left is None:
            print("Node value: %10.10s" % cur.value)
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            if pre.right is None:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                print("Node value: %10.10s" % cur.value)
                cur = cur.right


def postorder_traversal_morris(binary_tree):
    """
    额外空间复杂度O(1)
    :type binary_tree:Node
    :param binary_tree:
    :return:
    """

    def reverse_partition(head):
        """
        反转从start到end节点
        :type head:Node
        :param head:
        :return:
        """
        pre = None
        while head:
            next = head.right
            head.right = pre
            pre = head
            head = next
        return pre

    def print_right_edge(head):
        """
        打印从start开始到end节点值
        :type head:Node
        :param head:
        :return:
        """
        tail = reverse_partition(head)
        cur = tail
        while cur:
            print("Node value: %10.10s" % cur.value)
            cur = cur.right
        reverse_partition(tail)

    if binary_tree is None:
        return binary_tree
    tmp = Node(0)
    tmp.left = binary_tree
    cur = tmp
    while cur:
        if cur.left is None:
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            if pre.right is None:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                print_right_edge(cur.left)
                cur = cur.right


if __name__ == "__main__":
    pass
