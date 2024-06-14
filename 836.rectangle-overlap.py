#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        min_x_rec1 = min(rec1[0], rec1[2])
        max_x_rec1 = max(rec1[0], rec1[2])
        min_y_rec1 = min(rec1[1], rec1[3])
        max_y_rec1 = max(rec1[1], rec1[3])
        min_x_rec2 = min(rec2[0], rec2[2])
        max_x_rec2 = max(rec2[0], rec2[2])
        min_y_rec2 = min(rec2[1], rec2[3])
        max_y_rec2 = max(rec2[1], rec2[3])
        if max_x_rec1 <= min_x_rec2 or min_x_rec1 >= max_x_rec2 or max_y_rec1 <= min_y_rec2 or min_y_rec1 >= max_y_rec2:
            return False
        else:
            return True
            
             
        
# @lc code=end

