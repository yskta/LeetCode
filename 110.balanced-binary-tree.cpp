/*
 * @lc app=leetcode id=110 lang=cpp
 *
 * [110] Balanced Binary Tree
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
    bool isBalanced(TreeNode* root) {
        if (root == nullptr)
            return true;
        bool result = true;
        helper(root, result);
        return result;
    }

    void helper(TreeNode* root, bool& result){
        if (root == nullptr)
            return ;
        if (result == false)
            return ;
        helper(root->left, result);
        helper(root->right, result);
        if (result == false)
            return ;
        int leftHight = getHight(root->left);
        int rightHight = getHight(root->right);
        if (abs(leftHight - rightHight) >= 2){
            result = false;
        }
        return;
    }

    int getHight(TreeNode* root){
        int left_height;
        int right_height;
        int tree_height;

        if (root == nullptr)
            return 0;
        left_height = getHight(root->left);
        right_height = getHight(root->right);
        if (left_height > right_height) {
            tree_height = left_height;
        } else {
            tree_height = right_height;
        }
        return tree_height + 1;
    }
    
};
// @lc code=end

