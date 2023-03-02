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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>ret_vec;
        
        //find max depth
        int max_d = maxDepth(root);
        
        
        if(root == nullptr) {return ret_vec;}
        ret_vec.resize(max_d);
        ret_vec[0].push_back(root->val);
        
        levelHelper(root->left, ret_vec, 1);
        levelHelper(root->right, ret_vec, 1);
        return ret_vec;
    }
    void levelHelper(TreeNode* root, vector<vector<int>>& ret_vec, int level) {
        if(root == nullptr) {
            return;
        }
        //cout << root->val << "level: " << level << '\n';
        ret_vec[level].push_back(root->val);
        levelHelper(root->left, ret_vec, level + 1);
        levelHelper(root->right, ret_vec, level + 1);   
    }
    
    int maxDepth(TreeNode* root) {
        if(root == nullptr) {return 0;}
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};