'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashtable = {}
        for a in A:
            for b in B:
                if a+b in hashtable:
                    hashtable[a+b] += 1
                else:
                    hashtable[a+b] = 1
        
        # 上面的双重循环可以用collections.Counter()类执行，Counter()内可以是一个iterable队形，（list, tuple. dict, string等）
        # hashtable = collections.Counter(a+b for a in A for b in B)
        
        # 下面的双重循环可以用sum函数替代
        # sum(hashtable[-c-d] for c in C for d in D)
        count = 0
        for c in C:
            for d in D:
                if -c-d in hashtable:
                    count += hashtable[-c-d]
                    
        return count
                
        