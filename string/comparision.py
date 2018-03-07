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
@File:              comparision.py 
@Time:              18-1-21 下午12:12 
"""
"""
a.给定两个字符串str1和str2,如果str1和str2中出现的字符种类一样且每种字符出现的次数也是一样,那么str1和str2互为变形词,判断两字符是否为变形词.
b.给定一个字符串str1,把字符串str1前面任意的部分挪到后面形成的字符串叫做str1的旋转词,例如str1='12345',str1的旋转词有'12345','23451',
  '34512','45123'和'51234',给定两个字符串str1和str2,判断str1和str2是否互为旋转词
c.给定一个字符串列表valueList,在valueList中有些位置是空,但在不为空的位置上字符串是按照字典顺序由小到大依次出现的,再给定一个字符串cStr,返回
  cStr在valueList出现的最左位置
    思路：
        1.由于题目已经说明是有序,考虑采用二分法加快
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


def get_index(valueList, cStr):
    """
    c题目的二分法解决方式
    :type valueList:list
    :type cStr:str
    :param valueList:
    :param cStr:
    :return:
    """
    if not valueList or not cStr or len(valueList) == 0:
        return -1
    result = -1
    left = 0
    right = len(valueList) - 1
    while left < right:
        mid = (left+right) // 2
        if valueList[mid] and valueList[mid] == cStr:
            result = mid
            right = left - 1
        elif valueList[mid]:
            if valueList[mid] < cStr:
                left = mid + 1
            else:
                right = mid - 1
        else:
            index = mid
            while not valueList[index] and index >= left:
                index -= 1
            if index < left or valueList[index] < cStr:
                left = mid + 1
            else:
                result = index if valueList[index] == cStr else result
                right = index - 1
    return result


if __name__ == "__main__":
    pass
