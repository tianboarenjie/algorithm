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
@File:              statistic.py 
@Time:              18-1-25 上午12:00 
"""
"""
a.给定一个字符串str1,返回str1的统计字符串,例如'aaaabbadddffc'的统计字符串为'a_4_b_2_a_1_d_3_f_2_c_1'
b.给定一个a中统计字符串cStr,一个整数index,返回cStr表示原始字符串上的第index个字符
c.给定一个字符串,判断串中是否所有字符都只出现一次
d.给定一个字符串列表valueList,再给定两个字符串str1和str2,返回在valueList中str1与str2的最小距离,如果str1和str2为None,或者不在valueList中,
  返回-1
    思路：
        1.变量last1记录最后一个出现str1的位置,last2记录最后一次出现str2的位置
        2.minDistance每次判断都更新,只要last1和last2都不为-1时才更新为新值,利用
          类似min（minDistance, minDistance if last1!=-1 else index-last1）更新minDistance
e.给定一个字符串str1,str1表示一个公式,公式里可能有整数,加减乘除符号和左右括号,返回公式里的计算结果.
    思路：假设str1一定是正确公式且合法
        1.采用递归方式,遍历str1,最初str1整个都在递归中,遇到'('后将'('后放入新递归中,遇到')'或是str1遍历完成递归结束
        2.要判定递归结果是否为负数,如果是负数需要用括号括起来
f.给定一个整数N,求出'0'和'1'字符组成的长度为N的所有字符串中,满足'0'字符的左边必须有'1'的字符串数量
    思路：
        1.思考可知N=1时为1,N=2时为2,R(N)表示满足条件的字符串数量Fi表示满足此条件字符的i位置字符
        2.字符串位置i为0...N-1,,F0可知必须为1,F1=1时,满足条件的有F(N-1),F1=0时,满足条件的有F(N-2) 
g.给定一个字符串value,value一定是若干新类型字符正确组合结果,再给定一个整型index,代表value中位置,返回value中index位置指中的新类型字符
    新类型字符长度可为1也可为2,新类型字符可以是消协字母,大写字母加小写字母,大写字母加大写字母
"""


def get_count_string(str1):
    """
    获得统计字符串
    :type str1:str
    :param str1:
    :return:
    """
    if not str1 or str1 == "":
        return ""
    result = str1[0]
    count = 1
    for i in range(1, len(str1)):
        if str1[i] == str1[i-1]:
            count += 1
        else:
            result = result + "_" + str(count) + "_" + str1[i]
            count = 1
    return result + "_" + str(count)


def get_char_at(cStr, index):
    """
    获取原始字符串中第index个字符
    :type cStr:str
    :type index:int
    :param cStr:
    :param index:
    :return:
    """
    if not cStr or cStr == "" or index < 0:
        return ""
    isChar = True
    result = ""
    num = 0
    counts = 0
    for i in range(len(cStr)):
        if cStr[i] == "_":
            isChar = not isChar
        elif isChar:
            counts += num
            if counts > index:
                return result
            result = cStr[i]
            num = 0
        else:
            num = num*10 + int(cStr[i])
    return result if (counts+num)>index else ""


def is_unique(cStr):
    """
    字符串中字符是否唯一
    :type cStr:str
    :param cStr:
    :return:
    """
    if not cStr:
        return True
    tmp = ""
    for i in cStr:
        if i in tmp:
            return False
        tmp += i
    return True


def min_distance(valueList, str1, str2):
    """
    valueList中str1和str2最小距离
    :type valueList:list
    :type str1:str
    :type str2:str
    :param valueList:
    :param str1:
    :param str2:
    :return:
    """
    if not valueList or not str1 or not str2:
        return -1
    if str1 == str2:
        return 0
    last1 = -1
    last2 = -1
    minDistance = -2
    for index in range(len(valueList)):
        if valueList[index] == str1:
            minDistance = min(minDistance, minDistance if last2 == -1 else abs(index-last2))
            last1 = index
        elif valueList[index] == str2:
            minDistance = min(minDistance, minDistance if last1 == -1 else abs(index-last1))
            last2 = index
    return minDistance if minDistance != -2 else -1


def result_from_expression(expStr):
    """
    通过expStr字符串得到字符串所代表表达式的值
    :type expStr:str
    :param expStr:
    :return:
    """

    def value(exp, index):
        """
        递归函数,消除exp总的括号,但遇到(时进入新的递归,返回表达式所代表的值以及遍历的下一个位置
        :type exp:str
        :type index:int
        :param exp:
        :param index:
        :return:
        """
        dep = []
        pre = 0
        while index < len(exp) and exp[index] != ")":
            if exp[index] >= "0" and exp[index] <= "9":
                pre = pre*10 + int(exp[index])
                index += 1
            elif exp[index] != "(":
                add_num(dep, pre)
                dep.append(exp[index])
                index += 1
                pre = 0
            else:
                tmp = value(exp, index+1)
                pre = tmp[0]
                index = tmp[1] + 1
        add_num(dep, pre)
        return calculate(dep), index

    def add_num(dep, num):
        """
        通过向dep列表添加num,得到表达式各独立元素组成的列表(计算乘除法)
        :type dep:list
        :type num:int
        :param dep:
        :param num:
        :return:
        """
        if dep:
            top = dep.pop()
            if top in "-+":
                dep.append(top)
            else:
                cur = int(dep.pop())
                num = cur*num if top == "*" else cur/num
        dep.append(num)

    def calculate(dep):
        """
        遍历dep列表得到表达式各元素,计算该表达式最后结果
        :type dep:list
        :param dep:
        :return:
        """
        add = True
        res = 0
        while dep:
            cur = dep.pop(0)
            if cur == "+":
                add = True
            elif cur == "-":
                add = False
            else:
                cur = int(cur)
                res += cur if add else -cur
        return res

    if not expStr or expStr == "":
        return 0
    return value(expStr, 0)[0]


def sum_of_zero_left_one(num):
    """
    给定一个整数num,求出'0'和'1'字符组成的长度为num的所有字符串中,满足'0'字符的左边必须有'1'的字符串数量
    :type num:int
    :param num:
    :return:
    """
    if not num or num < 1:
        return 0
    if num == 1:
        return 1
    pre = 1
    cur = 2
    for i in range(2, num):
        tmp = cur
        cur += pre
        pre = tmp
    return cur


def newstr_index(value, index):
    """
    返回value中index位置的新类型字符
    :type value:str
    :type index:int
    :param value:
    :param index:
    :return:
    """
    if not value or value == "" or index < 0 or index >= len(value):
        return ""
    upNum = 0
    for i in range(index-1, 0, -1):
        if value[i].islower():
            break
        upNum += 1
    if upNum&1 == 1:
        return value[index-1: index+1]
    if value[index].isupper():
        return value[index: index+2]
    return value[index]

if __name__ == "__main__":
    pass
