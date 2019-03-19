# -*- coding:utf-8 -*-
'''
《顺时针打印矩阵》
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 
1 2 3 4 
5 6 7 8 
9 10 11 12 
13 14 15 16 
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

'''
解题思路：
1、方法一：外圈绕一圈之后，剩下的内部又是一个小一圈的matrix
2、方法二：逆时针旋转魔方，每次输出最上面一行
'''


class Solution:
    # matrix类型为二维列表，需要返回列表
    # 下面这个方法调试没问题，但再相同的测试用例上牛客网执行错误
    def printMatrix(self, matrix):
        if not matrix:
            return
        m = len(matrix) # 行数
        n = len(matrix[0]) # 列数
        res = []
        if m==1 and n==1:
            print(matrix[0][0])
            res.append(matrix[0][0])
        
        for j in range(n-1): # 上面, 0~n-2
            print(matrix[0][j])
            res.append(matrix[0][j])
    
        for i in range(m-1): # 右面, 0~m-2
            print(matrix[i][n-1])
            res.append(matrix[i][n-1])
                  
        for j in range(n-1, 0, -1): # 下面, n-1 ~ 1
            print(matrix[m-1][j])
            res.append(matrix[m-1][j])
        
        for i in range(m-1, 0 ,-1): #左面, m-1 ~ 1
            print(matrix[i][0])
            res.append(matrix[i][0])
        if m < 3 or n < 3:
            return res
        else:
            # new_matrix = [[0 for i in range(n-2)] for j in range(m-2)]
            new_matrix = []
            for i in range(1, m-1):
                new = []
                for j in range(1, n-1):
                    # new_matrix[i-1][j-1] = matrix[i][j]
                    new.append(matrix[i][j])
                new_matrix.append(new)
            res.extend(self.printMatrix(new_matrix))
        

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        while len(matrix)>0:
            res.extend(matrix[0])
            matrix = zip(*matrix[1:])[::-1] # 旋转
        return res
        


def main():
    matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    Solution().printMatrix(matrix)


if __name__=='__main__':
    main()