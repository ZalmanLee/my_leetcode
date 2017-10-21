#!/usr/bin/env python
# encoding: utf-8

"""
@author: ZalmanLee
@contact: zalman_lee@163.com
@file: problem_1.py
@time: 2017/10/18 上午10:43
"""


# slow solution
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return None

# use sorted
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         _nums = sorted(zip(range(len(nums)), nums), key=lambda x: x[1])
#         p_s = 0
#         p_e = len(nums) - 1
#         while p_s < p_e:
#             if _nums[p_s][1] + _nums[p_e][1] == target:
#                 return [_nums[p_s][0], _nums[p_e][0]]
#             elif _nums[p_s][1] + _nums[p_e][1] < target:
#                 p_s += 1
#             else:
#                 p_e -= 1
#         return None



# fast solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for idx, val in enumerate(nums):
            if (target - val) in dic:
                return [dic[target - val], idx]
            dic[val] = idx
        return None
