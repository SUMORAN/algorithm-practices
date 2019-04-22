# -*- coding:utf-8 -*-
"""构建乘积数组
    题目描述
    给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
    
    解题思路：
    用另外两个数字分别保存从前到后乘和从后到前乘的结果
    空间复杂度3n
    时间复杂度2n
"""
class Solution:
    def multiply(self, A):
        if not A:
            return []
        C = [] # 前面部分的乘积，C[i]表思前i个数的乘积
        D = [] # 后面部分的乘积 , D[i]表示后i个数的乘积
        C.append(1)
        D.append(1)
        n = len(A)
        B = []
        for i in range(1, len(A)):
            C.append(C[i-1]*A[i])
            D.append(D[i-1]*A[n-i])
        
        B.append(D[n-1])
        for i in range(1, n):
            B.append(C[i-1]*D[n-i-1])
        return B


class Solution2:
    def multiply(self, A):
        # 先从前到后算一遍（求出来的每个B都只考虑了i之前的部分）
        # 再从后往前算一遍，与刚才的B相乘（这样就又把i之后的部分考虑了）
        if not A:
            return []
        n = len(A)
        B = []
        B.append(1)
        for i in range(1, len(A)):
            B.append(B[i-1]*A[i-1])
        tmp = 1

        for j in range(n):
            B[n-j-1] *= tmp
            tmp *= A[n-j-1]
        
        return B


def main():
    A = [1, 2, 3, 4, 5]
    res = Solution2().multiply(A)
    print(res)

if __name__=='__main__':
    main()
            