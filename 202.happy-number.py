#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        dict = {}
        def cal_sum(num: int) -> int:
            sum = 0
            while num > 0:
                cal = num % 10
                sum += cal ** 2
                num = num // 10
            return sum
        dict[n] = cal_sum(n)
        curr = cal_sum(n)
        while 1:
            temp = curr
            curr = cal_sum(curr)
            if (curr == 1):
                return True
            elif curr not in dict:
                dict[temp] = curr
            else:
                return False                
                        
        
# @lc code=end

