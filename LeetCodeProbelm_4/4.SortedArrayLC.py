from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1 + nums2)
        print(combined)
        addition = 0
        n = len(combined)
        if len(combined) % 2 == 0:
            median = (combined[n // 2] + combined[n // 2 - 1]) / 2
        elif len(combined) % 2 == 1:
            median = combined[len(combined)//2]
        median = round(median, 2)
        print(median)



sol = Solution()
print(sol.findMedianSortedArrays([9], [7,10]))