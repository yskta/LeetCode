/*
 * @lc app=leetcode id=119 lang=cpp
 *
 * [119] Pascal's Triangle II
 */

// @lc code=start
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result(rowIndex + 1, 1); // 事前確保と初期化
        if (rowIndex == 0) {
            return result;
        }
        for (int i = 1; i <= rowIndex; ++i) {
            result.push_back(1);
            for (int j = i - 1; j > 0; --j) {
                result[j] += result[j - 1];
            }
        }
        return result;
    }
};
// @lc code=end

