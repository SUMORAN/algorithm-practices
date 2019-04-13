# -*- coding:utf-8 -*-
"""数组中只出现一次的数字
    题目描述
    一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

    解题思路：
    方法1：位运算
    任何一个数字异或自己都是0
    最后两个不一样的数字异或，得到的二进制结果中肯定有一位是1
    取第一个1所在的位置，对原数组进行遍历，将该位等于1的分为一组，该位等于0的分为一组
    然后分别对两组进行异或，异或之后的结果就是要求的数字，两个结果就是两个数

    方法二：哈希
    建一个字典，遍历一遍数组，保存数字出现的次数，数字出现次数等2了，就可以将其从字典中删去
    直到最后字典中剩下的两个key，就是要找到的两个数字
"""
# 方法一
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        tmp = 0
        for i in array:
            tmp = tmp^i
        
        #获取tmp中第一个1的位置(从低位向高位数)
        idx = 0
        while (tmp & 1) == 0:
            idx += 1
            tmp = tmp >> 1 # tmp右移一位（除以2）
        
        odd = []
        even = []
        for i in array:
            if self.isBit(i, idx):
                odd.append(i)
            else:
                even.append(i)
        num1 = 0
        num2 = 0

        for o in odd:
            num1 = num1^o
        for e in even:
            num2 = num2^e
        
        return [num1, num2]


    def isBit(self, num, idx):
        num = num >> idx  # num右移idx位，将第idx位变为最末一位  
        return num & 1 # 与1相与，末位是1时相与结果为1，末位是0时相与结果为0



# 方法二
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        dic = {}
        for i in array:
            if (i in dic.keys()):
                dic.pop(i)
            else:
                dic[i] = 1
        return list(dic.keys())

            