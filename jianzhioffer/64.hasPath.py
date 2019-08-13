# -*- coding:utf-8 -*-
"""矩阵中的路径
    题目描述
    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
    路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
    如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 
    例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
    但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
    路径不能再次进入该格子。

    解题思路：
    回溯
    
"""
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        self.flags = [[False for i in range(cols)] for j in range(rows)]
        
        m = [list(matrix[cols*i: cols*i+cols]) for i in range(rows)] # 由于给的是个字符串，这里按照给定的rows和cols将字符串变成矩阵
        
        for i in range(rows):
            for j in range(cols):
                if self.judge(m, i, j, rows, cols, 0, path):
                    return True
        return False
        
        
    def judge(self, matrix, i, j, rows, cols, k, path):
        if k >= len(path): # 如果k大于path字符串长度了，说明已经匹配最后一个字符了，说明存在
            return True
        if i > rows-1 or j > cols-1 or i < 0 or j < 0: # 说明往这个方向找行不通
            return False
        if not self.flags[i][j]:
            if matrix[i][j] == path[k]:
                self.flags[i][j] = True
                if self.judge(matrix, i+1, j, rows, cols, k+1, path) or self.judge(matrix, i-1, j, rows, cols, k+1, path) or self.judge(matrix, i, j+1, rows, cols, k+1, path) or self.judge(matrix, i, j-1, rows, cols, k+1, path):
                    return True
                else:
                    self.flags[i][j] = False
                    return False
        else:
            return False
        