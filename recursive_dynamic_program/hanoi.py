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
@File:              hanoi.py 
@Time:              18-1-8 下午11:00 
"""
"""
a.给定一个整数num,代表汉诺塔游戏中从小到大放置的num个圆盘,假设开始时所有圆盘都放置在左边的柱子上,想按照汉诺塔游戏要求把所有圆盘都移动到右边柱子上,请实现函数打印最优移动轨迹
b.给定一个整数列表disks,其中只包含1,2,3,代表圆盘状态,1表示左柱,2表示中柱3表示右柱,disks[i]表示第i+1个圆盘所在位置.如果disks代表的状态是最优移动轨迹过程中出现的状态,返回
  这种状态是最优移动轨迹中的第几个状态,如果disks不是最优移动状态过程中出现的状态,返回-1
    思路：
        1.分析最优移动过程,首先需要将left上的1～i都移动到right,需要第一步骤将1～i-1移动到mid,有s(i-1)步,而后第二步骤将i移动到right,有1步,最后将1～i-1移动到right有s(i-1)
        2.分析共有s(i)=t(i-1)+1+t(i-1),解得s(i)=2^i-1=2*t(i-1)+1==>t(i-1)=2^(i-1)
        3.disks[i-1]表示最大圆盘,判定其所在位置,如果disks[i-1]为1表示在left,即上述第一步骤还没结束,需要考察disks[i-2],移动目标为left到mid,如果disks[i-1]为2表示mid,最右移动没有这种情况,直接
          返回-1,如果disks[i-1]为3表示在right,表明起码移动了2^(i-1)步骤即第一步骤完成,需要考察disks[i-2],移动目标为mid到right
"""


def hanoi(num):
    """
    打印汉诺塔移动轨迹
    :type num:int
    :param num:
    :return:
    """

    def process(num, fro, mid, to):
        """
        打印移动轨迹
        :type num:int
        :type fro:str
        :type mid:str
        :type to:str
        :param num:
        :param fro:
        :param mid:
        :param to:
        :return:
        """
        if num == 1:
            print("Move from %s to %s" % (fro, to))
        else:
            process(num-1, fro, to, mid)
            process(num, fro, mid, to)
            process(num-1, mid, fro, to)

    if num > 0:
        process(num, "left", "mid", "right")


def hanoi_step_recursion(disks):
    """
    判定disks为最右移动次序的状态值
    :type disks:list
    :param disks:
    :return:
    """

    def process(disks, index, left, mid, right):
        """
        确定移动状态
        :type disks:list
        :type index:int
        :type left:int
        :type mid:int
        :type right:int
        :param disks:
        :param index:
        :param left:
        :param mid:
        :param right:
        :return:
        """
        if index == -1:
            return -1
        if disks[index] not in [left, right]:
            return -1
        if disks[index] == left:
            return process(disks, index-1, left, right, mid)
        else:
            first = process(disks, index-1, mid, left, right)
            if first == -1:
                return -1
            return (1 << index) + first

    if disks is None or len(disks) == 0:
        return -1
    # 1表示right,2表示mid,3表示right
    return process(disks, len(disks)-1, 1, 2, 3)


def hanoi_step(disks):
    """
    —判定disks为最右移动次序的状态值
    :type disks:list
    :param disks:
    :return:
    """
    if disks is None or len(disks) == 0:
        return -1
    left = 1
    mid = 2
    right = 3
    index = len(disks)-1
    steps = 0
    while index >= 0:
        if disks[index] not in [left, right]:
            return -1
        if disks[index] == right:
            steps += 1 << index
            tmp = left
            left = mid
        else:
            tmp = right
            right = mid
        mid = tmp
        index -=1
    return steps


if __name__ == "__main__":
    pass
