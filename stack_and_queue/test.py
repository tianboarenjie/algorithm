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
@File:              test.py 
@Time:              11/26/17 10:21 PM 
"""
from min import MinImplementation1, MinImplementation2
from stack import Stack,TwoStackQueue
from .hanoi import hanoi_stack


def min():
    mi1 = MinImplementation1()
    mi1.push(4)
    print(mi1.get_min())
    mi1.push(10)
    print(mi1.get_min())
    mi1.push(1)
    print(mi1.get_min())
    mi1.pop()
    print(mi1.get_min())

    print("-"*10)
    mi2 = MinImplementation2()
    mi2.push(4)
    print(mi2.get_min())
    mi2.push(10)
    print(mi2.get_min())
    mi2.push(1)
    print(mi2.get_min())
    mi2.pop()
    print(mi2.get_min())


def two_stack_queue():
    queue = TwoStackQueue()
    queue.add(1)
    print(queue.peek())
    print(queue)
    queue.add(7)
    print(queue.peek())
    print(queue)
    print(queue.poll())
    print(queue)
    queue.add("tian")
    print(queue.peek())
    print(queue)
    print(queue.poll())
    print(queue)


def reverse():
    reversestack = Stack()
    reversestack.push(1)
    reversestack.push(2)
    reversestack.push(3)
    reversestack.push(4)
    reversestack.push(5)
    print(reversestack)
    reversestack.reverse()
    print(reversestack)


def main():
    # min()
    # two_stack_queue()
    # reverse()
    print("hanoi 3 total: %s" % hanoi_stack(3))

if __name__ == "__main__":
    main()
