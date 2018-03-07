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
@File:              conversion.py 
@Time:              18-1-21 下午9:38 
"""
"""
a.给定一个字符串str1,如果str1符合日常书写的整数规则,返回str1能代表的整数值,否则返回0
b.给定一个字符串str1,如果可以在str1的任意位置添加字符,请返回在添加字符最少情况下,让str1整体都是回文字符串的一种结果
    思路：
        1.首先通过动态规划获得最少添加几个字符可以使str1成为回文字符串,dp[i][j]代表字串str1[i...j]最少添加几个字符可以使str1[i...j]成为回文
            1)如果str1[i..j]只有一个字符,则dp[i][j]=0
            2)如果str1[i...j]只有两个字符,且相等,则dp[i][j]=0,如果不相等,则dp[i][j]=1
            3)如果str1[i...j]大于两个字符,且str1[i]==str1[j],则dp[i][j]=dp[i+1][j-1],如果str1[i]!=str1[j],则将str1[i...j]变成回文
              有两种方法,首先将str1[i...j-1]变成回文,而后在str1[i...j]前面插入str1[j],第二种即先将str1[i+1...j]变成回文,而后在str1[i...j]
              末尾插入str1[i],取两种跟小值,dp[i][j]=min(dp[i][j-1], dp[i+1][j])+1
        2.通过1获得动态规划表,即可得到最少添加几个字符便可使str1变成回文,即dp[0][-1],则需要返回的字符长度为dp[0][-1]+str1长度
        3.res为列表,长度为dp[0][-1]+str1长度,所有位置置为None,根据dp,str1填充res
            1)如果str1[i]==str1[j],则str1[i...j]会变成str1[i]+str1[i+1...j-1]回文+str1[j]
            2)如果str1[i]!=str1[j],则判断dp[i][j-1]和dp[i+1][j]哪个更小,如果dp[i][j-1]更小,则返回str1[j]+str1[i...j-1]回文+str1[j],
              否则返回str1[i]+str1[i+1...j]回文+str1[i]
        
c.在b的基础上,在给定str1的最长回文子序列str1lps,请返回在添加字符最少的情况下,让str1整体都是回文字符串的一种结果
    思路：
        1.str1长度为N,str1lps长度为M,则可知回文字符串长度为2×N-M
        2.类似剥洋葱方法,第0层为str1lps[0]和str1lps[M-1]组成,从str1左侧开始找第一个字符为str1lps[0],最左侧到这个字符记为leftPart,从str1右侧开始找
          第一个str1lps[M-1],最右侧到这个字符记为rightPart,则洋葱第0层左侧为leftPart+rightPart+str1lps[0],洋葱第0层右侧为str1lps[M-1]+rightPart+leftPart
        3.依次,直到str1lps查找完毕
d.给定字符串str1,判断是不是整体有效的括号字符串
    思路：
        1.由左至右遍历,判断每一个字符是否是'('或')',如果不是,直接False
        2.统计'('数量,记为counts,如果字符是')',则counts-1,判断最终counts是否是0
e.给定一个字符串str1,返回最长的有效括号字符
    思路：
        1.需要使用动态规划方法,动态规划表dp[i]表示str1[0...i]字符串中以str1[i]结尾的最长有效子串长度
        2.dp[0]=0,由左至右遍历str1[1...-1],根据不同情况赋值dp[i]
            a)str1[i]=='(',有效字符串必须以')'结尾,故此dp[i]=0
            b)str1[i]==')',则str1[i]结尾的最长有效子串可能存在,dp[i-1]表示str1[i-1]结尾的最长有效括号子串长度,pre记为i-dp[i-1]-1,如果str1上pre(>=0)位置为'(',
              则恰好可以配出一对有效括号,dp[i]=dp[i-1]+2+(dp[pre-1] if pre else 0)
              
"""


def convert_integer(str1):
    """
    将字符串转换为能表达的整数值
    :type str1:str
    :param str1:
    :return:
    """

    def is_valid(str1):
        """
        判断str1是否符合整数书写规范
        :type str1:str
        :param str1:
        :return:
        """
        if str1[0] not in "-0123456789":
            return False
        if str1[0] == "-" and (len(str1)==1 or str1[1]==0):
            return False
        if str1[0] == "0" and len(str1) > 1:
            return False
        for i in str1[1:]:
            if i not in "0123456789":
                return False
        return True

    if not str1 or str1 == "":
        return 0
    if not is_valid(str1):
        return 0
    isMinus = True if str1[0] == "-" else False
    result = 0
    for cur in str1[1 if isMinus else 0:]:
        cur = int(cur)
        result = result*10 + cur
    return -result if isMinus else result


def get_palindrome(str1):
    """
    通过在任意位置插入最少字符使得str1成为回文,返回该回文
    :type str1:str
    :param str1:
    :return:
    """

    def get_dp(str1):
        """
        通过动态规划表得到最少插入多少字符可以使str1成为回文
        :type str1:str
        :param str1:
        :return:
        """
        dp = [[0 for i in range(len(str1))] for j in range(len(str1))]
        for j in range(1, len(str1)):
            dp[j-1][j] = 0 if str1[j-1] == str1[j] else 1
            for i in range(j-2, 0, -1):
                if str1[i] == str1[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp

    if not str1 or len(str1) < 2:
        return str1
    dp = get_dp(str1)
    res = ["" for i in range(len(str1)+dp[0][-1])]
    # i,j分别标记str1左右位置
    i = 0
    j = len(str1) - 1
    # resLeft,resRight分表标记res列表的左右位置
    resLeft = 0
    resRight = len(res) - 1
    while i <= j:
        if str1[i] == str1[j]:
            res[resLeft] = str1[i]
            res[resRight] = str1[j]
            resLeft += 1
            resRight -= 1
            i += 1
            j -= 1
        elif dp[i][j-1] < dp[i+1][j]:
            res[resLeft] = str1[j]
            res[resRight] = str1[j]
            resLeft += 1
            resRight -= 1
            j -= 1
        else:
            res[resLeft] = str1[i]
            res[resRight] = str1[i]
            resLeft += 1
            resRight -= 1
            i += 1
    return "".join(res)


def get_palindrome_by_substr(str1, str1lps):
    """
    通过在任意位置插入最少字符使得str1成为回文,返回该回文
    :type str1:str
    :type str1lps:str
    :param str1:
    :param str1lps:
    :return:
    """

    def set_result(res, resLeft, resRight, str1, leftStart, leftEnd, rightStart, rightEnd):
        """
        设置result
        :type res:list
        :type resLeft:int
        :type resRight:int
        :type str1:str
        :type leftStart:int
        :type leftEnd:int
        :type rightStart:int
        :type rightEnd:int
        :param res:
        :param resLeft:
        :param resRight:
        :param str1:
        :param leftStart:
        :param leftEnd:
        :param rightStart:
        :param rightEnd:
        :return:
        """
        for i in range(leftStart, leftEnd+1):
            res[resLeft] = str1[i]
            res[resRight] = str1[i]
            resLeft += 1
            resRight -= 1
        for i in range(rightEnd, rightStart-1, -1):
            res[resLeft] = str1[i]
            res[resRight] = str1[i]
            resLeft += 1
            resRight -= 1

    if not str1 or str1 == "" or not str1lps or str1lps == "":
        return ""
    res = ["" for i in range(len(str1) + len(str1lps))]
    str1Left = 0
    str1Right = len(str1) - 1
    lpsLeft = 0
    lpsRight = len(str1lps) - 1
    resLeft = 0
    resRight = len(res) - 1
    while lpsLeft <= lpsRight:
        tmpLeft = str1Left
        tmpRight = str1Right
        while str1[str1Left] != str1lps[resLeft]:
            str1Left += 1
        while str1[str1Right] != str1lps[resRight]:
            str1Right -= 1
        set_result(res, resLeft, resRight, str1, tmpLeft, str1Left, tmpRight, str1Right)
        resLeft += str1Left - tmpLeft + tmpRight - str1Right
        resRight -= str1Left - tmpLeft + tmpRight - str1Right
        res[resLeft] = str1[str1Left]
        res[resRight] = str1[str1Right]
        resLeft += 1
        str1Left += 1
        resRight -= 1
        str1Right -= 1
        lpsLeft += 1
        lpsRight -= 1
    return "".join(res)


def is_effective_bracket(str1):
    """
    判断括号是否有效
    :type str1:str
    :param str1:
    :return:
    """
    if not str1 or str1 == "":
        return False
    counts = 0
    for i in range(len(str1)):
        if str1[i] not in "()":
            return False
        if str1[i] == "(" and counts >= 0:
            counts += 1
        if str1[i] == ")" and counts >= 0:
            counts -= 1
    return counts == 0


def max_length_effective_bracket(str1):
    """
    最长有效括号子串
    :type str1:str
    :param str1:
    :return:
    """
    if not is_effective_bracket(str1):
        return 0
    dp = [0 for i in range(len(str1))]
    res = 0
    for i in range(1, len(str1)):
        if str1[i] == ")":
            pre = i - dp[i-1] - 1
            if pre>=0 and str1[pre] == "(":
                dp[i] = dp[i-1] + 2 + (dp[pre-1] if pre else 0)
        res = max(dp[i], res)
    return res


if __name__ == "__main__":
    pass
