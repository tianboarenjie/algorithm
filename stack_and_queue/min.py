#!/usr/bin/env python  
# -*-coding:utf-8 -*-

""" 
@Version:           v1.0 
@Author:            tianbaorenjie
@License:           GPL license  
@Contact:           tianbaorenjie@163.com
@Site:              https://github.com/tianbaorenjie 
@Software:          PyCharm 
@Project:           py36_algorithm
@File:              min.py 
@Time:              11/26/17 9:29 PM 
"""
"""
实现一个特殊栈，在实现基本的栈功能基础上，再实现返回栈中最小元素的操作
思路:创建两个栈，一个存放数据，一个存放当前最小元素
"""

from stack import Stack

__all__ = ["MinImplementation1", "MinImplementation2"]


class MinImplementation1:
    """__min_stack空间更小，入栈出栈都需判断，以时间换空间"""
    __slots__ = ("__data_stack", "__min_stack")
    
    def __init__(self):
        self.__data_stack = Stack()
        self.__min_stack = Stack()

    def push(self, data=None):
        """首先判断__min_stack是否为空，为空直接压入__min_stack否则判断data和__min_stack栈顶大小情况，
        data小则入栈,最后data入__data_stack栈"""
        if data:
            if self.__min_stack.is_empty:
                self.__min_stack.push(data)
            elif data <= self.get_min():
                self.__min_stack.push(data)
            self.__data_stack.push(data)
        else:
            raise TypeError("Missing data! You must push a data rather than NULL!")

    def pop(self):
        """首先判断__data_stack是否为空，而后判断__data_stack出栈值与__min_stack当前最小值是否相等，
        相等则__min_stack出栈"""
        if self.__data_stack.is_empty:
            raise NotImplementedError("You stack is empty")
        value = self.__data_stack.pop()
        if value == self.get_min():
            self.__min_stack.pop()
        return value

    def get_min(self):
        if self.__min_stack.is_empty:
            raise NotImplemented("You stack is empty!")
        return self.__min_stack.peek()


class MinImplementation2:
    """__min_stack空间和__data_stack一样，只需入栈判断，以空间换时间"""
    __slots__ = ["__data_stack", "__min_stack"]
    
    def __init__(self):
        self.__data_stack = Stack()
        self.__min_stack = Stack()

    def push(self, data):
        """首先判断__min_stack是否为空，为空直接压入__min_stack否则判断data和__min_stack当前最小值min，
        data小则入栈，否则min再次入栈"""
        if data:
            if self.__min_stack.is_empty:
                self.__min_stack.push(data)
            elif data <= self.get_min():
                self.__min_stack.push(data)
            else:
                self.__min_stack.push(self.get_min())
            self.__data_stack.push(data)
        else:
            raise TypeError("Missing data! You must push a data rather than NULL!")

    def pop(self):
        if self.__data_stack.is_empty:
            raise NotImplementedError("You stack is empty")
        self.__min_stack.pop()
        return self.__data_stack.pop()

    def get_min(self):
        if self.__min_stack.is_empty:
            raise NotImplemented("You stack is empty!")
        return self.__min_stack.peek()
