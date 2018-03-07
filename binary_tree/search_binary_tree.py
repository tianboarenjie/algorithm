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
@File:              search_binary_tree.py
@Time:              17-12-28 下午11:11 
"""
"""
搜索二叉树：若二叉树它的左子树不为空,则左子树所有节点的值均小于它的根节点,若它的右子树不为空,则右子树所有节点均大于根节点

a.给定一个二叉树头节点tree,已知所有节点值都不一样,找到含有节点最多的搜索二叉树
    要求：如果节点数N,则要求时间复杂度O(N),额外空间复杂度为O(h),h为二叉树高度
    思路：
        1.以tree为头的树中,如果tree.left和tree.right均满足搜索二叉树,且max(tree.left)<tree.value<min(tree.right)
          则表明整个二叉树都是搜索二叉树,否则最大搜索二叉树在tree的左子树或是右子树之中
        2.由于要先判断左子树,右子树情况,而后判断根,故此采用后序遍历方式
        3.遍历到cur节点,先遍历cur.left获得左子树4个信息：left_SBT(左子树上最大搜索二叉树头节点),left_size(左子树节点数),
          left_min(左子树最小节点值),left_max(左子树最大节点值),同样右子树也需要收集这4个信息right_SBT,right_size,right_min,right_max
        4.根据3收集信息判断是否符合1,符合返回cur,不符合判断left_size和right_size返回相应头节点
b.给定一棵二叉树头节点tree,已知所有节点值都不一样,返回其中最大且符合搜索二叉树的最大拓扑结构的大小
    思路1：利用常规递归,时间复杂度为O(N^2)
        1.先考察node的左右孩子是否符合搜索二叉树定义,符合则这个孩子节点可以作为最大搜索二叉树拓扑一部分,并且继续延伸考察孩子节点的孩子节点
    思路2：利用拓扑贡献记录实现时间复杂度O(N),额外空间复杂度最差O(N*logN)
        拓扑贡献值：每个节点计算2个值,第1个为节点左子树可以为当前头节点的拓扑贡献值,第2个为节点右节点可以为当前头节点的拓扑共享值
        1.后续遍历获得每个节点左孩子和右孩子的拓扑贡献记录
        2.通过节点左右孩子获得当前节点拓扑贡献记录,通过考察左孩子右边界和右孩子左边界节点
c.一棵二叉树原本是搜索二叉树,但由于其中2个节点调换了位置使得它不再是搜索二叉树,该树各节点值都不一样.
    普通：给定这棵二叉树头节点tree,返回这2个错误节点.
        思路：
            1.根据搜索二叉树定义,对tree进行中序遍历一定是升序,直到两个错误节点时会降续
            2.出现2次降续时,第1个错误节点是第1次降续较大值,第2个错误节点是第2次降续较小值
            3.出现1次降续时,第1个错误节点是第1次降续较大值,第2个错误节点是地1次降续较小值
            4.归纳即为第1个错误节点为第1次降序较大值,第2个错误节点为最后一次降续较小值
    进阶：找到2个错误节点,并在结构上完全交换这2个节点位置（不是交换这2个节点值）
        思路：分不同情况讨论,e1和e2分别为第1个和第2个错误节点,e1p和e2p分别为第1个和第2个错误节点父节点,e1l、e1r、e2l和e2r分别为第1个第2个错误节点左右孩子
            主要需要关注三个问题：
                1.e1和e2是否有1个为头节点,如果有,谁是头节点
                2.e1和e2是否相邻,如果相邻,谁是谁的父节点
                3.e1和e2分别是各自父节点的左孩子还是右孩子
            根据各种情况综合讨论,大概情况如下,（是按照中序遍历得到的错误节点和错误父节点）：
                1.e1是头节点,且e1是e2的父节点,则e2是e1的右孩子
                2.e1是头节点,且e1不是e2父节点,e2是e2p的左孩子
                3.e1是头节点,且e1不是e2父节点,e2是e2p的右孩子
                4.e2是头节点,且e2是e1的父节点,则e1是e2的左孩子
                5.e2是头节点,且e2不是e1的父节点,e1是e1p的左孩子
                6.e2是头节点,且e2不是e1的父节点,e1是e1p的右孩子
                7.e1和e2都不是头节点,e1是e2的父节点,则e2是e1的右孩子,e1是e1p的左孩子
                8.e1和e2都不是头节点,e1是e2的父节点,则e2是e1的右孩子,e1是e1p的右孩子
                9.e1和e2都不是头节点,e2是e1的父节点,则e1是e2的左孩子,e2是e2p的左孩子
                10.e1和e2都不是头节点,e2是e1的父节点,则e1是e2的左孩子,e2是e2p的右孩子
                11.e1和e2都不是头节点,e1和e2谁都不是谁的父节点,e1是e1p的左孩子,e2是e2p的左孩子
                12.e1和e2都不是头节点,e1和e2谁都不是谁的父节点,e1是e1p的左孩子,e2是e2p的右孩子
                13.e1和e2都不是头节点,e1和e2谁都不是谁的父节点,e1是e1p的右孩子,e2是e2p的左孩子
                14.e1和e2都不是头节点,e1和e2谁都不是谁的父节点,e1是e1p的右孩子,e2是e2p的右孩子
            注意：其中1-3头节点为e2,4-6头节点为e1
d.给定一个整形列表value_list,其中没有重复值,
    普通：判断value_list是否可能是节点值类型为整型的搜索二叉树后序遍历结果
        思路：
            1.由于后续遍历可知列表最后一个节点值为头节点,将原列表分为比头节点小的左子树和比头节点大的右子树
            2.判断左右字数是否符合搜索二叉树后续遍历规则
    进阶：根据该value_list搜索二叉树后序遍历结果重建该搜索二叉树
        思路：
            1.由于后续遍历可知列表最后一个节点值为头节点,将原列表分为比头节点小的左子树和比头节点大的右子树
"""
from binary_tree import Node
import sys


def biggest_subSBT(tree):
    """
    获取tree中最大搜索二叉树头节点
    :type tree:Node
    :param tree:
    :return:
    """

    def postorder(head, records):
        """
        :type head:Node
        :type records:list
        :param head:
        :param records:
        :return:
        """
        if not head:
            records[0] = 0                      # size
            records[1] = sys.maxsize            # min
            records[2] = 0-sys.maxsize          # max
            return head

        value = head.value
        left_SBT = postorder(head.left, records)
        left_size, left_min, left_max = records
        right_SBT = postorder(head.right, records)
        right_size, right_min, right_max = records
        # 如果最大搜索二叉树不是本身,则records[1]和records[2]就没有用了
        records[1] = min(left_min, right_min)
        records[2] = max(left_max, right_max)
        if left_SBT == head.left and right_SBT == head.right and left_max < value and value < right_min:
            records[0] = left_size + right_size + 1
            return head
        records[0] = max(left_size, right_size)
        return left_SBT if left_size > right_size else right_SBT


    sbt_record = [0, 1, 2]
    return postorder(tree, sbt_record)


def biggest_subSBT_topology_size1(tree):
    """
    最大且符合搜索二叉树的最大拓扑结构的大小
    :type tree:Node
    :param tree:
    :return:
    """

    def isSBTnode(head, node, value):
        """
        判断node是否符合搜索二叉树定义
        :type head:Node
        :type node:Node
        :type value:int
        :param head:
        :param node:
        :param value:
        :return:
        """
        if not head:
            return False
        if head == node:
            return True
        return isSBTnode(head.left if head.value > value else head.right, node, value)

    def max_topology(head, child):
        """
        获取最大搜索二叉树字数拓扑大小
        :type head:Node
        :type child:
        :param head:
        :param child:
        :return:
        """
        if head and child and isSBTnode(head, child, child.value):
            return max_topology(head, head.left) + max_topology(head, head.right) + 1
        return 0

    if not tree:
        return tree
    max_size = max_topology(tree, tree)
    max_size = max(biggest_subSBT_topology_size1(tree.left), max_size)
    max_size = max(biggest_subSBT_topology_size1(tree.right), max_size)
    return max_size


def biggest_subSBT_topology_size(tree):
    """
    获取最大搜索二叉树字数拓扑大小
    :type tree:Node
    :param tree:
    :return:
    """

    class Record:

        def __init__(self, left, right):
            self.left = left
            self.right = right

        @property
        def left(self):
            return self.left

        @left.setter
        def left(self, value):
            self.left = value

        @property
        def right(self):
            return self.right

        @right.setter
        def right(self, value):
            self.right = value


    def modify_recoreds(head, value, records, is_left):
        """
        :type head:Node
        :type value:int
        :type records:dict
        :type is_left:bool
        :param head:
        :param value:
        :param records:
        :param is_left:
        :return:
        """
        if not head or not records.get(head):
            return 0
        record = records.get(head)
        if (is_left and head.value > value) or ((not is_left) and head.value < value):
            return record.left + record.right + 1
        else:
            minus = modify_recoreds(head.right if is_left else head.left, value, records, is_left)
            if is_left:
                record.right = record.right - minus
            else:
                record.left = record.left - minus
            records[head] = record
            return minus

    def postorder(head, records):
        """
        后续遍历更新拓扑共享记录
        :type head:Node
        :type records:dict
        :param head:
        :param records:
        :return:
        """
        if not head:
            return 0
        left = postorder(head.left, records)
        right = postorder(head.right, records)
        modify_recoreds(head.left, head.value, records, True)
        modify_recoreds(head.right, head.value, records, False)
        left_record = records.get(head.left)
        right_record = records.get(head.right)
        left_sbt = 0 if not left else left_record.left + left_record.right + 1
        right_sbt = 0 if not right else right_record.left + right_record.right + 1
        records[head] = Record(left_sbt, right_sbt)
        return max(left_sbt + right_sbt + 1, max(left, right))

    node_map = {}
    return postorder(tree, node_map)


def get_two_error_nodes_depend_list(tree):
    """
    给定1棵原本为搜索二叉树头节点tree,由于调换2个节点使得不再是搜索二叉树,依赖列表返回这2个错误节点
    :type tree:Node
    :param tree:
    :return:
    """
    if not tree:
        return None
    errors = {}
    tmp = []
    pre = None
    while tmp or tree:
        if tree:
            tmp.append(tree)
            tree = tree.left
        else:
            tree = tmp.pop()
            if pre and pre.value > tree.value:
                errors[0] = errors[0] if errors[0] else pre
                errors[1] = tree
            pre = tree
            tree = tree.right
    return errors


def get_two_error_nodes_depend_morris(tree):
    """
    给定1棵原本为搜索二叉树头节点tree,由于调换2个节点使得不再是搜索二叉树,利用morris算法快速返回这2个错误节点
    :type tree:Node
    :param tree:
    :return:
    """
    if not tree:
        return None
    errors = {}
    cur = tree
    while cur:
        pre = cur.left
        if pre:
            while pre.right and pre.right != cur:
                pre = pre.right
            if pre.right is None:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
        else:
            if cur.value > cur.right.value:
                errors[0] = errors[0] if errors.get(0) else cur
                errors[1] = cur.right
            cur = cur.right
    return errors.get(0), errors.get(1)


def get_two_error_parents_depend_mirrors(tree):
    """
    给定1棵原本为搜索二叉树头节点tree,由于调换2个节点使得不再是搜索二叉树,利用morris算法快速返回这2个错误节点的父节点
    :type tree:Node
    :param tree:
    :return:
    """
    if not tree:
        return tree
    parents = {}
    # errors = {}
    pre_node = None
    cur = tree
    while tree:
        pre = cur.left
        if pre:
            while pre.right and pre.right != cur:
                pre = pre.right
            if pre.right is None:
                pre.right = cur
                pre_node = cur
                cur = cur.left
            else:
                pre.right = None
        else:
            if cur.value > cur.right.value:
                parents[0] = parents[0] if parents.get(0) else pre_node
                parents[1] = pre_node
                # errors[0] = errors[0] if errors.get(0) else cur
                # errors[1] = cur.right
            pre_node = cur
            cur = cur.right
    return parents.get(0), parents.get(1)


def repair_sbt_with_two_error_nodes(tree):
    """
    由于两个节点调换位置导致搜索二叉树不符合定义,修复搜索二叉树
    :type tree:Node
    :param tree:
    :return:
    """
    if tree is None:
        return tree
    e1, e2 = get_two_error_nodes_depend_morris(tree)
    e1p, e2p = get_two_error_parents_depend_mirrors(tree)
    e1l = e1.left
    e1r = e1.right
    e2l = e2.left
    e2r = e2.right
    if e1 == tree:
        # 第1种情况
        if e1 == e2p:
            e1.left = e2l
            e1.right = e2r
            e2.left = e1l
            e2.right = e1
        # 第2中情况
        elif e2p.left == e2:
            e2p.left = e1
            e2.left = e1l
            e2.right = e2r
            e1.left = e2l
            e1.right = e2r
        # 第3种情况
        else:
            e2p.right = e1
            e2.left = e1l
            e2.right = e1r
            e1.left = e2l
            e1.right = e2r
        tree = e2
    elif e2 == tree:
        # 第4种情况
        if e2 == e1p:
            e2.left = e1l
            e2.right = e1r
            e1.left = e2
            e1.right = e2r
        # 第5种情况
        elif e1p.left == e1:
            e1p.left = e2
            e1.left = e2l
            e1.right = e2r
            e2.left = e1l
            e2.right = e1r
        # 第6种情况
        else:
            e1p.right = e2
            e1.left = e2l
            e1.right = e2r
            e2.left = e1l
            e2.right = e1r
        tree = e1
    else:
        if e1 == e2p:
            # 第7中情况
            if e1p.left == e1:
                e1p.left = e2
                e1.left = e2l
                e1.right = e2r
                e2.left = e1l
                e2.right = e1
            # 第8种情况
            else:
                e1p.right = e2
                e1.left = e2l
                e1.right = e2r
                e2.left = e1l
                e2.right = e1
        elif e2 == e1p:
            # 第9种情况
            if e2p.left == e2:
                e2p.left = e1
                e2.left = e1l
                e2.right = e1r
                e1.left = e2
                e1.right = e2r
            # 第10种情况
            else:
                e2p.right = e1
                e2.left = e1l
                e2.right = e1r
                e1.left = e2
                e1.right = e2r
        else:
            if e1p.left == e1:
                # 第11种情况
                if e2p.left == e2:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.left = e2
                    e2p.left = e1
                # 第12种情况
                else:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.left = e2
                    e2p.right = e1
            else:
                # 第13种情况
                if e2p.left == e2:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.right = e2
                    e2p.left = e1
                # 第14种情况
                else:
                    e1.left = e2l
                    e1.right = e2r
                    e2.left = e1l
                    e2.right = e1r
                    e1p.right = e2
                    e2p.right = e1
    return tree


def isSBTpostorder(value_list):
    """
    判断value_list是否可能是节点值类型为整型的搜索二叉树后序遍历结果
    :type value_list:list
    :param value_list:
    :return:
    """

    def check(value, start, end):
        """
        判断子列表是否符合搜索二叉树后序遍历规则
        :type value:list
        :type start:int
        :type end:int
        :param value:
        :param start:
        :param end:
        :return:
        """
        if start == end:
            return True
        little_end = 0
        large_start = end
        for i in range(start, end+1):
            if value[i] < value[end]:
                little_end = i
            else:
                large_start = i if large_start == end else large_start
        if little_end != large_start-1:
            return False
        if little_end == 0 or large_start == end:
            return check(value, start, end - 1)
        return check(value, start, little_end) and check(value, large_start, end-1)

    if value_list is None or len(value_list) == 0:
        return False
    return check(value_list, 0, len(value_list)-1)


def rebuild_sbt_by_postorder(value_list):
    """
    利用搜索二叉树后序遍历结果重建搜索二叉树
    :type value_list:list
    :param value_list:
    :return:
    """

    def rebuild(value, start, end):
        if start > end:
            return None
        head = Node(value[end])
        little_end = 0
        large_start = end
        for i in range(start, end+1):
            if value[i] < value[end]:
                little_end = i
            else:
                large_start = i if large_start == end else large_start
        head.left = rebuild(value, start, little_end)
        head.right = rebuild(value, large_start, end-1)
        return head

    if len(value_list)==0 or isSBTpostorder(value_list) is False:
        return None
    rebuild(value_list, 0, len(value_list)-1)


if __name__ == "__main__":
    pass
