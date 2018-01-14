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
@File:              transformation.py 
@Time:              18-1-14 上午9:54 
"""
"""
a.给定一个字符串value,value全部由数字字符组成,长度为N,如果value中某一个或某相邻两个字符组成的子串在1～26之间,则这个子串可以转换为一个字母,规定"1"转换"A",
  "2"转换"B","3"转换"C"..."26"转换"Z",写一个函数实现求解value有多少种不同的转换结果
    思路：
        暴力递归
            1.定义process(i)0<=i<=N函数,process(i)计算当前value[i]位置转换种类,表示value[0...i-1]已经转换完成,而value[i...N-1]还没开始转换,
            2.如果i==N-1,表明计算到value[N-1],直接返回1
            3.不满足1.2.又有value[i]=="0",表明value[0...i-1]转换完成,value[i]==0,不可能有正确转换格式,直接返回0
            4.不满足1.2.3.,表明value[i]=[1~9],又value可能属于[A~Z],因此process(i)=process(i+1)
            5.如果value[i:i+2]==[10~26],表明可以转换为[A-Z],此时process(i)+=process(i+2)
        优化递归
            1.思考可知process(i)只依赖于process(i+1)和process(i+2),从前到后计算会导致时间复杂度O(2^N),额外空间复杂度O(N)
            2.可以思考从后到前计算
"""


def transformation_str_recursion(value):
    """
    数字转换为字符串
    :type value:str
    :param value:
    :return:
    """

    def process(value, index):
        """
        判定value[index]转换情况
        :type value:str
        :type index:int
        :param value:
        :param index:
        :return:
        """
        if index == len(value):
            return 1
        if value[index] == "0":
            return 0
        result = process(value, index+1)
        if ((index+1 < len(value)) and (int(value[index])*10 + int(value[index+1]) < 27)):
            result += process(value, index+2)
        return result

    if not value or value == "":
        return 0
    return process(value, 0)


def transformation_str_recursive_optimization(value):
    """
    优化递归求解value转换字符串结果
    :type value:str
    :param value:
    :return:
    """
    if not value or value == "":
        return 0
    cur = 1 if value[len(value)-1] != 0 else 0
    follow = 1
    tmp = 0
    for i in range(len(value)-2, -1, -1):
        if value[i] == "0":
            follow = cur
            cur = 0
        else:
            tmp = cur
            if int(value[i])*10 + int(value[i+1]) < 27:
                cur += follow
        follow = tmp
    return cur


if __name__ == "__main__":
    pass
