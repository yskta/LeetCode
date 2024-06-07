#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        res = letters[0]
        for i in range(len(letters)):
            if (letters[i] <= target):
                continue
            else:
                res = letters[i]
                break
        return(res)
# @lc code=end

