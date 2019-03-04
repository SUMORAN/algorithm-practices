# -*- coding:utf-8 -*-
'''
用两个栈实现队列
题目描述: 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, node): # 入队列
        self.stack1.append(node) # 入队列直接入
    
    def pop(self): # 出队列
        # 当栈2不为空时，pop
        if self.stack2:
            return self.stack2.pop()

        elif not self.stack1: # 如果栈1为空，则无数据可弹出
            return None

        elif len(self.stack1) == 1: # 栈2为空栈1不为空且只有一个数据
            return self.stack1.pop()
            
        else: # 栈2为空栈1不为空且不只一个数据
            while self.stack1: # 将栈1中的数据依次转移到栈2中
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()






链接：https://www.nowcoder.com/questionTerminal/54275ddae22f475981afa2244dd448c6
来源：牛客网

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
         
    def push(self, node):
        # write code here
        self.stackA.append(node)
         
    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()