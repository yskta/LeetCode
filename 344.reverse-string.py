#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        cnt = n // 2
        for i in range(cnt):
            temp = s[i]
            s[i] = s[n-1-i]
            s[n-1-i] = temp
        
# @lc code=end

