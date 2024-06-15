#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
       
        res = []     
        startnode = None
        prev = None
        lastnode = None
        
        def dfs(root):
            #nonlocal は、Pythonにおける変数スコープを扱うためのキーワードの一つです。
			#具体的には、内側の関数から外側の関数（つまり、ネストされた関数の一つ外側のスコープ）にある変数を参照したり変更したりする際に使用
            nonlocal res, startnode, prev, lastnode
            if not root:
                return
            # 左部分木へ進む（中間順走査のステップ1）
            dfs(root.left)
            # 処理を行う（中間順走査のステップ2）
			# ソート順が崩れている最初と最後のノードを見つける
            if prev and prev.val > root.val:
                if not startnode:
                    startnode = prev
                lastnode = root
            
			# 現在のノードを前のノードとして更新
            prev = root
			
			# 右部分木へ進む（中間順走査のステップ3）
            dfs(root.right)
            
        
        dfs(root)
        # swap the nodes that are not in place
        if startnode and lastnode:
            startnode.val, lastnode.val = lastnode.val, startnode.val
        
# @lc code=end

