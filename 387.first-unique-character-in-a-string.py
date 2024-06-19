#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1
        unique_chars = [index for index, char in enumerate(s) if dict[char] == 1]
        if (unique_chars == []):
            return -1
        else:
            return min(unique_chars)
# @lc code=end

