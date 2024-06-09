#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def execute(self, root: Optional[TreeNode]): 
        if root is None:
            return
        if root.right is None:
            root.right = root.left
            root.left = None
        else:
            temp = root.right
            root.right = root.left
            root.left = temp
        self.execute(root.left)
        self.execute(root.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.execute(root)
        return root
        
# @lc code=end

