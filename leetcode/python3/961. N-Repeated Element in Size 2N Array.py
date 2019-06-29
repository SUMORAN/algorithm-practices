'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5

'''

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        sorted(A)
        length = len(A)
        N = int(length/2)
        if A[0]==A[N]:
            return A[0]
        else:
            return A[N+1]


'''
Check if A[i] == A[i - 1] or A[i] == A[i - 2]
If so, we return A[i]
If not, it must be [x, x, y, z] or [x, y, z, x].
We return A[0] for the cases that we miss.
O(N) time O(1) space
'''
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(3, len(A)):
            if A[i]==A[i-1] or A[i]==A[i-2]:
                return A[i]
        return A[0]