/*
 * @lc app=leetcode id=66 lang=cpp
 *
 * [66] Plus One
 */

// @lc code=start
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int index = digits.size() - 1;
        while (index >= 0)
        {
            if (digits[index] != 9){
                digits[index] += 1;
                break;
            }
            else if (index != 0 && digits[index] == 9){
                digits[index] = 0;
                index--;
            }
            else{
                digits[index] = 0;
                digits.insert(digits.begin(), 1); 
                break;
            }
        }
        return digits;
    }
};
// @lc code=end

