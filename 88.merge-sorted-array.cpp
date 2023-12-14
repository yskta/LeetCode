/*
 * @lc app=leetcode id=88 lang=cpp
 *
 * [88] Merge Sorted Array
 */

// @lc code=start

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int insertIndex = 0;
        int j = 0;
        if (n == 0)
            return ;
        if (m == 0){
            for (int i = 0; i < n; i++){
                nums1[i] = nums2[i];
            }
            return ;
        }
        while (insertIndex < n + m && j < n)
        {
            if (nums1[insertIndex] > nums2[j]){
                nums1.insert(nums1.begin() + insertIndex, nums2[j]);
                nums1.erase(nums1.end() - 1);
                j++;
            }
            insertIndex++;
        }
        insertIndex = m + j;
        while (insertIndex < n + m && j < n)
        {
            nums1.insert(nums1.begin() + insertIndex, nums2[j]);
            nums1.erase(nums1.end() - 1);
            j++;
            insertIndex++;
        }
    }
};
// @lc code=end

