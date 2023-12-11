/*
 * @lc app=leetcode id=28 lang=cpp
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
class Solution {
public:
    int strStr(string haystack, string needle) {
        int resultIndex = -1;
        int i = 0;
        int j;
        while (i < haystack.size())
        {
            j = 0;
            if (haystack[i] == needle[j])//先頭文字が一致
            {
                resultIndex = i;
                while (j < needle.size())
                {
                    if (haystack[i] == needle[j])//一致している間インクリメント
                    {
                        i++;
                        j++;
                    }
                    else
                        break;
                }
                if (j == needle.size())
                    break;
                else{
                    i = resultIndex;
                    resultIndex = -1;
                }
            }
            i++;
        }
        return resultIndex;
    }
};
// @lc code=end

