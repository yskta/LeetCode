#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        maxProfit = 0
        for price in prices:
            if min_price > price:
                 min_price = price
            if price - min_price > maxProfit:
                 maxProfit = price - min_price 
        return maxProfit
# @lc code=end

