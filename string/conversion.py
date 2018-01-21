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
@File:              conversion.py 
@Time:              18-1-21 下午9:38 
"""
"""
a.给定一个字符串str1,如果str1符合日常书写的整数规则,返回str1能代表的整数值,否则返回0
"""
import sys


def convert_integer(str1):
    """
    将字符串转换为能表达的整数值
    :type str1:str
    :param str1:
    :return:
    """

    def is_valid(str1):
        """
        判断str1是否符合整数书写规范
        :type str1:str
        :param str1:
        :return:
        """
        if str1[0] not in "-0123456789":
            return False
        if str1[0] == "-" and (len(str1)==1 or str1[1]==0):
            return False
        if str1[0] == "0" and len(str1) > 1:
            return False
        for i in str1[1:]:
            if i not in "0123456789":
                return False
        return True

    if not str1 or str1 == "":
        return 0
    if not is_valid(str1):
        return 0
    isMinus = True if str1[0] == "-" else False
    result = 0
    for cur in str1[1 if isMinus else 0:]:
        cur = int(cur)
        result = result*10 + cur
    return -result if isMinus else result


if __name__ == "__main__":
    pass
