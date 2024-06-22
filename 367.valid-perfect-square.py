#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        if left == right:
            return True
        while left < right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                left = mid + 1
            else:
                right = mid
        return False
# @lc code=end

