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
@File:              expectation.py 
@Time:              18-1-14 下午12:04 
"""
"""
a.给定一个只由0（假）1（真）&（逻辑与）|（逻辑或）^（异或）五种字符组成的字符串express,再给定一个布尔值desired,实现函数返回express能有多少种组合方式得到desired的结果
    思路：
        首先判断是否为有效表达式,需要符合一下几个要求放为有效表达式
            1）表达式字符串个数应该为奇数
            2）表达式偶数位置value[0,2,4...]应该为0或是1
            3）表达式奇数位置value[1,3,5...]应该为&或^或|
        1.采用暴力递归方法,将长express划分为两个部分,判断符左和判断符右,每个以此调用递归方法得到判断结果的种类,递归函数传入express表达书,start表达式开始位置,end表达式
          结束位置,desired期望的判断结果
        2.动态规划优化暴力递归,保存计算结果,true[i][j]表示express[i...j]组成True种类,false[i][j]express[i...j]组成False种类
"""


def is_valid(value):
    """
    判断表达式是否有效
    :type value:str
    :param value:
    :return:
    """
    if not value or value == "":
        return False
    for i in  range(0, len(value), 2):
        if value[i] not in "01":
            return False
    for i in range(1, len(value), 2):
        if value[i] not in "^|&":
            return False
    return True


def expectation_recursion(value, desired):
    """
    获得value表达式符合desired结果的种类
    :type value:str
    :type desired:bool
    :param value:
    :param desired:
    :return:
    """

    def process(value, start, end, desired):
        """
        分段得到value[start:end]能够得到desired结果的组合种类
        :type value:str
        :type start:int
        :type end:int
        :type desired:bool
        :param value:
        :param start:
        :param end:
        :param desired:
        :return:
        """
        if start == end:
            if value[start] == 1:
                return 1 if desired else 0
            else:
                return 0 if desired else 1
        result = 0
        # 判断True时种类
        if desired:
            for i in range(start+1, end, 2):
                if value[i] == "&":
                    result += process(value, start, i-1, True) * process(value, i+1, end, True)
                elif value[i] == "|":
                    result += process(value, start, i-1, True) * process(value, i+1, end, False)
                    result += process(value, start, i-1, False) * process(value, i+1, end, True)
                    result += process(value, start, i-1, True) * process(value, i+1, end, True)
                else:
                    result += process(value, start, i-1, True) * process(value, i+1, end, False)
                    result += process(value, start, i-1, False) * process(value, i+1, end, True)
        else:
            for i in range(start+1, end, 2):
                if value[i] == "&":
                    result += process(value, start, i-1, True) * process(value, i+1, end, False)
                    result += process(value, start, i-1, False) * process(value, i+1, end, True)
                    result += process(value, start, i-1, False) * process(value, i+1, end, False)
                elif value[i] == "|":
                    result += process(value, start, i-1, False) * process(value, i+1, end, False)
                else:
                    result += process(value, start, i-1, False) * process(value, i+1, end, False)
                    result += process(value, start, i-1, True) * process(value, i+1, end, True)
        return result


    if not is_valid(value):
        return 0
    return process(value, 0, len(value), desired)


def expectation_dynamic(value, desired):
    """
    获得value表达式符合desired结果的种类
    :type value:str
    :type desired:bool
    :param value:
    :param desired:
    :return:
    """
    if not is_valid(value):
        return 0
    true = [[0 for i in range(len(value))] for j in range(len(value))]
    false = [[0 for i in range(len(value))] for j in range(len(value))]
    true[0][0] = 1 if value[0] else 0
    false[0][0] = 0 if value[0] else 1
    for i in range(2, len(value), 2):
        true[i][i] = 1 if value[i] else 0
        false[i][i] = 0 if value[i] else 0
        for j in range(i-2, -1, -2):
            for k in range(j, i, 2):
                if value[j+1] == "&":
                    true[j][i] += true[j][k] * true[k+2][i]
                    false[j][i] += (false[j][k] + true[j][k]) * false[k+2][i] + (false[j][k] * true[k+2][i])
                elif value[j+1] == "|":
                    true[j][i] += (true[j][k] + true[j][k]) * true[k+2][i] + true[j][k] * false[k+2][i]
                    false[j][i] += true[j][k] * true[k+2][i]
                else:
                    true[j][i] += false[j][k] * true[k+2][i] + true[j][k] * false[k+2][i]
                    false[j][i] += false[j][k] * false[k+2][i] + true[j][k] * true[k+2][i]
    return true[0][len(value)-1] if desired else false[0][len(value)-1]


if __name__ == "__main__":
    pass
