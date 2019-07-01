'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
数据的全排列

# 这道题需要再思考一下
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 1、递归，把所有的排列都只当成两个数的排列
        # 2、不递归，3层循环嵌套
        
        # xrange() 函数用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器。
        res = [nums]
        for i in xrange(1, len(nums)):
            m = len(res)
            for k in xrange(m):
                for j in xrange(i):
                    res.append(res[k][:])
                    res[-1][j], res[-1][i] = res[-1][i], res[-1][j]
        return res
