#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for i in range(len(nums)):
            if (nums[i] not in counter):
                 counter[nums[i]] = 1
            else:
                counter[nums[i]] += 1
		#countが1のkeyを返したい
        for key, value in counter.items():
        	if value == 1:
                    return key
# @lc code=end

