/**
 * Definition for a binary tree node. 
 * */
// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//  };

class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        
        // 判断新的节点值是否跟上一个节点值相等

        bool isUnival(TreeNode* root, int lastVal){
            if(root == NULL){ // 判断是否遍历完
                return true;
            }
            if(root->val!=lastVal){ // 如果不等就跳出得结果
                return false;
            }
            return isUnival(root->left,root->val) && isUnival(root->right,root->val);
        }

        if(root){
            return isUnival(root,root->val);
        }
        return true;
    }
};