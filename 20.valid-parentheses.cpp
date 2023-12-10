/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */

// @lc code=start
#include <stack>

class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;

        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                stk.push(c);
            } else {
                if (stk.empty()) {
                    return false;  // 開き括弧がないのに閉じ括弧が現れた場合
                }
                char openBracket = stk.top();// 一番上の要素を取り出す
                stk.pop();// 一番上の要素を削除する

                if ((c == ')' && openBracket != '(') ||
                    (c == ']' && openBracket != '[') ||
                    (c == '}' && openBracket != '{')) {
                    return false;  // 対応する開き括弧がない場合
                }
            }
        }
        return stk.empty();  // スタックが空であれば有効な括弧の組み合わせ
    }
};
// @lc code=end

