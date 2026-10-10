class Solution:
    def minRotations(self, s: str) -> int:
        cur = 0
        ans = 0
        for i in s:
            n = int(i) 
            diff = abs(cur - n)
            ans += min( diff , 10 - diff)

            cur = n

        return ans