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
@File:              cost.py 
@Time:              18-1-11 下午10:00 
"""
"""
a.给定两个字符串value1和value2,再给定三个整数ic,dc和rc,分别代表插入删除和替换一个字符串的代价,请返回value1编辑成value2的最小代价
    思路：
    经典动态规划方法
        1.生成动态规划表dp,dp[i][j]表示value1[0...i-1]编辑成value2[0...j-1]的最小代价
        2.dp[0][0]=0,表示value1空子串编辑成value2空子串所需代价为0
        3.dp第一行即dp[0][0...N-1]表示value1空子串编辑成value2[0:i-1]最小代价,可知dp[0][i]=ic*i
        4.dp第一列即dp[0...M-1][0]表示value1[0:i-1]编辑成value2空串最小代价,可知dp[i][0]=dc*i
        5.其他位置从左到右,从上到下之可能是下面4中情况,选取最小值
            1)如果value1[i]==value2[j],这种情况下dp[i][j]=dp[i-1][j-1]
            2)如果value1[i]!=value2[j],这种情况下先把value1[0...i-2]编辑成value2[0...j-2],再将value1[i-1]替换成value2[j-1],
              这种情况下dp[i][j]=rc+dp[i-1][j-1]
            3)value1[0...i-1]先编辑成value1[i-2],即删除value1[i-1],而后由value1[i-2]编辑成value2[j-1],也即dp[i-1][j]代价,
              所以这种情况下dp[i][j]=dc+dp[i-1][j]
            4)value1[0...i-1]先编辑成value2[j-2],然后将value2[j-2]插入value2[j-1]编辑成value2[0...j-1],
              这种情况下dp[i][j]=id+dp[i][j-1]
    空间压缩动态规划
        1.由上面可知,可将dp二维压缩为一维,将dp长度设为min(len(value1)N,len(value2)M),如果value1长度更短,将对应插入删除对换一下
"""


def min_cost_of_change_str1_to_str2_dynamic_classic(value1, value2, ic, dc, rc):
    """
    value1编辑为value2的最小代价
    :type value1:str
    :type value2:str
    :type ic:int
    :type dc:int
    :type rc:int
    :param value1:
    :param value2:
    :param ic:
    :param dc:
    :param rc:
    :return:
    """
    if not value1 or not value2 or not ic or not dc or not rc:
        return 0
    row = len(value1) + 1
    col = len(value2) + 1
    dp = [[0 for i in range(col)] for j in range(row)]
    for i in range(1, col):
        dp[0][i] = ic * i
    for i in range(1, row):
        dp[i][0] = dc * i
    for i in range(1, row):
        for j in range(1, col):
            if value1[i-1] == value2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + rc
            dp[i][j] = min(dp[i][j], dp[i][j-1]+ic)
            dp[i][j] = min(dp[i][j], dp[i-1][j]+dc)
    return dp[row-1][col-1]


def min_cost_of_change_str1_to_str2_dynamic_space_compression(value1, value2, ic, dc, rc):
    """
    value1编辑为value2的最小代价
    :type value1:str
    :type value2:str
    :type ic:int
    :type dc:int
    :type rc:int
    :param value1:
    :param value2:
    :param ic:
    :param dc:
    :param rc:
    :return:
    """
    if not value1 or not value2 or not ic or not dc or not rc:
        return 0
    value1Len = len(value1)
    value2Len = len(value2)
    longer = value1 if value1Len >= value2Len else value2
    shorter = value1 if value1Len < value2Len else value2
    if shorter == value1Len:
        tmp = dc
        dc = ic
        ic = tmp
    dp = [0 for i in range(len(shorter)+1)]
    for i in range(1, len(shorter)+1):
        dp[i] = ic * i
    for i in range(1, len(longer)+1):
        pre = dp[0]
        dp[0] = dc * i
        for j in range(1, len(shorter)+1):
            tmp = dp[j]
            if longer[i-1] == shorter[j-1]:
                dp[j] = pre
            else:
                dp[j] = pre + rc
            dp[j] = min(dp[j], dp[j-1]+ic)
            dp[j] = min(dp[j], tmp+dc)
            pre = tmp
    return dp[len(shorter)]


if __name__ == "__main__":
    pass
