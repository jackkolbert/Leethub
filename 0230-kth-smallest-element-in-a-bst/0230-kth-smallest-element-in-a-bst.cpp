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
    int kthSmallest(TreeNode* root, int k) {
        // go as far left as possible
        // check the node off
        // check the parent off
        // check the right side off
        
        return helper(root, k);
        
    }
    
    int helper(TreeNode* root, int& k) {
        if(root == nullptr) {
            return -1;
        }
        else if(k == 0) {
            return root->val;
        }
        else{
            int a = helper(root->left, k);
            if(a != -1) {return a;}
            k--; // serves to check current node
            if(k == 0) {return root->val;}
            int b = helper(root->right, k);
            if(b != -1) {return b;}
            return -1;
        }
    }
};