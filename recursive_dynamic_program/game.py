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
@File:              game.py 
@Time:              18-1-13 下午5:34 
"""
"""
a.给定一个二维列表map,表示一张地图,从左上角出发,每次只能向右或是向下走,直到到达右下角.每个位置表示将要遭遇的事情,为负数表示需要损失相应血量,为正数
  表示可以增加相应血量,走到每个位置血量不能少于1.为了保证能到达右下角,初始血量至少为多少,设计函数利用map返回初始血量
    思路：
        1.找到一条最优路径
        2.利用dp二维列表保存动态规划计算值,dp[i][j]走到map[i][j]起码需要的血量,最终返回dp[0][0]
        3.从右到左,从下到上计算没一个值
"""


def minHP_dynamic_classic(map):
    """
    初始血量最低值
    :type map:list
    :param map:
    :return:
    """
    if not map or len(map) == 0 or not map[0] or len(map[0]) == 0:
        return 1
    row = len(map)
    col = len(map[0])
    dp = [[1 for i in range(col)] for j in range(row)]
    dp[row-1][col-1] = 1 if map[row-1][col-1] > 0 else (1-map[row-1][col-1])
    for i in range(col-2, -1, -1):
        dp[row-1][i] = max(dp[row-1][i+1] - map[row-1][i], 1)
    for i in range(row-2, -1, -1):
        dp[i][col-1] = max(dp[i+1][col-1]-map[i][col-1], 1)
        for j in range(col-2, -1, -1):
            right = max(dp[i][j+1] - map[i][j], 1)
            down = max(dp[i+1][j] - map[i][j], 1)
            dp[i][j] = min(right, down)
    return dp[0][0]


def minHP_dynamic_space_compression(map):
    """
    空间压缩生成dp计算最低初始血量要求
    :type map:list
    :param map:
    :return:
    """
    if not map or len(map) == 0 or not map[0] or len(map[0]):
        return 1
    more = max(len(map), len(map[0]))
    less = min(len(map), len(map[0]))
    rowMore = more == len(map)
    dp = [1 for i in range(less)]
    tmp = map[len[map]-1][len(map[0])-1]
    dp[less-1] = 1 if tmp > 0 else 1-tmp
    for i in range(less-2, -1, -1):
        row = more-1 if rowMore else i
        col = i if rowMore else more-1
        dp[i] = max(dp[i+1]-map[row][col], 1)
    for i in range(more-2, -1, -1):
        row = i if rowMore else less-1
        col = less-1 if rowMore else i
        dp[less-1] = max(dp[less-1]-map[row][col], 1)
        for j in range(less-2, -1, -1):
            row = i if rowMore else j
            col = j if rowMore else i
            choose1 = max(dp[j]-map[row][col], 1)
            choose2 = max(dp[j+1]-map[row][col], 1)
            dp[j] = min(choose1, choose2)
    return dp[0]


if __name__ == "__main__":
    pass
