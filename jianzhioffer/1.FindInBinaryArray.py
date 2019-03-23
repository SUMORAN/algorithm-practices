# -*- coding:utf-8 -*-
'''
《二维数组中的查找》
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
解题思路：
找每一行最大的不大于target的数，标记为anchor
先横着找，找到anchor，看这个数是否等于target，不等的话找它的下一行的数，也就是i+1，
如果下一个数大于target，顺着行往前找，思路同上；
如果找到最后一行都没找到，返回False
'''
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # array = [y for x in array for y in x]
        if not array:
            return False

        m = len(array) # 行数
        n = len(array[0]) # 列数
        anchor = -2 # anchor指向当前行最大的不大于target的位置
        for i in range(n):
            if array[0][i] == target:
                return True
            elif array[0][i] > target:
                anchor = i - 1
                break
        print('anchor:',anchor)

        if anchor == -1: # 如果第一个数就大于target，返回
            return False
        elif anchor == -2: # 如果第一行一整行都不大于target，则anchor指向第一行最后一个
            anchor = n-1
        
        j = 1
        print('1111111111111')
        while j <= m-1:
            print('1111111111111')
            while array[j][anchor]>target:
                anchor -= 1
                if anchor < 0:
                    return False
            print('222222222222')
            print('anchor:',anchor)
            if array[j][anchor] == target:
                return True
            elif j == m-1:
                return False
            else:
                j += 1

        return False

def main():
    array = [[1,2,8,9],[4,7,10,13]]
    target = 7
    return Solution().Find(target, array)

if __name__=='__main__':
    main()