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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
                

        return helper_1(root, subRoot);
        
    }
    bool helper_1(TreeNode* root, TreeNode* subRoot) {
        if(root == nullptr && subRoot == nullptr) {
            return true;
        }
        else if(root != nullptr && subRoot == nullptr) {
            return false;
        }
        else if(root == nullptr && subRoot != nullptr) {
            return false;
        }
        if(root->val == subRoot->val) {
            bool temp = isSame(root->left, subRoot->left) 
                        && isSame(root->right, subRoot->right); 
            if (temp) {
                return temp;
            }
        }
        return helper_1(root->left, subRoot) || helper_1(root->right, subRoot);    
    }
    
    bool isSame(TreeNode* root, TreeNode* subRoot) {
        
        if(root == nullptr && subRoot == nullptr) {
            return true;
        }
        else if(root != nullptr && subRoot == nullptr) {
            return false;
        }
        else if(root == nullptr && subRoot != nullptr) {
            return false;
        }
        else if(subRoot->val == root->val) {
            return isSame(root->left, subRoot->left) 
                && isSame(root->right, subRoot->right);
        }
        return false;
    }
};