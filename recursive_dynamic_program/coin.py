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
@File:              coin.py 
@Time:              18-1-7 下午3:22 
"""
"""
a.给定列表coin,coin中所有的值都为正数且不重复,每个值代表一种面值的货币,每种面值的货币都可以使用任意张,再给定一个整数aim代表要找的钱数,求组成aim最少货币数.
    思路1：经典动态规划方法
        1.如果coin的长度为N,生成行数为N,列数为aim+1的动态规划表dynamic_result,dynamic_result[i][j]表示在可以任意使用coin[0...i]货币情况下,组成j所需要的最小货币数
        2.dynamic_result[0...N-1][0]表示找的钱数为0时所需要的最少货币数,应该设置为0
        3.dynamic_result[0][0...aim]表示只能使用coin[0]货币情况下找某个钱数的最小张数,如果coin[0]为2,则dynamic_result[0][2,4,6]可设置其他设置为最大整数
        4.从上到下从左到右依次计算
            完全不使用单前货币coin[i]情况下最少货币数为:dynamic_result[i-1][j]
            只是用k张当前货币coin[i]情况下最少货币数：dynamic_result[i-1][j-k*coin[i]]+k
        5.所有情况中取最终货币数最少的:
            dynamic_result[i][j]=min(dynamic_result[i-1][j-k*coin[i]]+k)
                                =>min(dynamic_result[i-1][j],dynamic_result[i][j-coin[i]]+1)
            如果j-coin[i]<0表明越界
    思路2：空间压缩的动态规划方法
b.给定列表coin,coin中所有值都为正数,每个值仅代表一张钱的面值,再给定一个整数aim代表要找的钱数,求组成aim的最少货币数.
    思路1：经典动态规划方法和方法a的类似
c.给定列表coin,coin中所有值都为正数且不重复,每个值代表一种面值的货币,每种面值的货币可以使用任意张,在给定一个整数aim代表要找的钱数,求换钱有多少中方法
    思路1：暴力递归
    思路2：记忆搜索
        需要记录每个递归过程的结果,record[i][j]=0表示process(i,j)没有计算过,为-1表示计算过但是返回值为0
    思路3：3种动态规划
        第一种时间复杂度为O(N*aim^2)
        第二种时间复杂度为O(N*aim)
        第三种是对第二种进行了空间压缩,时间复杂度为O(N*aim)
"""
import sys


def min_coins_with_a_dynamic_classic(coin, aim):
    """
    解决问题a
    :type coin:list
    :type aim:int
    :param coin:
    :param aim:
    :return:
    """
    if coin is None or len(coin) == 0 or aim < 0:
        return -1
    category = len(coin)
    maxsize = sys.maxsize
    dynamic_result = [[0] for i in range(category)]
    # 计算第一行
    for i in range(1, aim+1):
        dynamic_result[0].append(maxsize)
        if i-coin[0] >= 0 and dynamic_result[0][i-coin[0]] != maxsize:
            dynamic_result[0][i] = dynamic_result[0][i-coin[0]] + 1
    for i in range(1, category):
        for j in range(1, aim+1):
            left = maxsize
            if j-coin[i] >= 0 and dynamic_result[i][j-coin[i]] != maxsize:
                left = dynamic_result[i][j-coin[i]] + 1
            dynamic_result[i].append(min(left, dynamic_result[i-1][j]))
    return dynamic_result[-1][aim] if dynamic_result[-1][aim] != maxsize else -1


def min_coins_with_a_dynamic_space_compression(coin, aim):
    """
    解决问题a,动态规划表使用空间压缩
    :type coin:list
    :type aim:int
    :param coin:
    :param aim:
    :return:
    """
    if coin is None or len(coin) == 0 or aim < 0:
        return -1
    category = len(coin)
    maxsize = sys.maxsize
    dynamic_result = [0]
    for i in range(1, aim+1):
        dynamic_result.append(maxsize)
        if i-coin[0] >= 0 and dynamic_result[i-coin[0]] != maxsize:
            dynamic_result[i] = dynamic_result[i-coin[0]] + 1
    for i in range(1, category):
        for j in range(1, aim+1):
            left = maxsize
            if j-coin[i] >= 0 and dynamic_result[j-coin[i]] != maxsize:
                left = dynamic_result[j-coin[i]] + 1
            dynamic_result[j] = min(left, dynamic_result[j])
    return dynamic_result[aim] if dynamic_result[aim] != maxsize else -1


def min_coins_with_b_dynamic_classic(coin, aim):
    """
    解决问题b
    :type coin:list
    :type aim:int
    :param coin:
    :param aim:
    :return:
    """
    if coin is None or len(coin) == 0 or aim < 0:
        return -1
    num = len(coin)
    maxsize = sys.maxsize
    dynamic_result = [[0] for i in range(num)]
    for i in range(1, aim+1):
        dynamic_result[0].append(maxsize)
    if coin[0] <= aim:
        dynamic_result[0][coin[0]] = 1
    for i in range(1, num):
        for j in range(1, aim+1):
            left = maxsize
            if j-coin[i] >= 0 and dynamic_result[i-1][j-coin[i]] != maxsize:
                left = dynamic_result[i-1][j-coin[i]] + 1
            dynamic_result[i].append(min(left, dynamic_result[i-1][j]))
    return dynamic_result[-1][aim] if dynamic_result[-1][aim] != maxsize else -1


def min_coins_with_b_dynamic_space_compression(coin, aim):
    """
    解决问题b,动态规划表使用空间压缩
    :type coin:list
    :type aim:int
    :param coin:
    :param aim:
    :return:
    """
    if coin is None or len(coin) == 0 or aim < 0:
        return -1
    num = len(coin)
    maxsize = sys.maxsize
    dynamic_result = [0]
    for i in range(1, aim+1):
        dynamic_result.append(maxsize)
    if coin[0] <= aim:
        dynamic_result[coin[0]] = 1
    for i in range(1, num):
        for j in range(1, aim+1):
            left = maxsize
            if j-coin[i] >= 0 and dynamic_result[j-coin[i]] != maxsize:
                left = dynamic_result[j-coin[i]] + 1
            dynamic_result[j] = min(left, dynamic_result[j])
    return dynamic_result[aim] if dynamic_result[aim] != maxsize else -1


def methods_coins_by_violent_recursion(coin, aim):
    """
    暴力递归获得找钱的方法数
    :type coin:list
    :type aim:int
    :param coin:
    :param aim:
    :return:
    """

    def process(coins, index, aims):
        """
        暴力递归
        :type coins:list
        :type index:int
        :type aims:int
        :param coins:
        :param index:
        :param aims:
        :return:
        """
        result = 0
        if index == len(coins)-1:
            result = 1 if aims == 0 else 0
        else:
            i = 0
            while coins[index]*i <= aims:
                result += process(coins, index+1, aims-coins[index]*i)
                i += 1
        return result

    if coin is None or len(coin) == 0 or aim < 0:
        return 0
    return process(coin, 0, aim)


def methods_coins_by_remember_search(coin, aim):
    """
    暴力破解的优化,记忆搜索1
    :type coin:list
    :type aim:int
    :param coin:
    :param aim:
    :return:
    """

    def process(coins, index, aims, records):
        """
        记忆搜索
        :type coins:list
        :type index:int
        :type aims:int
        :type records:list
        :param coins:
        :param index:
        :param aims:
        :param records:
        :return:
        """
        result = 0
        if index == len(coins)-1:
            result = 1 if aims == 0 else 0
        else:
            for i in range(0, aims//coins[index]+1):
                record_result = records[index+1][aims-coins[index]*i]
                if record_result != 0:
                    result += record_result if record_result != -1 else record_result
                else:
                    result += process(coins, index+1, aims-coins[index*i], records)
        records[index][aims] = result if result else -1
        return result


    if coin is None or len(coin) == 0 or aim < 0:
        return 0
    record = [[0 for i in range(1,aim+1)] for j in range(0, len(coin))]
    return process(coin, 0, aim, record)


def methods_coins_by_dynamic_classic(coin, aim):
    """
    使用动态规划求解
    :type coin:list
    :type aim:int
    :param coin:
    :param aim:
    :return:
    """
    if coin is None or len(coin) == 0 or aim < 0:
        return 0
    dynamic_result = [[0 for i in range(aim+1)] for j in range(len(coin))]
    for i in range(len(coin)):
        dynamic_result[i][0] = 1
    for i in range(1, (aim+1)//(coin[0])+1):
        dynamic_result[0][coin[0]*i] = 1
    for i in range(1, len(coin)):
        for j in range(1, aim+1):
            num = 0
            for k in range(j//coin[i]+1):
                num += dynamic_result[i-1][j-coin[i]*k]
            dynamic_result[i][j] = num
    return dynamic_result[-1][aim]


def methods_coins_by_dynamic_optimization(coin, aim):
    """
    优化动态规划求解
    :type coin:list
    :type aim:int
    :param coin:
    :param aim:
    :return:
    """
    if coin is None or len(coin) == 0 or aim < 0:
        return 0
    dynamic_result = [[0 for i in range(aim+1)] for j in range(len(coin))]
    for i in range(len(coin)):
        dynamic_result[i][0] = 1
    for i in range(1, aim//coin[0]+1):
        dynamic_result[0][coin[0]*i] = 1
    for i in range(1, len(coin)):
        for j in range(1, aim+1):
            dynamic_result[i][j] = dynamic_result[i-1][j]
            dynamic_result[i][j] += dynamic_result[i][j-coin[i]] if j-coin[i] > 0 else 0
    return dynamic_result[-1][aim]


def methods_coins_by_dynamic_optimization_and_space_compression(coin, aim):
    """
    优化动态规划并压缩空间求解
    :type coin:list
    :type aim:int
    :param coin:
    :param aim:
    :return:
    """
    if coin is None or len(coin) == 0 or aim < 0:
        return 0
    dynamic_result = [0 for i in range(aim+1)]
    for i in range(aim//coin[0]+1):
        dynamic_result[coin[0]*i] = 1
    for i in range(1, len(coin)):
        for j in range(1, aim+1):
            dynamic_result[j] += dynamic_result[j-coin[i]] if j-coin[i] >= 0 else 0
    return dynamic_result[aim]


if __name__ == "__main__":
    pass
