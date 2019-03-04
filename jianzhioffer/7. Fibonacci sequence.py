# -*-coding:utf-8 -*-
'''
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''
# 此题用下面的递归不合理
# 因为递归会产生大量的重复运算，空间复杂度和时间复杂度都会太大
class Sulotion:
    def Fibonacci(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)
    
# 可以将计算结果保存，避免重复计算
class Sulotion:
    def Fibonacci(self, n):
        result = [0,1,1,2]
        #消除边界影响
        if n<0:
            return 0
        else:
            # 先根据n将整个数列计算出来并保存，免得重复计算
            while len(result)<=n:
                result.append(result[-1]+result[-2])
            return result[n]





t= Sulotion()
t.Fibonacci(30)