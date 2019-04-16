# -*- coding:utf-8 -*-
"""和为S的两个数字
    题目描述
    输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
    输出描述:
    对应每个测试案例，输出两个数，小的先输出。

    解题思路：
        左右两个指针，一起往中间凑。
        从右面的开始比较，大于S时向左挪，小于S时左指针向右挪
        当有多组值等于S时，比较乘积
    
"""
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) < 2:
            return []
        left = 0
        right = len(array)-1

        result = []

        while left < right:
            if array[left] + array[right] > tsum:
                right -= 1
            elif array[left] + array[right] < tsum:
                left += 1
            else:
                if result:
                    if array[right]*array[left] <  result[0]*result[1]:
                        result[0] = array[left]
                        result[1] = array[right] 
                else:
                    result.append(array[left])
                    result.append(array[right])
                left += 1
                right -= 1

        return result

def main():
    array = [1,2,4,7,11,15]
    S = 15
    print('start')
    res = Solution().FindNumbersWithSum(array, S)
    print(res)

if __name__=='__main__':
    main()
