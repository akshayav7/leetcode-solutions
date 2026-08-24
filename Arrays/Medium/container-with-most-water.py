class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxi = 0

        while l < r:
            cur_area = min(height[l], height[r]) * (r - l)
            maxi = max(maxi, cur_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxi
        