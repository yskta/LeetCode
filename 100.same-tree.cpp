/*
 * @lc app=leetcode id=100 lang=cpp
 *
 * [100] Same Tree
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        bool result = true;
        helper(p,q, result);
        return result;
    }

    void helper(TreeNode* p, TreeNode *q, bool& result){
        if (p != nullptr && q != nullptr){
            if (p->val != q->val)
                result = false;
            helper(p->left, q->left, result);
            helper(p->right, q->right, result);
        }
        else if (p == nullptr && q == nullptr)
            return ;
        else
            result = false;
    }
};
// @lc code=end

