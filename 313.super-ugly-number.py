#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
class Solution:
    @staticmethod
    def solve(n, primes):
        ugly = [1]
        cnt = {}
        for i in range(len(primes)):
            cnt[primes[i]] = 0
        for i in range(1, n+1):
            next_ugly = min(ugly[cnt[primes[i]]] * primes[i] for i in range(len(primes)))
            ugly.append(next_ugly)
            for i in range(len(primes)):
                if next_ugly == ugly[cnt[primes[i]]] * primes[i]:
                    cnt[primes[i]] += 1
        return ugly
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = Solution.solve(n, primes)
        return ugly[n-1]
# @lc code=end

