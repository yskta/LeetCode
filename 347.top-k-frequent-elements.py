#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        heap = [(-value, key) for key, value in counter.items()]
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            value, key = heapq.heappop(heap)
            ans.append(key)
        return ans
# @lc code=end

