#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        max_value = max(nums)
        for i in range(len(nums)):
            addFrag = False
            j = i
            if (nums[i] == max_value):
                ans.append(-1)
            else:
                for j in range(i, len(nums)):
                    if nums[j] > nums[i]:
                        ans.append(nums[j])
                        addFrag = True
                        break
                if j == len(nums) - 1 and addFrag == False:
                    for k in range(i):
                        if (nums[k] > nums[i]):
                            ans.append(nums[k])
                            break
        return ans
                
                
        
# @lc code=end

