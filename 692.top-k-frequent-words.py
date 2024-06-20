#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        for word in words:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
        heap = [(-value, key) for key, value in counter.items()]
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            value, key = heapq.heappop(heap)
            ans.append(key)
        return ans
        
        
# @lc code=end

