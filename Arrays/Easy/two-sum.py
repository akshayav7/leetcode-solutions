class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort()

        l, r = 0, len(arr) - 1

        while l < r:
            s = arr[l][0] + arr[r][0]

            if s == target:
                return [arr[l][1], arr[r][1]]
            elif s < target:
                l += 1
            else:
                r -= 1