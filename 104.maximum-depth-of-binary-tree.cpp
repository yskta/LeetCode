/*
 * @lc app=leetcode id=104 lang=cpp
 *
 * [104] Maximum Depth of Binary Tree
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
    int maxDepth(TreeNode* root) {
        if (root == nullptr)
            return 0;
        int maxDepth = 1;
        int temporaryDepth = 1;
        helper(root, maxDepth, temporaryDepth);
        return maxDepth;
    }

    void helper(TreeNode* root, int& maxDepth, int& temporaryDepth){
        if (root->left == nullptr && root->right == nullptr){
            if (temporaryDepth > maxDepth)
                maxDepth = temporaryDepth;
            return ;
        }
        temporaryDepth++;
        if (root->left == nullptr){
            helper(root->right, maxDepth, temporaryDepth);
        }
        else if (root->right == nullptr){
            helper(root->left, maxDepth, temporaryDepth);
        }
        else {
            helper(root->left, maxDepth, temporaryDepth);
            helper(root->right, maxDepth, temporaryDepth);
        }
        temporaryDepth--;
    }
};
// @lc code=end

