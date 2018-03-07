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
@File:              path_sum.py 
@Time:              18-1-6 下午9:04 
"""
"""
a.给定一个列表paths,从左上角开始每次只能向右或者向下走,最后到达右下角位置,路径上所有数字累加起来的就是路径和,返回所有路径中最小路径和
    思路1：生成一个维数和paths一样的列表result,result[i][j]表示从左上角到i行j列位置的最小路径和
        时间复杂度为O(M*N),额外空间复杂度为O(M*N)
    思路2：生成列表result每次更新路径和都只在result中修改
"""


def minimum_path_sum_dynamic_classic(paths):
    """
    多维列表中所有路径和的最小值
    :type paths:list
    :param paths:
    :return:
    """
    if paths is None or len(paths) == 0 or paths[0] is None or len(paths[0]) == 0:
        return 0
    row = len(paths)
    col = len(paths[0])
    result = [[] for i in range(row)]
    result[0][0] = paths[0][0]
    for i in range(1, row):
        result[i][0] = result[i-1][0] + paths[i][0]
    for i in range(1, col):
        result[0][i] = result[0][i-1] + paths[0][i]
    for i in range(1, row):
        for j in range(1, col):
            result[i][j] = min(result[i-1][j], result[i][j-1]) + paths[i][j]
    return result[row-1][col-1]


def minimum_path_sum_dynamic_space_compression(paths):
    """
    使用空间压缩求解多维列表中所有路径和的最小值
    :type paths:list
    :param paths:
    :return:
    """
    if paths is None or len(paths) == 0 or paths[0] is None or len(paths[0]) == 0:
        return 0
    more = max(len(paths), len(paths[0]))
    less = min(len(paths), len(paths[0]))
    is_rowmore = (more == len(paths))
    result = [paths[0][0]]
    for i in range(1, less):
        result.append(result[i-1] + (paths[0][i] if is_rowmore else paths[i][0]))
    for i in range(1, more):
        result[0] = result[0] + (paths[i][0] if is_rowmore else paths[0][i])
        for j in range(1, less):
            result[j] = min(result[j], result[j-1]) + (paths[i][j] if is_rowmore else paths[j][i])
    return result[less-1]


if __name__ == "__main__":
    pass
