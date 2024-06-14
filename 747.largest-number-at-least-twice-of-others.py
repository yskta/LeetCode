#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = 0
        max_value = nums[0]
        for i in range(len(nums)):
            if max_value < nums[i]:
                max_value = nums[i]
                max_index = i
        for i in range(len(nums)):
            if (i == max_index):
                continue
            else:
                if max_value // 2 < nums[i]:
                    return -1
        return max_index
        
        
# @lc code=end

