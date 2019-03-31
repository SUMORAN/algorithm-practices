#include "iostream"

/**
 * 《矩形覆盖》
 * 题目描述
 * 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
 * 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
*/

/**
 * 解题思路：
 * n=0时 0 种
 * n=1时 1 种
 * n=2时 2 种
 * n=3时 3 种
 * n=4时 5 种
 * n=5时 8 种
 * n=6时 13 种
 * 类似斐波那契数列
*/
class Solution {
public:
    int rectCover(int number) {
        int res[3] = {0,1,2};
        
        
        if(number<3){
            return res[number];
        }
        else{
            int preOne = 2;
            int preTwo = 1;
            int result = 2;
            for(int i=2;i<number;i++){
                result = preOne + preTwo;
                preTwo = preOne;
                preOne = result;
            }
            return result;
        }
    }
};