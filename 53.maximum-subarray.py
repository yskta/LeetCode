#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    #O(n)で解決。メモリも少ない。
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                  max_global = max_current
        return max_global
                        
                    
            
        
# @lc code=end

