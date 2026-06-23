from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = sum(arr[:k])
        avg_wind = window_sum / k
        count = 0

        if avg_wind >= threshold:
            count += 1

        for right in range(k, len(arr)):
            window_sum += arr[right]
            window_sum -= arr[right - k]
            avg_wind = window_sum / k

            if avg_wind >= threshold:
                count += 1

        return count

def main():
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4

    sol = Solution()
    result = sol.numOfSubarrays(arr, k, threshold)

    print("Answer:", result)

if __name__ == "__main__":
    main()
