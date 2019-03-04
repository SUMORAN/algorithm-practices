/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        int ans = 0;
        void dfs(node){
            if(node){
                if(node->val>=L&&node->val<=R){
                    ans+=node->val;
                }
                if(node->val>L){
                    dfs(node->left);
                }
                if(node->val<R){
                    dfs(node->right);
                }
            }
        }
        dfs(root);
        return ans;
    }
};