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
@File:              common.py 
@Time:              18-1-10 下午8:19 
"""
"""
a.给定两个字符串value1和value2,返回两个字符串的最长公共子序列
    example:  value1="1A2C3D4B56"  value2="B1D23CA45B6A"  ===>最长公共子序列为"123456"或"12C4B6"
    思路：
        动态规划表生成
            1.设计动态规划表,设value1长度M,value2长度N,生成M行N列的M*N的dp动态规划表（列表）,dp[i][j]表示value1[0...i-1]与value2[0...j-1]最长公共子序列长度
            2.初始化第一列dp[0...M-1][0]和第一行dp[0][0..N-1],规则一样,如果第一列value1[i]和value2[0]相等,则dp[i-1][0]及其以后的为1,前面的设置为0,第一行同理
            3.根据实际情况修改dp[i][j],可能是dp[i-1[j],可能dp[i][j-1]也可能dp[i-1][j-1]+1
        动态规划表逆推最长公共子序列
            1.i表示行数,j表示列数,如果dp[i][j]大于dp[i-1][j]和dp[i][j-1],表明value1[i]与value2[j]相等,应当加入result
            2.如果dp[i][j]与dp[i-1][j]相等,表明决策来源于上,所以上移动
            3.如果dp[i][j]与dp[i][j-1]相等,表明决策来源于左,所以左移动
            4.如果dp[i][j]与dp[i][j-1],dp[i-1][j]都相等,无所谓左移还是上移
b.给定两个字符串value1和value2,返回两个字符串最长公共子串,value1长度M,value2长度N,实现时间复杂度O(M*N),额外空间复杂度O(1)
    example: value1="1AB2345CD" value2="12345EF"  ===>最长公共子串"2345"
    思路：生成动态规划表不一样,由动态规划表生成最长公共字串是一样的逻辑
        经典动态规划
            1.生成M行N列的列表dp,dp[i][j]表示以value1[i]和value2[j]结尾（两字符相同）的最长公共字串长度
            2.第一行第一列将本value的第一个字符（index=0）与另一子串依次比较,相等置1不等置0
            3.而后依次判断,判定dp[i][j],如果value1[i]与value[j]相等,则置dp[i][j]=dp[i-1][j-1]+1
        空间压缩动态规划
            1.斜方向计算,dp[i][j]依赖dp[i-1][j-1]
"""


def longest_common_subsequence(value1, value2):
    """
    得到value1和value2的最长公共子序列
    :type value1:str
    :type value2:str
    :param value1:
    :param value2:
    :return:
    """

    def get_dp(value1, value2):
        """
        获得dp动态规划表
        :type value1:str
        :type value2:str
        :param value1:
        :param value2:
        :return:
        """
        dpRecords = [[0 for i in range(len(value2))] for j in range(len(value1))]
        dpRecords[0][0] = 1 if value1[0] == value2[0] else 0
        for i in range(1, len(value2)):
            dpRecords[0][i] = max(dpRecords[0][i - 1], 1 if value2[i] == value1[0] else 0)
        for i in range(1, len(value1)):
            dpRecords[i][0] = max(dpRecords[i - 1][0], 1 if value1[i] == value2[0] else 0)
        for i in range(1, len(value1)):
            for j in range(1, len(value2)):
                dpRecords[i][j] = max(dpRecords[i - 1][j], dpRecords[i][j - 1])
                if value1[i] == value2[j] and dpRecords[i - 1][j] == dpRecords[i][j - 1]:
                    dpRecords[i][j] = max(dpRecords[i][j], dpRecords[i - 1][j - 1] + 1)
        return dpRecords

    if value1 is None or value2 is None or len(value1) == 0 or len(value2) == 0:
        return ""
    indexValue1 = len(value1)-1
    indexValue2 = len(value2)-1
    dpRecords = get_dp(value1, value2)
    result = []
    length = dpRecords[indexValue1][indexValue2]
    while length >= 0:
        if indexValue1 > 0 and dpRecords[indexValue1][indexValue2] == dpRecords[indexValue1-1][indexValue2]:
            indexValue1 -= 1
        elif indexValue2 > 0 and dpRecords[indexValue1][indexValue2] == dpRecords[indexValue1][indexValue2-1]:
            indexValue2 -= 1
        else:
            result.insert(0, value1[indexValue1])
            indexValue1 -= 1
            indexValue2 -= 1
            length -= 1
    return "".join(result)


def longest_common_substr_classic(value1, value2):
    """
    获取value1和value2最长公共子串
    :type value1:str
    :type value2:str
    :param value1:
    :param value2:
    :return:
    """

    def get_dp(value1, value2):
        """
        获得动态规划表记录
        :type value1:str
        :type value2:str
        :param value1:
        :param value2:
        :return:
        """
        dpRecords = [[0 for i in range(len(value2))] for j in range(len(value1))]
        for i in range(len(value1)):
            if value1[i] == value2[0]:
                dpRecords[i][0] = 1
        for i in range(1, len(value2)):
            if value2[i] == value1[0]:
                dpRecords[0][i] = 1
        for i in range(1, len(value1)):
            for j in range(1, len(value2)):
                if value1[i] == value2[j]:
                    dpRecords[i][j] = dpRecords[i-1][j-1] + 1
        return dpRecords
    if value1 is None or value2 is None or len(value1) == 0 or len(value2) == 0:
        return ""
    dpRecords = get_dp(value1, value2)
    end = 0
    length = 0
    for i in range(len(value1)):
        for j in range(len(value2)):
            if dpRecords[i][j] > length:
                end = i
                length = dpRecords[i][j]
    return "".join(value1[end+1-length: end+1])


def longest_common_substr(value1, value2):
    """
    获取value1和value2最长公共子串
    :type value1:str
    :type value2:str
    :param value1:
    :param value2:
    :return:
    """
    if value1 is None or value2 is None or len(value1) == 0 or len(value2) == 0:
        return ""
    row = 0
    col = len(value2)-1
    maxLen = 0
    end = 0
    # 从右到左,从上到下,每次遍历都是斜向右下
    while row < len(value1):
        i = row
        j = col
        length = 0
        while i < len(value1) and j < len(value2):
            if value1[i] != value2[j]:
                length = 0
            else:
                length += 1
            if length > maxLen:
                maxLen = length
                end = i
            i += 1
            j += 1
        if col > 0:
            col -= 1
        else:
            row += 1
    return "".join(value1[end+1-maxLen:end+1])


if __name__ == "__main__":
    pass
