# -*- coding:utf-8 -*-
"""滑动窗口的最大值
    题目描述
    给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
    例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 
    针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
    {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

    解题思路：
    对N个数字的数组，窗口大小为n，则共有N+1-n个滑动窗口。

"""
class Solution:
    def maxInWindows(self, num, size):
        if not num or not size:
            return []
        elif len(num) < size:
            return []
        else:
            left = 0
            right = size
            res = []
            while right < len(num)+1:
                tmp = max(num[left:right])
                res.append(tmp)
                left += 1
                right += 1
            return res
            
def main():
    num = [10,14,12,11]
    size = 4
    res = Solution().maxInWindows(num, size)
    print(res)

main()