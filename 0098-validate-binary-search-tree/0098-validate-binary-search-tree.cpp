/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return helper(root->left, LONG_MIN, root->val) && 
                    helper(root->right, root->val, LONG_MAX); 
    }
    
    bool helper(TreeNode *root, long lower, long upper) {
        if(root == nullptr) {
            return true;
        }
        else {

            
            if(root->val < upper && root->val > lower) {
                
                return helper(root->left, lower, root->val) 
                    && helper(root->right, root->val ,upper);
            }
            else {
                return false;
            }
        }
    }
};