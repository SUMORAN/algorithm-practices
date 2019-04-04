# -*- coding:utf-8 -*-
'''
《最小的K个数》
题目描述
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''

'''
解题思路：
解法一：
排序后输出前K个数

解法二：
额外存储一个k个数字的容器，
如果n<K，那直接把全部n个数返回
如果n大于K，就先将前K个数放进容器中，记下其中最大值及其位置，
后续数字都跟这个最大值比较，小于这个最大值的话就替换之，否则不做处理
最后返回这个容器中的数
用什么来实现这个容器能方便地找到最大值呢？
大根堆？
红黑树？？？

'''
# 解法一
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        tinput = sorted(tinput)
        if k > len(tinput):
            return []
        if k < 1:
            return []
        return tinput[0:k]


# 解法二
# 下面代码还没写完，暂时写了的部分也有错
# 我去补大根堆和红黑树了的实现了。。。。。。。。。。TOT
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        if k < 1:
            return []
        if k == len(tinput):
            return tinput

        res = []
        tmp_k = 1
        Max = tinput[0]
        Max_index = 0
        for item in tinput:
            if tmp_k < k:
                res.append(item)
                tmp_k += 1
                # 记录容器中最大值及其位置
                if item > Max:
                    Max = item
                    Max_index = tmp_k-1
            else:
                if item < Max:
                    Max

            
            




print(Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],10))