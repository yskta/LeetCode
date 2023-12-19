/*
 * @lc app=leetcode id=111 lang=cpp
 *
 * [111] Minimum Depth of Binary Tree
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
    int minDepth(TreeNode* root) {
       if (root == nullptr)
            return 0;
        
        // 左右のサブツリーの最小深さを取得
        int left_depth = minDepth(root->left);
        int right_depth = minDepth(root->right);
        
        // 特別なケースの処理
        if (left_depth == 0)
            return right_depth + 1;
        if (right_depth == 0)
            return left_depth + 1;
        
        // 左右のサブツリーの最小深さの小さい方に1を加える
        return std::min(left_depth, right_depth) + 1;
    }
};
// @lc code=end

