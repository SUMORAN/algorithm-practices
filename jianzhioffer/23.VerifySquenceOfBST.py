# -*- coding:utf-8 -*-
'''
《二叉搜索树的后序遍历序列》
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''

'''
解题思路：
后序遍历结果最后一个数字为根，前面的分为两段，前半段都小于根，后半段都大于根。
不符合上述规律就不是后序遍历
'''


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        
        def cantree(sequence):
            if not sequence or len(sequence)==1:
                return True
            root = sequence[-1]
            print('root:',root)
            left = []
            right = []
            subseq = sequence[0:-1]
            split = -1
            for i in range(0, len(subseq)):
                # 找到第一个比root大的数
                if subseq[i]>root:
                    split = i
                    print('split:',split)
                    break
                else:
                    continue
            if split == -1:
                left = subseq
            else:
                left = subseq[0:split]
                right = subseq[split:]
            # 看right中还有没有比root小的
            if not right:
                return cantree(left)
            else:
                for item in right:
                    if item<root:
                        print(item)
                        return False
                    else:
                        continue
                return cantree(left) and cantree(right)

        return cantree(sequence)

def main():
    lis = [4,6,7,5]
    print(Solution().VerifySquenceOfBST(lis))

if __name__=='__main__':
    main()