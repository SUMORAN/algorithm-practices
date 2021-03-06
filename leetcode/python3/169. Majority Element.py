'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # more than ⌊ n/2 ⌋ means at least  n/2 上限
        if not nums:
            return
        else:
            nums = sorted(nums)
            l = len(nums)
            if l & 1:
                return nums[l/2]
            else:
                return nums[l/2-1]