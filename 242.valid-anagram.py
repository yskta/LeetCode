#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        str_len = len(s)
        if str_len != len(t):
            return False
        for i in range(str_len):
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1
        return dict_s == dict_t
# @lc code=end

