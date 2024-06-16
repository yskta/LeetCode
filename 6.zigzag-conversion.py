#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strLen = len(s)
        lists = [[] for _ in range(numRows)]
        #3→x=4, 4→x=6,,,
        x = numRows * 2 - 2
        if (x == 0):
            return s
        for i in range(strLen):
            y = i % x
            if (y < numRows):
                lists[y].append(s[i])
            else:
                lists[x-y].append(s[i])
        res = ""
        for i in range(numRows):
            temp = ''.join(lists[i])
            res += temp
        return res
            
# @lc code=end

