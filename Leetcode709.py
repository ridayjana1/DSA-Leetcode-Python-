class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        window_sum = 0
        min_len = float("inf")


        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                curr_len = right - left + 1
                min_len = min(min_len, curr_len)
                window_sum -= nums[left] #---> Shrinking the left 
                left += 1 #---> after update move the left index + 1
        return 0 if min_len == float("inf") else min_len
