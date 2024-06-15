#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
         #長さ取得
         length = len(nums)
         #配列を2倍にすることで、循環配列のように扱う
         nums.extend(nums)
         # スタックを初期化
         stack = deque()
         ans = []
         print(nums)
         #逆方向(右から左)に配列をループ
         for i in range(len(nums)-1,-1,-1):
             #stackのトップと現在の要素を比較し、現在の要素がスタックのトップより大きい場合、スタックをポップ
             while len(stack)>0 and stack[len(stack)-1]<=nums[i]:
                 stack.pop()
             # スタックが空の場合、次の大きい要素は存在しないので -1 を追加
             if len(stack)==0:
                 ans.append(-1)
             else:
                 #スタックのトップが次の大きい要素    
                 ans.append(stack[len(stack)-1])
             # 現在の要素をスタックに追加
             stack.append(nums[i])
         # 結果のリストを逆順にする
         ans = ans[::-1]
         #最初の配列の長さ分だけ結果を返す
         return ans[:length] 
# @lc code=end

