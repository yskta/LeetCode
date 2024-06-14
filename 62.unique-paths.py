#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def cal_factorial(n: int) -> int:
            return math.factorial(n)
        ans = cal_factorial(m + n - 2) // (cal_factorial(m - 1) * cal_factorial(n - 1))
        return ans
# @lc code=end

