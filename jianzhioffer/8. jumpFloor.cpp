#include <iostream>

/**
 * 《跳台阶》
 * 题目描述
 * 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
*/

/**
 * 解题思路：
 * 假设有n级台阶，如果第一次跳1阶，就还剩n-1阶；如果第一次跳2阶，就还剩n-2阶。
 * 因此对于n阶来说，跳法f(n)=f(n-1)+f(n-2)
 * 也就是一个斐波那契数列
*/

class Solution {
public:
    int jumpFloor(int number) {
        int result[5] = {0, 1, 2};

        if(number<3){
            return result[number];
        }

        int preOne = 2;
        int preTwo = 1;
        int res = 0;

        int i = 2;
        while(i < number){
            res = preOne + preTwo;
            preTwo = preOne;
            preOne = res;
            i++;
        }
        return res;
    }
};