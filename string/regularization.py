#!/usr/bin/env python  
# -*-coding: utf-8 -*- 

""" 
@Version:           v0.1
@Author:            tianbaorenjie
@License:           GPL License
@Contact:           tianbaorenjie@163.com
@Site:              https://github.com/tianbaorenjie 
@Software:          PyCharm 
@Project:           py363_algorithm
@File:              regularization.py 
@Time:              18-1-21 下午9:59 
"""
"""
a.给定三个字符串,str1,fro,to,已知fro字符串中无重复字符,把str1中所有fro的子串全部替换成to字符串,对连续出现fro部分要求只替换成一个to子串,返回最终
    思路：
        1.生成str1List列表,整型变量match表示匹配到fro字符串的什么位置
        2.如果str1[i]==fro[match],且match是fro最后一个字符位置,表示str1中匹配到了fro,则str1List[i]前面N个位置置为''
        3.如果str1[i]!=fro[match],表示不匹配,match置为0
        4.最后将str1List转换字符串,其中连续''字符转换为一个to字符串
b.给定一个字符串类型列表,请找出一种拼接顺序,使得将所有字符串拼接起来组成的字符串是所有可能性中字典顺序最小的,并返回这个字符串
    思路：
        1.假设两个字符分别为a,b,a和b拼接可以是a.b也可以是b.a,如果a.b的字典顺序小于b.a,则a放在前面,按照这个标准比较
c.给定一个字符串value,返回把value全部切成回文子串的最小分割数
    思路：
        1.思考需要使用动态规划思想解决,设定dp[i]表示子串value[0...i]至少需要切割多少次,才能把value[0...i]全部切成回文子串
        2.在遍历过程中,假定j（0<=j<i）,如果value[j...i]是回文串,那么dp[i]可能为dp[j-1]+1,他的意义在于既然value[j...i]
            为回文串,那么它必然是一个分割部分,剩下的value[0...j-1]继续做分割,也即是dp[j-1]
        3.如何快速判断value[j...i]是否为回文
            定义二维列表tmp[j][i]=True表示value[j...i]为回文,为False表示value[j...i]不是回文,为True有如下几种可能
                1）tmp[j][i]为1个字符
                2）tmp[j][i]为2个字符且都想等
                3）tmp[j][i]为多个字符,满足value[j]==value[i]且tmp[j+1][i-1]=True
d.给定字符串value,其中绝对不含有字符'.'和'*',再给定字符串exp,其中可以含有'.'和'*','*'不能是exp的首字符且任意两个'*'不能相邻,
  '.'代表任意一个字符,'*'代表前一个字符可以有0个或者多个,请写一个函数判断value能否被exp匹配
    思路：
        1.首先编写函数判断value和exp是否符合输入要求
        2.
"""


def replace(str1, fro, to):
    """
    替换子串
    :type str1:str
    :type fro:str
    :type to:str
    :param str1:
    :param fro:
    :param to:
    :return:
    """

    def clear(chaList, end, length):
        """
        清除chaList中匹配的字符
        :type chaList:list
        :type end:int
        :type length:int
        :param chaList:
        :param end:
        :param length:
        :return:
        """
        while length:
            chaList[end] = ""
            end -= 1
            length -= 1

    if not str1 or not fro or str1 == "" or fro == "":
        return str1
    str1List = list(str1)
    match = 0
    for i in range(len(str1List)):
        if str1List[i] == fro[match]:
            match += 1
            if match == len(fro):
                clear(str1List, i, match)
                match = 0
        else:
            match = 0
            if str1List[i] == fro[0]:
                match = 1
    result = ""
    for i in range(len(str1List)):
        if str1List[i] != "":
            result = result + str1List[i]
        elif i == 0 or str1List[i-11] != "":
            result = result + to
    return result


def lowest_str(valueList):
    """
    将valueList列表中所有元素拼接,返回字典顺序最小的拼接结果
    :type valueList:list
    :param valueList:
    :return:
    """
    if not valueList or valueList == "":
        return ""
    from functools import cmp_to_key
    tmp = sorted(valueList, key=cmp_to_key(lambda x,y: 1 if x+y > y+x else -1))
    return "".join(tmp)


def min_cuts_of_palindrome(value):
    """
    把value全部切成回文子串的最小分割数,由前至后遍历
    :type value:str
    :param value: 
    :return: 
    """
    if not value or value == "":
        return 0
    lens = len(value)
    dp = [0 for i in range(lens)]
    tmp = [[False for i in range(lens)] for j in range(lens)]
    import sys
    for i in range(lens):
        dp[i] = sys.maxsize
        for j in range(i, -1, -1):
            if value[j] == value[i] and tmp[j+1][i-1]:
                dp[i] = min(dp[i], 0 if j-1 == -1 else dp[j-1]+1)
                tmp[j][i] = True
    return dp[-1]


def is_match(value, exp):
    """
    判断value能否被exp匹配
    :type value:str
    :type exp:str
    :param value:
    :param exp:
    :return:
    """

    def is_valid(val, e):
        """
        判断val和e是否符合输入要求
        :type val:str
        :type e:str
        :param val:
        :param e:
        :return:
        """
        for i in range(len(val)):
            if val[i] == "*" or val[i] == ".":
                return False
        for i in range(len(e)):
            if e[i] == "*" and (i == 0 or e[i-1] == "*"):
                return False
        return True

    def process(val, e):
        """
        开始判断val是否能被e匹配
        :type val:str
        :type e:str
        :param val:
        :param e:
        :return:
        """
        # TODO (programme at 18-3-7): 后续继续

    if not value or not exp:
        return False
    if is_valid(value, exp):
        return process(value, exp)
    else:
        return False


if __name__ == "__main__":
    pass
