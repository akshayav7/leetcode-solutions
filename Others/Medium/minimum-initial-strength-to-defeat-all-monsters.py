class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)

        diff = [0] * (n + 1)
        for l, r, v in boosts:
            diff[l] += v
            if r + 1 < n:
                diff[r + 1] -= v

        bonus = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            bonus[i] = cur

            
        ans = 0
        prefix = 0
        for i in range(n):
            if bonus[i] < monsters[i]:
                ans = max(ans, prefix + monsters[i] - bonus[i])
            prefix += monsters[i]

        return ans
        