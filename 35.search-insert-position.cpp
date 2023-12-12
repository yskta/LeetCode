/*
 * @lc app=leetcode id=35 lang=cpp
 *
 * [35] Search Insert Position
 */

// @lc code=start
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int taragetIndex;
        if (nums.size() == 0)
            return 0;
        if (target < nums[0])
            return 0;
        if (target > nums[nums.size() - 1])
            return nums.size();
        if (target - nums[0] < nums[nums.size() - 1] - target)
        {
            for (int i = 0; i < nums.size(); i++)
            {
                if (nums[i] == target)
                    return i;
                if (nums[i] > target)
                    return i;
            }
        }
        else
        {
            for (int i = nums.size() - 1; i >= 0; i--)
            {
                if (nums[i] == target)
                    return i;
                if (nums[i] < target)
                    return i + 1;
            }
        }
        return taragetIndex;
    }
};
// @lc code=end

