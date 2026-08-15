class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in mpp:
                return [mpp[complement], i]
            mpp[num] = i