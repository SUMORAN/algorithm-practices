# -*- coding:utf-8 -*-
'''
《数组中的逆序对》
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5
'''

'''
归并？
把数组两个两个拆分，再拆分，拆成一个一个的
然后对这两两一对的一个一个的统计逆序对
然后把两个两个合起来，排个序，再比较前面的两个中较小的那个是不是大于后面的两个中较大的那个，如果是，这就是4个逆序对，
如果前面的较小的大于后面较小的但不大于后面较大的，是2个逆序对，
如果前面较小的不大于后面较小的但前面较大的大于后面较大的，是2个逆序对
如果前面较小的不大于后面较小的，但前面较大的大于后面较小的且不大于后面较大的，是1个逆序对
下面的代码是牛客网讨论区别人的
链接：https://www.nowcoder.com/questionTerminal/96bd6684e04a44eb80e6a68efc0ec6c5


代码需要修改！！！！！！
'''
count = 0
class Solution:
    def InversePairs(self, data):
        global count
        def MergeSort(lists):
            global count
            if len(lists) <= 1:
                return lists
            num = int(len(lists)/2)
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            r, l = 0, 0
            result = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left)-1
            result += right[r:]
            result += left[l:]
            return result
        
        MergeSort(data)
        return count%1000000007
