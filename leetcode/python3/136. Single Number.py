'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for item in nums:
            if item in dic.keys(): # 这个过程比较耗时
                dic.pop(item)
            else:
                dic[item] = 1
        return dic.keys()[0]
    # 上面的时间复杂度超出限制了

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]




        # or
        return reduce(lambda x, y : x^y, nums)