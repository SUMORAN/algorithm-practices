# -*- coding:utf-8 -*-
"""扑克牌顺子
    题目描述
    LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
    他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
    “红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....
    LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
    上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 
    现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。
    为了方便起见,你可以认为大小王是0。

    解题思路：
    先给数组排序，看0的数量够不够填补空缺
    有对子的话就肯定不是顺子
"""
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        tmp = sorted(numbers)
        for i, item in enumerate(tmp):
            if item > 0:
                numOfZero = i
                small = i # 数组中最小的数的位置，0不算
                break
        large = small + 1 # 大一点的数的位置
        gap = 0
        
        while large < len(tmp) :
            gap += tmp[large] - tmp[small]-1
            if tmp[large] == tmp[small]:
                return False
            small += 1
            large += 1
            if gap > numOfZero:
                return False
        return True
        
            
res = Solution().IsContinuous([1,0,0,1,0])
print(res)
        
