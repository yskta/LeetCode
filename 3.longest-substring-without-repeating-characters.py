#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		# 文字列の長さを取得
		n = len(s)
		# 最長部分文字列の長さを格納する変数を初期化
		maxLength = 0
		# 現在の部分文字列に含まれる文字を格納するセットを初期化
		charSet = set()
		# 左側のポインタを初期化
		left = 0

		# 右側のポインタを文字列の始めから順に動かしていく
		for right in range(n):
			# もし右側のポインタが指す文字がセットに含まれていなければ
			if s[right] not in charSet:
				# その文字をセットに追加
				charSet.add(s[right])
				# 現在の部分文字列の長さを更新し、最長の長さを保持
				maxLength = max(maxLength, right - left + 1)
			else:
				# もし右側のポインタが指す文字がセットに含まれていれば
				# 左側のポインタを動かし、セットから文字を削除していく
				while s[right] in charSet:
					charSet.remove(s[left])
					left += 1
				# 右側のポインタが指す文字をセットに追加
				charSet.add(s[right])
		# 最長部分文字列の長さを返す
		return maxLength   
# @lc code=end

