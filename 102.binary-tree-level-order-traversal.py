#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
from collections import deque
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        List = []
        def BFS (root: Optional[TreeNode]):
            nonlocal List, queue
            if (root is None):
                return
            else:
                List.append([root.val])
            if root.left is None and root.right is None:
                return
            else:
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
            curr = root
            while len(queue) > 0:
                addList = []
                n = len(queue)
                for i in range(n):
                    curr = queue.popleft()
                    addList.append(curr.val)
                    if curr.left is None and curr.right is None:
                        continue
                    if curr.left is not None:
                        queue.append(curr.left)
                    if curr.right is not None:
                        queue.append(curr.right)
                List.append(addList)
        BFS(root)
        return List
# @lc code=end

