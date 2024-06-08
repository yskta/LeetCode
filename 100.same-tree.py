#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, parent1: Optional[TreeNode], parent2: Optional[TreeNode]) -> bool:
        if parent1 is None and parent2 is None:
            return True
        if parent1 is None or parent2 is None:
            return False
        if parent1.val != parent2.val:
            return False
        return self.dfs(parent1.left, parent2.left) and self.dfs(parent1.right, parent2.right)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)
        
        
# @lc code=end

