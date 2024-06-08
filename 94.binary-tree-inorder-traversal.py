#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, order = [],[]
        curr = root
        while curr or len(stack) > 0:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                order.append(curr.val)
                curr = curr.right
        return order
# @lc code=end

