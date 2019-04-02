#include <iostream>
#include <deque>

/**
 * 《调整数组顺序使奇数位于偶数前面》
 * 题目描述：
 * 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
 * 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
 * 并保证奇数和奇数，偶数和偶数之间的相对位置不变。 
*/

/**
 * 解题思路：
 * 1、冒泡排序
 * 2、使用deque,双端队列（deque，全名double-ended queue）是一种具有队列和栈性质的抽象数据类型。 
 * 双端队列中的元素可以从两端弹出，插入和删除操作限定在队列的两邊进行。
 * 方法有pop(), popleft(), append(), appendleft()
 * #include <deque>
*/

class Solution {
public:
    void reOrderArray(vector<int> &array) {
        deque<int> result; 
        int length = array.size();
        for(int i=0; i < length; i++){
            if((array[length-i-1]&1) == 1){ //奇数
                result.push_front(array[length-i-1]);
            }
            if((array[i]&1) == 0){ //偶数
                result.push_back(array[i]);
            }            
        }
        // 因为此函数要求修改原数组而不是返回新数组，因此将原数组改掉
        for(int j = 0;j<length; j++){
            array[j] = result[j];
        }
    }
};
