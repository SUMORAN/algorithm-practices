'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def DFS(l, r, path, res):
            if r < l or l == -1 or r == -1:
                return
            if l == 0 and r == 0:
                res.append(path[:])
            else:
                DFS(l-1, r, path+"(", res)
                DFS(l, r-1, path+")", res)
        
        DFS(n, n, "", res)
        return res

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def recursive(n, res):
            if not n:
                return []
            else:
                for i in recursive(n-1, res):
                    res.append("(" + i + ")")

        res = []
        recursive(n, res) 
        return res



