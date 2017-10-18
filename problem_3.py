#!/usr/bin/env python
# encoding: utf-8

"""
@author: ZalmanLee
@contact: zalman_lee@163.com
@file: problem_3.py
@time: 2017/10/18 下午6:06
"""


# # tle
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         arr = [0 for x in range(0, len(s))]
#         for idx in range(len(s)):
#             pool = set()
#             for p in range(idx, len(s)):
#                 if s[p] not in pool:
#                     arr[idx] += 1
#                     pool.add(s[p])
#                 else:
#                     break
#         print arr
#         max_len = 0
#         for x in arr:
#             if max_len < x:
#                 max_len = x
#         return max_len


# # tle
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         arr = [0 for x in range(0, len(s))]
#         count = 0
#         pool = set()
#         for idx in range(len(s)):
#             arr[idx] = count
#             for p in range(idx + count, len(s)):
#                 if s[p] not in pool:
#                     arr[idx] += 1
#                     pool.add(s[p])
#                     count += 1
#                 else:
#                     count -= 1
#                     pool.remove(s[idx])
#                     break
#         max_len = 0
#         for x in arr:
#             if max_len < x:
#                 max_len = x
#         return max_len


# # tle
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         max_len = 0
#         count = 0
#         pool = [0 for x in range(0, 256)]
#         for idx, val in enumerate(s):
#             tmp_max = count
#             for p in range(idx + count, len(s)):
#                 if pool[ord(s[p])] == 0:
#                     tmp_max += 1
#                     pool[ord(s[p])] = 1
#                     count += 1
#                 else:
#                     count -= 1
#                     pool[ord(val)] = 0
#                     break
#             if tmp_max > max_len:
#                 max_len = tmp_max
#         return max_len


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        count = 0
        pool = [0 for x in xrange(0, 256)]
        for idx, val in enumerate(s):
            tmp_max = count
            for p in xrange(idx + count, len(s)):
                if pool[ord(s[p])] == 0:
                    tmp_max += 1
                    pool[ord(s[p])] = 1
                    count += 1
                else:
                    count -= 1
                    pool[ord(val)] = 0
                    break
            if tmp_max > max_len:
                max_len = tmp_max
        return max_len
