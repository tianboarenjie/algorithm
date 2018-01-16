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
        3.从右到左,从下到上计算每一个值
b.给定一个整数列表value,代表数值不同的纸牌排成一条线.玩家A和玩家B依次拿走每一张纸牌,规定玩家A先拿,玩家B后拿,但是每个玩家每次只能拿走最左边或最右边
  纸牌,玩家A和玩家B都绝顶聪明.请返回最后获胜分数.
    思路：
    暴力递归
        1.定义函数front(i,j)表示如果在value[i...j]这个排列上的纸牌被绝顶聪明的人先拿,最终能获得什么分数
            front(i,j),如果i==j,只剩下一张肯定会被先拿走,返回value[i];如果i！=j,当前有两种选择value[i],那么剩下value[i+1...j]
            或则value[j],那么剩下value[i...j-1],无论选择哪种,对于剩下的纸牌列表,当前玩家都是这个纸牌列表后拿的玩家,作为聪明绝顶玩家,
            他肯定回去最大值max(value[i]+follow(i+1,j),value[j]+follow(i,j-1))
        2.定义函数follow(i,j)表示如果在value[i...j]这个排列上的纸牌被绝顶聪明的人后拿,最终能获得什么分数
            follow(i,j),如果i==j,只剩下一张肯定会被拿走,返回value[i];如果i！=j,由于是value[i...j]纸牌列表后拿,肯定被拿走了value[i]
            或是value[j],则剩余value[i+1...j]或是value[i...j-1],作为聪明绝顶的对手,肯定吧最差的情况留给了当前玩家,所以返回
            min(front(i+1,j),front(i,j-1))
    动态规划
        1.利用front[i][j]记录暴力递归中front(value,i,j)返回值,follow记录暴力递归中follow(value,i,j)返回值
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


def card_recursion(value):
    """
    纸牌博弈
    :type value:list
    :param value:
    :return:
    """

    def front(value, i, j):
        """
        先拿value[i...j]最终结果
        :type value:list
        :type i:int
        :type j:int
        :param value
        :param i:
        :param j:
        :return:
        """
        if i == j:
            return value[i]
        return max(value[i]+follow(value, i+i, j), value[j]+follow(value, i, j-1))

    def follow(value, i, j):
        """
        value[i...j]后拿最终结果
        :type value:list
        :type i:int
        :type j:int
        :param value:
        :param i:
        :param j:
        :return:
        """
        if i == j:
            return value[i]
        return min(front(value, i+1, j), front(value, i, j-1))

    if not value or len(value) == 0:
        return 0
    return max(front(value, 0, len(value)-1), follow(value, 0, len(value)-1))


def card_dynamic(value):
    """
    动态递归求解纸牌博弈
    :type value:list
    :param value:
    :return:
    """

    if not value or len(value) == 0:
        return 0
    front = [[0 for i in range(len(value))] for j in range(len(value))]
    follow = [[0 for i in range(len(value))] for j in range(len(value))]
    for i in range(len(value)):
        front[i][i] = value[i]
        for j in range(i-1, -1, -1):
            front[j][i] = max(value[j]+follow[j+1][i], value[i]+follow[j][i-1])
            follow[j][i] = min(front[j+1][i], front[j][i-1])
    return max(front[0][-1], follow[0][-1])


if __name__ == "__main__":
    pass
