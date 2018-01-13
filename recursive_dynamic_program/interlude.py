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
@File:              interlude.py 
@Time:              18-1-13 下午3:29 
"""
"""
a.给定三个字符串value1,value2,aim,如果aim包含且仅包含value1和value2的所有字符,并且在aim中属于value1的字符之间保持原来在value1中的顺序,属于
  value2的字符之间保持原来在value2的顺序,那么称aim是value1和value2的交错组合,实现函数判断aim是否是value1和value2的交错组合
    思路：M=len(value1)   N=len(value2)
    经典动态规划
        1.aim如果是由value1和value2交错组成,则aim长度一定是M+N,否则返回False
        2.组成二维dp动态规划表,dp[i][j]表示aim[0...i+j-1]是否由value1[0...i-1]和value2[0...j-1]交错组成,判断从左到右从上到下
        3.dp[0][0]为True,dp第一列也即dp[0...M-1][0],只有aim[0...i-1]等于value1[0...i-1]才置dp[i][0]=True,否则为False
        3.dp第一行也即dp[0][N-1],只有aim[0...i-1]等于value2[0...i-1]才置dp[0][i]=True,否则为False
        4.其他位置的dp[i][j]由如下几种情况决定：
            1）dp[i-1][j]表示aim[0...i+j-2]能否被value1[0...i-2]和value2[0...j-1]交错组成,如果为True,且value1[i-1]等于aim[i+j-1]
              说明value1[i-1]可以作为交错组成aim[0...i+j-1]最后一个字符,此时dp[i][j]=True
            2）dp[i][j-1]表示aim[0...i+j-2]能否被value1[0...i-1]和value2[0...j-2]交错组成,如果为True,且value2[j-1]等于aim[i+j-1]
              说明value2[j-1]可以作为交错组成aim[0...i+j-1]最后一个字符,此时dp[i][j]=True
            3）其他情况dp[i][j]=False
    空间压缩动态规划：参考cost
"""


def is_interlude_str_dynamic_classic(value1, value2, aim):
    """
    判断aim是否是value1和value2交错组成的
    :type value1:str
    :type value2:str
    :type aim:str
    :param value1:
    :param value2:
    :param aim:
    :return:
    """
    if not value1 or not value2 or not aim:
        return False
    if len(aim) != (len(value1) + len(value2)):
        return False
    dp = [[False for i in range(len(value2)+1)] for j in range(len(value1)+1)]
    dp[0][0] = True
    for i in range(1, len(value1)+1):
        if value1[i-1] != aim[i-1]:
            break
        dp[i][0] = True
    for i in range(1, len(value2)+1):
        if value2[i-1] != aim[i-1]:
            break
        dp[0][i] = True
    for i in range(1, len(value1)+1):
        for j in range(1, len(value2)+1):
            if (dp[i-1][j] and value1[i-1] == aim[i+j-1]) or (dp[i][j-1] and value2[j-1] == aim[i+j-1]):
                dp[i][j] = True
    return dp[len(value1)][len(value2)]


def is_interlude_str_dynamic_space_compression(value1, value2, aim):
    """
    空间压缩生产动态规划表验证aim是否是value1和value2的交错组成
    :type value1:str
    :type value2:str
    :type aim:str
    :param value1:
    :param value2:
    :param aim:
    :return:
    """
    if not value1 or not value2 or not aim:
        return False
    if len(aim) != (len(value1) + len(value2)):
        return False
    longer = value1 if len(value1) >= len(value2) else value2
    shorter = value1 if len(value1) < len(value2) else value2
    dp = [False for i in range(len(shorter)+1)]
    dp[0] = True
    for i in range(1, len(shorter)+1):
        if shorter[i-1] != aim[i-1]:
            break
        dp[i] = True
    for i in range(1, len(longer)+1):
        dp[0] = dp[0] and longer[i-1] == aim[i-1]
        for j in range(1, len(shorter)+1):
            if (dp[j-1] and shorter[j-1] == aim[i+j-1]) or (dp[j] and longer[i-1] == aim[i+j-1]):
                dp[j] = True
            else:
                dp[j] = False
    return dp[len(shorter)]


if __name__ == "__main__":
    pass
