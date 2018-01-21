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
@File:              comparision.py 
@Time:              18-1-21 下午12:12 
"""
"""
a.给定两个字符串str1和str2,如果str1和str2中出现的字符种类一样且每种字符出现的次数也是一样,那么str1和str2互为变形词,判断两字符是否为变形词.
b.给定一个字符串str1,把字符串str1前面任意的部分挪到后面形成的字符串叫做str1的旋转词,例如str1='12345',str1的旋转词有'12345','23451',
  '34512','45123'和'51234',给定两个字符串str1和str2,判断str1和str2是否互为旋转词
"""


def is_deformation(str1, str2):
    """
    判断str1和str2是否为变形词
    :type str1:str
    :type str2:str
    :param str1:
    :param str2:
    :return:
    """
    if not str1 or not str2 or len(str1) != len(str2):
        return False
    strDict = {}
    for i in str1:
        if not strDict.get(i):
            strDict[i] = 1
        else:
            strDict[i] += 1
    for i in str2:
        if strDict.get(i) and strDict.get(i) >= 1:
            strDict[i] -= 1
        # 该字符不存在或是该字符个数不同
        else:
            return False
    return True


def is_rotation(str1, str2):
    """
    判断两词是否互为旋转词
    :type str1:str
    :type str2:str
    :param str1:
    :param str2:
    :return:
    """
    if not str1 or not str2 or len(str1) != len(str2):
        return False
    return str1 in str2+str2


if __name__ == "__main__":
    pass
