/*
 * @lc app=leetcode id=70 lang=cpp
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution {
public:
    int climbStairs(int n) {
        int way;
        if (n == 1)
            way = 1;
        else if (n == 2)
            way = 2;
        else {
            int way1 = 1;
            int way2 = 2;
            for (int i = 3; i <= n; i++) {
                way = way1 + way2;
                way1 = way2;
                way2 = way;
            }
        }
        return way;
    }
};
// @lc code=end

