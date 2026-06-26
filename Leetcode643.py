from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k


def main():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4

    sol = Solution()
    result = sol.findMaxAverage(nums, k)

    print("Maximum Average:", result)


if __name__ == "__main__":
    main()
