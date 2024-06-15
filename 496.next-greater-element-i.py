#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dict = {}
        for j in range(len(nums2)):
            dict[nums2[j]] = j
        for i in range(len(nums1)):
            startIndex = dict[nums1[i]]
            for j in range(startIndex,len(nums2)):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    break
                if j == len(nums2) - 1:
                    ans.append(-1)
        return ans
# @lc code=end

