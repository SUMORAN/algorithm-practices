'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        print(n)
        if n < 2:
            return nums
        res = [1]
        # 从左到右只考虑当前数字左边的积
        for i in range(1, n):
            res.append((res[i-1]) * nums[i-1])
        
        # 从右到左考虑当前数字右边的积
        right = 1
        for j in range(n-1,-1,-1):
            res[j] *= right
            right *= nums[j]
        return res

if __name__=='__main__':
    nums = [1,2,3,4]
    res = Solution().productExceptSelf(nums)
    print(res)

