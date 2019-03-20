# -*- coding:utf-8 -*-
'''
《栈的压入、弹出序列》
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''

'''
解题思路：
按照popV的顺序push后pop，看能不能行得通
'''
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        n = 0
        for item in pushV:
            stack.append(item)
            # 对现在的栈按照popV出栈,一直符合一直出栈，不符合了就继续入栈
            while n < len(popV) and stack[-1] == popV[n]:
                stack.pop()
                n += 1

        # 到最后如果栈空了，说明popV是ok的    
        if len(stack):
            return False
        else:
            return True
