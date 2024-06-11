#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        cnt = 0
        for i in range(n + 1):
            if i == 0:
                ans.append(0)
            elif i == 1:
                ans.append(1)
            elif i & (i - 1) == 0:
                ans.append(1)
                cnt += 1
            else:
                j = i - 2 ** cnt
                ans.append(1 + ans[j])
        return ans
                
                
            
            
# @lc code=end

