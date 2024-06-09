#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        # メモ化のためのテーブルを初期化
        self.table = [-1] * (n + 1)
        # 基本ケース：nが0の場合、1つの木（空の木）しかない
        self.table[0] = 1
        # 再帰的に計算を開始
        return self.numTreesRec(n)
    def numTreesRec(self, n: int) -> int:
        # 既に計算された値がある場合、それを返す
        if self.table[n] != -1:
            return self.table[n]
        
        total = 0
        # nをルートとする二分探索木の数を計算
        for m in range(n):
            # 左部分木の節点数: m
            # 右部分木の節点数: n-1-m
            total += self.numTreesRec(m) * self.numTreesRec(n - 1 - m)
        
        # 計算結果をテーブルに保存
        self.table[n] = total
        return total
# @lc code=end

