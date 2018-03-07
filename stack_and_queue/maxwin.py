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
@File:              maxwin.py
@Time:              17-12-1 上午8:05 
"""
"""
给一个长度n整数数组和一个大小为w的窗口，窗口从数组最左到最右，每次窗口向右滑动一个位置，求给定n-w+1的数组，该数组记录每一种窗口状态下的最大值
"""


def get_max_windows(ori_list, win_len):
    """
    给一个长度n整数数组和一个大小为w的窗口，窗口从数组最左到最右，每次窗口向右滑动一个位置，求给定n-w+1的数组，该数组记录每一种窗口状态下的最大值
    :type ori_list: list
    :param ori_list: 原始数组
    :param win_len: 窗口大小
    :return: 窗口状态下最大值数组
    """
    if ori_list is None or win_len < 1 or win_len > len(ori_list):
        return None
    max_array = []            # 辅助记录窗口状态下较大值由左到右降续
    win_array = []
    for i in range(len(ori_list)):
        if len(max_array) != 0 and max_array[-1] <= ori_list[i]:
            max_array.pop()
        max_array.append(i)
        if max_array[0] == i-win_len:
            max_array.remove(max_array[0])
        if i > win_len-1:
            win_array.append(ori_list[max_array[0]])
    return win_array
