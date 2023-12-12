/*
 * @lc app=leetcode id=58 lang=cpp
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution {
public:
    int lengthOfLastWord(string s) {
        int size = 0;
        int lastChrIndex = s.length() - 1;
        while (s[lastChrIndex] == ' ')
            lastChrIndex--;
        while (lastChrIndex >= 0 && s[lastChrIndex] != ' ')
        {
            lastChrIndex--;
            size++;
        }
        return size;
    }
};
// @lc code=end

