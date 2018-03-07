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
@File:              substr.py 
@Time:              18-1-21 下午12:34 
"""
"""
a.给定一个字符串str1,求其中全部数字子串所代表的数字之和
    example: 'A1.3' ==> 1和3返回4    'A-1BC--12'==> -1和12返回11
b.给定一个字符串str1和一个整数k,如果str1中正好有连续的k个'0'字符出现,把k个连续'0'字符去除,返回处理后的字符串
c.给定一个字符串value,返回value的最长无重复字符子串的长度,要求时间复杂度为O(N),N为value长度
    思路：
        1.申请indexDict字典,记录某个字符index最近一次出现的位置;
        2.整型pre,如果遍历到i,pre表示必须以value[i-1]结尾下最长无重复字符子串开始位置的前一个位置,初始pre=-1;
        3.整型result,记录以每一个字符结尾情况下最长无重复子串长度的最大值;
        4.遍历value时如何同时更新pre和result,记indexDict[value[i]]为a位置
            a)pre+1为在value[i-1]结尾情况下最长无重复子串开始位置
            b)如果pre在a左边,则以value[i]结尾最长无重复子串为value[a+1...i]
            c)如果pre在a右边,则以value[i]结尾最长无重复子串为value[pre+1...i]
d.给定字符串value1和value2,求value1子串中含有value2所有字符的最小子串长度
    思路：
        1.借助几个变量
            left：遍历value1时,value1[left...right]表示框住的子串,left为左边界
            right:如上阐述right为右边界
            match：记录在value1[left...right]子串中一共欠value2多少个字符,可谓负数
            minLen:记录最小包含子串长度
        2.利用tmp字典记录value1欠value2相应字符的个数
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


def max_unique_substr(value):
    """
    给定一个字符串value,返回value的最长无重复字符子串的长度
    :type value:str
    :param value:
    :return:
    """
    if not value or value == "":
        return 0
    indexDict = {}
    pre = -1
    result = 0
    for i in range(len(value)):
        if indexDict.get(value[i]):
            pre = max(pre, indexDict.get(value[i]))
        result = max(result, i-pre)
        indexDict[value[i]] = i
    return result


def min_substr_length(value1, value2):
    """
    value1子串中含有value2所有字符的最小子串长度
    :type value1:str
    :type value2:str
    :param value1:
    :param value2:
    :return:
    """
    if not value1 or not value2 or len(value2) > len(value1):
        return 0
    import sys
    tmp = [0 for i in range(256)]
    for i in range(len(value2)):
        tmp[ord(value2[i])] += 1
    left = 0
    right = 0
    match = len(value2)
    minLen = sys.maxsize
    while right != len(value1):
        tmp[ord(value1[right])] -= 1
        if tmp[ord(value1[right])] >= 0:
            match -= 1
        if match == 0:
            while tmp[ord(value1[left])] < 0:
                tmp[ord(value1[left])] += 1
                left += 1
            minLen = min(minLen, right-left+1)
            match += 1
            tmp[ord(value1[left])] += 1
            left += 1
        right += 1
    return minLen if minLen != sys.maxsize else 0



if __name__ == "__main__":
    pass
