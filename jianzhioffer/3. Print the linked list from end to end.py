# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
从尾到头打印链表
题目描述: 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
'''
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        ArrayList = []
        
        if listNode is None:
            return ArrayList
        
        while listNode:
            ArrayList.append(listNode.val)
            listNode = listNode.next
        
        arrayList = ArrayList[::-1]
        # arrayList = list(reversed(ArrayList))
        return arrayList

# 插入排序
def insert_sort(ilist):
    for i in range(len(ilist)):
        for j in range(i): # 已排序部分
            if ilist[j] > ilist[i]:
                ilist.insert(j,ilist.pop(i)) # 将ilist[i]弹出，并将数值插入j的位置
                break
    return ilist

ilist = insert_sort([2,4,1,5,2,7,8])
print ilist