/*
 * @lc app=leetcode id=69 lang=cpp
 *
 * [69] Sqrt(x)
 */

// @lc code=start
class Solution {
public:
    int mySqrt(int x) {
        int i = 0;
        if (x == 1)
            return (1);
        while (i < x / 2)
        {
            i++;
            if ((size_t)(i+1) * (i+1) > x)
                break;
        }
        return i;
    }
};
// @lc code=end

