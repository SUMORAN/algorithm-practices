

/*
《二维数组中的查找》
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
*/

/*
解题思路：
找每一行最大的不大于target的数，标记为anchor
先横着找，找到anchor，看这个数是否等于target，不等的话找它的下一行的数，也就是i+1，
如果下一个数大于target，顺着行往前找，思路同上；
如果找到最后一行都没找到，返回False
*/

#include <vector>
#include <iostream>
using namespace std;
using std::vector;

class Solution {
public:
    bool Find(int target, vector<vector<int>> array) {
        if(array.begin()==array.end()){
            return false;
        }

        int m = array.size(); //行数
        int n = array[0].size(); //列数

        int anchor = -2;  //anchor指向当前行最大的不大于target的位置
        for(int i=0; i < n; i++){
            if(array[0][i]==target){
                return true;
            }else if(array[0][i]>target){
                anchor = i-1;
                break;
            }
        }
        cout << "anchor:" << anchor;

        if(anchor==-1){ //如果第一个数就大于target，返回
            return false;
        }
        else if(anchor==-2){ //如果第一行一整行都不大于target，则anchor指向第一行最后一个
            anchor = n-1;
        }

        int j = 1;
        while(j<=m-1){
            while(array[j][anchor]>target){
                anchor -= 1;
                if(anchor<0){
                    return false;
                }
            }
            if(array[j][anchor] == target){
                return true;
            }
            else if(j==m-1){
                return false;
            }
            else{
                j += 1;
            }
        }
        return false;
    }
};