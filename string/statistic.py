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
@File:              statistic.py 
@Time:              18-1-25 上午12:00 
"""
"""
a.给定一个字符串str1,返回str1的统计字符串,例如'aaaabbadddffc'的统计字符串为'a_4_b_2_a_1_d_3_f_2_c_1'
b.给定一个a中统计字符串cStr,一个整数index,返回cStr表示原始字符串上的第index个字符
c.给定一个字符串,判断串中是否所有字符都只出现一次
"""


def get_count_string(str1):
    """
    获得统计字符串
    :type str1:str
    :param str1:
    :return:
    """
    if not str1 or str1 == "":
        return ""
    result = str1[0]
    count = 1
    for i in range(1, len(str1)):
        if str1[i] == str1[i-1]:
            count += 1
        else:
            result = result + "_" + str(count) + "_" + str1[i]
            count = 1
    return result + "_" + str(count)


def get_char_at(cStr, index):
    """
    获取原始字符串中第index个字符
    :type cStr:str
    :type index:int
    :param cStr:
    :param index:
    :return:
    """
    if not cStr or cStr == "" or index < 0:
        return ""
    isChar = True
    result = ""
    num = 0
    counts = 0
    for i in range(len(cStr)):
        if cStr[i] == "_":
            isChar = not isChar
        elif isChar:
            counts += num
            if counts > index:
                return result
            result = cStr[i]
            num = 0
        else:
            num = num*10 + int(cStr[i])
    return result if (counts+num)>index else ""


def is_unique(cStr):
    """
    字符串中字符是否唯一
    :type cStr:str
    :param cStr:
    :return:
    """
    if not cStr:
        return True
    tmp = ""
    for i in cStr:
        if i in tmp:
            return False
        tmp += i
    return True


if __name__ == "__main__":
    pass
