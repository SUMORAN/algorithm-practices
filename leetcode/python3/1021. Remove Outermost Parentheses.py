
"""A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string"""

class Solution:
    def removeOuterParentheses(self, S):
        decomposition = []
        left = 0
        right = -1
        flag = 0 # 还有没匹配到右括号的左括号数
        if not S:
            return ""
        for idx, item in enumerate(S):
            if item == "(":
                flag += 1
            elif item == ")":
                flag -= 1
            if flag == 0:
                left = right + 1
                right = idx
                if right == len(S)-1:
                    decomposition.append(S[left])
                else:
                    decomposition.append(S[left:right+1])
        res = []
        for i in decomposition:
            res.append(i[1:-1])
        
        res = ''.join(res)
        return res
