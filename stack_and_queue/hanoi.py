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
@Time:              17-11-30 下午10:45 
"""
"""
利用递归和栈解决汗诺塔问题
"""
from enum import Enum
import sys
from stack import Stack


class Action(Enum):
    No = "No"
    LToM = "LToM"
    MToL = "MToL"
    RToM = "RToM"
    MToR = "MToR"


def hanoi_stack(num, left="left", mid="mid", right="right"):
    """
    利用栈逐一判断L->M,M->L,M->R,R->M是否符合移动规则
    :param num: 汉诺塔层数
    :param left: 源位置
    :param mid: 中转位置
    :param right: 目标位置
    :return: 完成移动所需步数
    """
    left_stack = Stack()
    mid_stack = Stack()
    right_stack = Stack()
    left_stack.push(sys.maxsize)
    mid_stack.push(sys.maxsize)
    right_stack.push(sys.maxsize)
    for i in range(num, 0, -1):
        left_stack.push(i)
    record_action = [Action.No]
    step = 0
    while right_stack.size() != num+1:
        step = step + stack_to_stack_process(record_action, Action.LToM, Action.MToL, left_stack, mid_stack, left, mid)
        step = step + stack_to_stack_process(record_action, Action.MToL, Action.LToM, mid_stack, left_stack, mid, left)
        step = step + stack_to_stack_process(record_action, Action.MToR, Action.RToM, mid_stack, right_stack, mid, right)
        step = step + stack_to_stack_process(record_action, Action.RToM, Action.MToR, right_stack, mid_stack, right, mid)
    return step


def stack_to_stack_process(record_action, current_action, against_action, source_stack, destination_stack, source, destination):
    """
    利用栈判断汉诺塔当前移动是否符合规则
    :param record_action: 记录汉诺塔上一步
    :param current_action: 判断汉诺塔当前步是否符合规则
    :param against_action: 汉诺塔当前移动的逆移动M->L的逆移动为L->M
    :param source_stack:
    :param destination_stack:
    :param source: 源位置
    :param destination: 目标位置
    :return: 移动符合规则返回1,不符合规则返回0
    """
    if record_action[0] != against_action and source_stack.peek() < destination_stack.peek():
        destination_stack.push(source_stack.pop())
        print("Move %s from %s to %s" % (destination_stack.peek(), source, destination))
        record_action[0] = current_action
        return 1
    return 0


def hanoi_recurrence(num, left="left", mid="mid", right="right"):
    if num < 1:
        return 0
    return recurrence_process(num, left, mid, right, left, right)


def recurrence_process(num, left="left", mid="mid", right="right", source="left", destination="right"):
    """

    :rtype: int
    """
    if num == 1:
        if source == "mid" or destination == "mid":
            print("Move 1 from %s to %s" % (source, destination))
            return 1
        else:
            print("Move 1 from %s to %s" % (source, mid))
            print("Move 1 from %s to %s" % (mid, destination))
            return 2
    if source == "mid" or destination == "mid":
        other = right if source == "left" or destination == "left" else left
        step_part1 = recurrence_process(num-1, left, mid, right, source, other)
        step_part2 = 1
        print("Move %s from %s to %s" % (num, source, destination))
        step_part3 = recurrence_process(num-1, left, mid, right, other, destination)
        return step_part1 + step_part2 + step_part3
    else:
        step_part1 = recurrence_process(num-1, left, mid, right, source, destination)
        step_part2 = 1
        print("Move %s from %s to %s" % (num, source, mid))
        step_part3 = recurrence_process(num-1, left, mid, right, destination, source)
        step_part4 = 1
        print("Move %s from %s to %s" % (num, mid, destination))
        step_part5 = recurrence_process(num-1, left, mid, right, source, destination)
        return step_part1 + step_part2 + step_part3 + step_part4 + step_part5
