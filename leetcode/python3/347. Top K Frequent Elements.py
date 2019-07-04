'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hs = {} # 数字-频率
        freq = {} # 频率-数字
        for i in xrange(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1
        
        for z, v in hs.iteritems():
            if v not in freq:
                freq[v] = [z]
            else:
                freq[v].append(z)
        
        arr = []

        # 把数字按出现频率次数大小存进arr
        for x in xrange(len(nums), 0, -1):
            if x in freq:
                for i in freq[x]:
                    arr.append(i)
        return arr[:k]