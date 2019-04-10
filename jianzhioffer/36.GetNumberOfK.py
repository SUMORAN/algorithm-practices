# -*- coding:utf-8 -*-
'''
《数字在排序数组中出现的次数》
题目描述
统计一个数字在排序数组中出现的次数。
'''

'''
解题思路：
二分查找
//因为data中都是整数，所以可以稍微变一下，不是搜索k的两个位置，而是搜索k-0.5和k+0.5
//这两个数应该插入的位置，然后相减即可。
来自牛客网讨论区drdr
'''
class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        
        start_low = 0
        start_high = len(data)-1
        end_low = 0
        end_high = len(data)-1
        start = 0
        end = 0
        while start_low <= start_low:
            mid = int((start_high + start_low) / 2)
            if k < data[mid]:
                start_high = mid - 1
            elif k > data[mid]:
                start_low = mid + 1
            else:  # k = data[mid]
                if data[mid-1] < k:
                    start = mid
                else:
                    start_high = mid - 1
        
        while end_low <= end_high:
            mid = int((end_high + end_low) / 2)
            if k < data[mid]:
                end_high = mid - 1
            elif k > data[mid]:
                end_low = mid + 1
            else:  # k = data[mid]
                if data[mid+1] > k:
                    end = mid
                else:
                    end_low = mid + 1

        if start!=0 and end != 0:
            return end+1-start
        else:
            return 0


class Solution:
    def biSearch(self, data, num):
        low = 0
        high = len(data)-1
        while low <= high:
            mid = int((high + low) / 2)
            if num < data[mid]:
                high = mid - 1
            elif num > data[mid]:
                low = mid + 1
        return low

    def GetNumberOfK(self, data, k):
        return self.biSearch(data, k+0.5)-self.biSearch(data, k-0.5)