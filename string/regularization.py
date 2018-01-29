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
@File:              regularization.py 
@Time:              18-1-21 下午9:59 
"""
"""
a.给定三个字符串,str1,fro,to,已知fro字符串中无重复字符,把str1中所有fro的子串全部替换成to字符串,对连续出现fro部分要求只替换成一个to子串,返回最终
    思路：
        1.生成str1List列表,整型变量match表示匹配到fro字符串的什么位置
        2.如果str1[i]==fro[match],且match是fro最后一个字符位置,表示str1中匹配到了fro,则str1List[i]前面N个位置置为''
        3.如果str1[i]!=fro[match],表示不匹配,match置为0
        4.最后将str1List转换字符串,其中连续''字符转换为一个to字符串
"""


def replace(str1, fro, to):
    """
    替换子串
    :type str1:str
    :type fro:str
    :type to:str
    :param str1:
    :param fro:
    :param to:
    :return:
    """

    def clear(chaList, end, length):
        """
        清除chaList中匹配的字符
        :type chaList:list
        :type end:int
        :type length:int
        :param chaList:
        :param end:
        :param length:
        :return:
        """
        while length:
            chaList[end] = ""
            end -= 1
            length -= 1

    if not str1 or not fro or str1 == "" or fro == "":
        return str1
    str1List = list(str1)
    match = 0
    for i in range(len(str1List)):
        if str1List[i] == fro[match]:
            match += 1
            if match == len(fro):
                clear(str1List, i, match)
                match = 0
        else:
            match = 0
            if str1List[i] == fro[0]:
                match = 1
    result = ""
    for i in range(len(str1List)):
        if str1List[i] != "":
            result = result + str1List[i]
        elif i == 0 or str1List[i-11] != "":
            result = result + to
    return result




if __name__ == "__main__":
    pass