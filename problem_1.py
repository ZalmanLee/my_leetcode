#!/usr/bin/env python
# encoding: utf-8

"""
@author: ZalmanLee
@contact: zalman_lee@163.com
@file: problem_1.py
@time: 2017/10/18 上午10:43
"""


# slow solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
