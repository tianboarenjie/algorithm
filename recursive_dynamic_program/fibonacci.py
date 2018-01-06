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
@File:              fibonacci.py 
@Time:              18-1-6 下午4:58 
"""
"""
a.给定整数N,返回斐波那契数列的第N项
    思路：f(n)=f(n-1)+f(n-2),f(1)=1,f(2)=1
        (f(n),f(n-1))=(f(n-1),f(n-2))*|1,1;1,0|=(f(2),f(1))*|1,1;1,0|^(n-2)
b.给定整数N,代表台阶数,一次可以跨2个或者1个台阶,返回有多少种走法
    思路：f(n)=f(n-1)+f(n-2),f(1)=1,f(2)=2
        (f(n),f(n-1))=(f(n-1),f(n-2))*|1,1;1,0|=(f(2),f(1))*|1,1;1,0|^(n-2)
c.假设农场中成熟的母牛每年只会生1头小母牛,并且永远不会死,第一年农场有1头成熟母牛,从第二年开始母牛开始生小母牛,每头小母牛3年之后成熟又可以生小母牛
  给定整数N,求出N年之后牛的数量
    思路：f(n)=f(n-1)+f(n-3),f(1)=1,f(2)=2,f(3)=3
        (f(n),f(n-1),f(n-2))=(f(n-1),f(n-2),f(n-3))*|1,1,0;0,0,1;1,1,0,0|=(f(3),f(2),f(1))*|1,1,0;0,0,1;1,0,0|^(n-3)
要求：所有问题均实现时间复杂度为O(logN)的解法
"""


def muli_matrix(mat1, mat2):
    """
    :type mat1:list
    :type mat2:list
    :param mat1:
    :param mat2:
    :return:
    """
    res = [[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res


def matrix_power(mat1, pow1):
    """
    :type mat1:list
    :type pow1:int
    :param mat1:
    :param pow1:
    :return:
    """
    # 单位矩阵
    res = [[0 if i != j else 1 for i in range(len(mat1[0]))] for j in range(len(mat1))]
    tmp = mat1
    while pow1 > 0:
        if pow1 & 1 != 0:
            res = muli_matrix(res, tmp)
        tmp = muli_matrix(tmp, tmp)
        pow1 >>= 1
    return res

def fibonacci_matrix(num):
    """
    利用矩阵求解斐波那契数组第num项值
    :type num:int
    :param num:
    :return:
    """

    if num < 1:
        return 0
    if num in [1,2]:
        return 1
    base = [[1,1], [1,0]]
    result = matrix_power(base, num-2)
    return result[0][0] + result[1][0]


def stair_matrix(num):
    """
    变形斐波那契数组
    :type num:int
    :param num:
    :return:
    """
    if num < 1:
        return 0
    if num in [1,2]:
        return num
    base = [[1,1], [1,0]]
    result = matrix_power(base, num-2)
    return 2*result[0][0] + result[1][0]


def fibonacci1_matrix(num):
    if num < 1:
        return 0
    if num in [1,2,3]:
        return num
    base = [[1,1,0], [0,0,1], [1,0,0]]
    result = matrix_power(base, num-3)
    return 3*result[0][0] + 2*result[1][0] + result[2][0]


if __name__ == "__main__":
    pass
