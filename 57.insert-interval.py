#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervalAdded = False
        ans = []
        if len(intervals) != 0 and newInterval[0] < intervals[0][0]:
            ans.append(newInterval)
            newIntervalAdded = True
        for i in range(len(intervals)):
            j = 0
            while j < len(ans):
                if (ans[j][0] > intervals[i][0]):
                    ans.insert(j, intervals[i])
                    break
                j+=1
            if j == len(ans):
                ans.append(intervals[i])
        if newIntervalAdded == False:
            j = 0
            while j < len(ans):
                if (ans[j][0] > newInterval[0]):
                    ans.insert(j, newInterval)
                    break
                j+=1
            if j == len(ans):
                ans.append(newInterval)
        i = 0
        print(ans)
        while i+1 != len(ans):
            if ans[i][1] >= ans[i+1][0]:
                ans[i][1] = max(ans[i][1], ans[i+1][1])
                ans.pop(i+1)
            else:
                i += 1
        return ans
# @lc code=end

