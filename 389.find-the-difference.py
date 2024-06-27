#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = len(s)
        dict_s = {}
        for i in range(n):
            if s[i] not in dict_s:
                dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1
        l = n + 1
        dict_t = {}
        for i in range(l):
            if t[i] not in dict_s:
                return t[i]
            elif t[i] not in dict_t:
                dict_t[t[i]] = 1
            else:
                dict_t[t[i]] += 1
        for i in range(l):
            if dict_t[t[i]] != dict_s[t[i]]:
                return t[i]
# @lc code=end

