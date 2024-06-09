#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.numArray = nums
        self.makeMemo()
    
    def makeMemo(self):
        self.memo = []
        if len(self.numArray) == 0 or len(self.numArray) == 1:
            return
        for i in range(len(self.numArray) - 1):
            if (i == 0):
                self.memo.append(self.numArray[0] + self.numArray[1])
            else:
                self.memo.append(self.memo[i-1] + self.numArray[i+1])
    def sumRange(self, left: int, right: int) -> int:
        if len(self.memo) == 0:
            if len(self.numArray) == 0:
                return None
            elif len(self.numArray) == 1 and left == 0 and right == 0:
                return self.numArray[0]
            else:
                return None
        elif left == right:
            return self.numArray[left]
        elif left == 0:
            return self.memo[right - 1]
        elif left == 1:
            return self.memo[right - 1] - self.numArray[0]
        else:
        	return (self.memo[right - 1] - self.memo[left - 2])
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

