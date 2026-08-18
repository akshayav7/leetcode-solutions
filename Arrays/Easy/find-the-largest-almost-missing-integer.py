class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        mpp ={}
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] in mpp:
                mpp[nums[i]] += 1
            else:
                mpp[nums[i]] = 1
        
            
        if k == 1:
            for key in sorted(mpp.keys() , reverse = True):
                if mpp[key] == 1:
                    return key 
            return -1
        if k == n:
            return maxi
        
        ans = -1
        if mpp[nums[0]] == 1:
            ans = max(ans , nums[0])
        
        if mpp[nums[n-1]] == 1:
            ans = max(ans , nums[n-1])
        return ans
            




        