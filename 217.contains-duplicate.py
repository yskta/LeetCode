#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                return True
        return False
# @lc code=end

