#!/usr/bin/env python
# encoding: utf-8

"""
@author: li.zheshen
@contact: lizheshen@ucfgroup.com
@file: problem_test.py
@time: 2017/10/21 上午11:22
"""


def del_char_from_str(s):
    """
    输入转移字符含'\b'的字符串
    输出删除转移字符'\b'和它前面的字符，如果遇到多个连续的'\b'则删除相同数量的转移字符前面的字符
    :param s:
    :return:
    """
    del_char = '\b'
    lst = list()
    for item in s:
        if item != del_char:
            lst.append(item)
        else:
            if lst:
                lst.pop()
            else:
                raise RuntimeError("no item in lst")
    return "".join(lst)


def main():
    print del_char_from_str("abc\b\bd\b\bghi")


if __name__ == '__main__':
    main()
