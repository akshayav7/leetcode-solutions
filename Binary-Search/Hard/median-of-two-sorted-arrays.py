class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = nums1+nums2
        k.sort()
        n = len(k)
        if n%2 != 0:
            return float(k[n//2])
        else:
            m1 = k[n//2 -1]
            m2 = k[n//2 ]
            return (float(m1)+float(m2))/2.0
        