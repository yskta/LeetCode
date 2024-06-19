#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_split = list(pattern)
        split_s = s.split()
        if (len(pattern_split) != len(split_s)):
            return False
        dict = {}
        for i in range(len(split_s)):
            if pattern_split[i] not in dict and split_s[i] not in dict.values():
                dict[pattern_split[i]] = split_s[i]
            elif pattern_split[i] not in dict and split_s[i] in dict.values():
                return False
            elif pattern_split[i] in dict and dict[pattern_split[i]] != split_s[i]:
                return False
        return True
# @lc code=end

