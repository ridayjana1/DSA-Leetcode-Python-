class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Write your solution here
        left = 0
        count = 0
        max_len = 0
        for right in range(len(s)):
            right_cost = abs(ord(s[right]) - ord(t[right]))
            count += right_cost
            while count > maxCost:
                left_cost = abs(ord(s[left]) - ord(t[left]))
                count -= left_cost
                left += 1
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
        return max_len



            



def main():
    test_cases = [
        ("abcd", "bcdf", 3, 3),
        ("abcd", "cdef", 3, 1),
        ("abcd", "acde", 0, 1),
        ("abcd", "abcd", 0, 4),
        ("krrgw", "zjxss", 19, 2),
        ("aaaa", "bbbb", 2, 2),
        ("xyz", "xyz", 0, 3),
    ]

    sol = Solution()

    for s, t, maxCost, expected in test_cases:
        result = sol.equalSubstring(s, t, maxCost)

        print("-" * 45)
        print(f"s               : {s}")
        print(f"t               : {t}")
        print(f"maxCost         : {maxCost}")
        print(f"Expected Output : {expected}")
        print(f"Your Output     : {result}")
        print("PASS" if result == expected else "FAIL")


if __name__ == "__main__":
    main()