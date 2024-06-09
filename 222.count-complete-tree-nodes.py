#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #currdepth = 0
        if root is None:
            return 0
        elif root.right is None:
            return (1 + self.countNodes(root.left))
        else:
        	return (1 + self.countNodes(root.left) + self.countNodes(root.right)) 
        
        


            

# @lc code=end

