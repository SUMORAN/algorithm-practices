'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2): # len(nums)-2 is because we need at least 3 numbers to continue
            if i > 0 and nums[i] == nums[i-1]: 
                # 如果当前节点跟上一个节点一样了，那么，上一个节点没找到三元组，这个就也找不到，如果上一个找到了，这个再找会重复，所以直接跳过
                continue
            # 这里实际上三个点中，i指最左的点，l指中间的点，r指最右的点
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] +nums[l]+nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # 去重
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res