class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        count_0 = 0
        for i in range(len(nums)):
            # 对整个数组遍历，非0数字前面有几个0，就向左移动几位, 0被换到当前位置
            if nums[i] == 0:
                count_0 += 1
            else:
                nums[i-count_0], nums[i] = nums[i], nums[i-count_0]
        return nums