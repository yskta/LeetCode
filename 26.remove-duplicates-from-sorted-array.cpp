/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            if (it != nums.begin() && *it == *(it - 1)) {
                nums.erase(it);
                --it;
            }
        }
        return nums.size();
    }
};
// @lc code=end

