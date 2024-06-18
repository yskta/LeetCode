#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        for i in range(n):
            for j in range(0, n-i-1):
                if intervals[j][0] > intervals[j+1][0]:
                    intervals[j],intervals[j+1] = intervals[j+1], intervals[j]
        i = 0
        while i + 1 != len(intervals):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i += 1
        return intervals

# @lc code=end

