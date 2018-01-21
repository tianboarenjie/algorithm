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
@File:              substr.py 
@Time:              18-1-21 下午12:34 
"""
"""
a.给定一个字符串str1,求其中全部数字子串所代表的数字之和
    example: 'A1.3' ==> 1和3返回4    'A-1BC--12'==> -1和12返回11
b.给定一个字符串str1和一个整数k,如果str1中正好有连续的k个'0'字符出现,把k个连续'0'字符去除,返回处理后的字符串
"""


def substr_sun(str1):
    """
    子串数字之和
    :type str1:str
    :param str1:
    :return:
    """
    if not str1:
        return 0
    num = 0
    result = 0
    isMinus = False
    for i in range(len(str1)):
        cur = str1[i]
        if cur not in "1234567890":
            result += num
            num = 0
            if cur == "-":
                isMinus = not isMinus
        else:
            cur = int(cur)
            num = num*10 + (-cur if isMinus else cur)
            isMinus = False
    return result + num


def remove_k_zero(str1, k):
    """
    删除str1中连续的k个'0'
    :type str1:str
    :type k:int
    :param str1:
    :return:
    """
    if not str1 or k < 1:
        return str1
    chas = list(str1)
    count = 0
    start = -1
    for i in range(len(chas)):
        if chas[i] == "0":
            count += 1
            start = i if start == -1 else start
        else:
            if count == k:
                while count:
                    chas[start] = ""
                    start += 1
                    count -= 1
            count = 0
            start = -1
    if count == k:
        while count:
            chas[start] = ""
            start += 1
            count -= 1
    return "".join(chas)


if __name__ == "__main__":
    pass
