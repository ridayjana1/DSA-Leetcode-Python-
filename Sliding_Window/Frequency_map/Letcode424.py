class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Write your solution here
        left = 0
        freq = {}
        
        for ch in range(len(s)):
            freq[ch] = s[ch]
            print(freq[ch])
            while freq[ch] >= k:
                pass
            


def main():
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
        ("ABCDE", 1, 2),
        ("BAAA", 0, 3),
        ("ABBB", 2, 4),
        ("AABA", 0, 2),
        ("ABCABC", 2, 4),
    ]

    sol = Solution()

    for s, k, expected in test_cases:
        result = sol.characterReplacement(s, k)

        print("-" * 40)
        print(f"s               : {s}")
        print(f"k               : {k}")
        print(f"Expected Output : {expected}")
        print(f"Your Output     : {result}")
        print("PASS" if result == expected else "FAIL")


if __name__ == "__main__":
    main()