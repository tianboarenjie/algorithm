#!/usr/bin/env python  
# -*-coding: utf-8 -*-

""" 
@Version:           v1.0 
@Author:            tianbaorenjie
@License:           GPL Licence  
@Contact:           tianbaorenjie@163.com
@Site:              https://github.com/tianbaorenjie 
@Software:          PyCharm 
@Project:           py36_algorithm
@File:              struct.py
@Time:              11/26/17 8:25 PM 
"""

__all__ = ["Stack", "TwoStackQueue"]


class Stack:
    """
    初始化栈为空列表,限定类成员只有__stack
    """
    __slots__ = ("__stack",)

    def __init__(self):
        self.__stack = []

    def __str__(self):
        return str(self.__stack)

    def is_empty(self):
        return self.__stack == []

    def peek(self):
        return self.__stack[len(self.__stack) - 1]

    def size(self):
        return len(self.__stack)

    def push(self, item):
        if isinstance(item, int):
            self.__stack.append(item)
        else:
            raise TypeError("element should be int object!")

    def pop(self):
        return self.__stack.pop()

    """
    仅仅利用递归和栈操作逆序一个栈,递归getAndRemoveLastElement获取栈最后一个元素并在栈中删除此元素
    递归reverse反转栈
    """
    def get_and_remove_last_element(self):
        result = self.pop()
        if self.is_empty():
            return result
        else:
            last = self.get_and_remove_last_element()
            self.push(result)
            return last

    def reverse(self):
        if self.is_empty():
            return
        last = self.get_and_remove_last_element()
        self.reverse()
        self.push(last)


class TwoStackQueue:
    """两个栈实现队列的add、poll、peek功能"""

    __slots__ = ["__push", "__pop"]

    def __init__(self):
        self.__push = Stack()
        self.__pop = Stack()

    def __str__(self):
        return str(self.__pop)

    def __check(self):
        if self.__push.is_empty() and self.__pop.is_empty():
            raise NotImplementedError("Queue is empty!")
        elif self.__pop.is_empty():
            while not self.__push.is_empty():
                self.__pop.push(self.__push.pop())

    def add(self, data):
        if data:
            self.__push.push(data)
        else:
            raise TypeError("Missing data! You must push a data rather than NULL!")

    def poll(self):
        self.__check()
        return self.__pop.pop()

    def peek(self):
        self.__check()
        return self.__pop.peek()


def sort_stack_depend_stack(ori_stack):
    """
    借助一个辅助栈完成对原始栈的排序，栈顶到栈底从大到小排序
    :param ori_stack: 原始未排序的栈
    :return: 栈顶到栈底从大到小已经排序好的栈
    """
    if ori_stack.is_empty():
        # raise RuntimeError("stack is empty!!!")
        return ori_stack
    help_stack = Stack()
    help_stack.push(ori_stack.pop())
    while not ori_stack.is_empty():
        tmp = ori_stack.pop()
        while not help_stack.is_empty() and tmp < help_stack.peek():
            ori_stack.push(help_stack.pop())
        help_stack.push(tmp)
    return help_stack
    #     while not help_stack.is_empty() and tmp > help_stack.peek():
    #         ori_stack.push(help_stack.pop())
    #     help_stack.push(tmp)
    # while not help_stack.is_empty():
    #     ori_stack.push(help_stack.pop())
    # return ori_stack


if __name__ == "__main__":
    pass
