/*
 * @lc app=leetcode id=101 lang=cpp
 *
 * [101] Symmetric Tree
 */

// @lc code=start
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
    bool isSymmetric(TreeNode* root) {
        bool result = true;
        helper(root->left, root->right, result);
        return (result);
    }

    void helper(TreeNode* rootLeft, TreeNode* rootRight, bool& result){
        if (rootLeft == nullptr && rootRight == nullptr)
            return ;
        else if (rootLeft == nullptr || rootRight == nullptr)
            result = false;
        else{
            if (rootLeft->val != rootRight->val){
                result = false;
                return ;
            }
            else{
                helper(rootLeft->left, rootRight->right, result);
                helper(rootLeft->right, rootRight->left, result);
            }
        }
    }
};
// @lc code=end

