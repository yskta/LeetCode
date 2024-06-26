#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #空のリスト用意
        k_numbers_min_heap = []
        # k番目までの要素を追加
        for i in range(k):
            k_numbers_min_heap.append(nums[i])
        # リストを最小ヒープに変換
        heapq.heapify(k_numbers_min_heap)
		# 'nums' 配列の残りの要素をループで処理
        for i in range(k, len(nums)):
             # 現在の要素を最小ヒープの最小要素（ルート）と比較
            if nums[i] > k_numbers_min_heap[0]:
                # 最小要素を削除
                heapq.heappop(k_numbers_min_heap)
                # 現在の要素を追加
                heapq.heappush(k_numbers_min_heap, nums[i])
        # ヒープのルートがk番目に大きい要素
        return k_numbers_min_heap[0]
# @lc code=end

