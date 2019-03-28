/*
* 从尾到头打印链表
* 题目描述: 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
*/

/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
#include <iostream>
#include <vector>

class Solution {
    public:
        vector<int> printListFromTailToHead(ListNode* head) {
            vector<int> ArrayList;

            if(head==NULL){
                return ArrayList;
            }

            // while(head!=NULL){
            //     ArrayList.push_back(head->val);
            //     head = head->next;
            // }

            // vector<int> arraylist;
            // while(ArrayList.begin()!=ArrayList.end()){
            //     auto iter = ArrayList.end();
            //     --iter;
            //     arraylist.push_back(*iter);
            //     ArrayList.pop_back();
            // }
            // return arraylist;

            while(head!=NULL){
                ArrayList.insert(ArrayList.begin(), head->val);
                head = head->next;
            }

            return ArrayList;
        }
    };