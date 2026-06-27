from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Write your solution here
        left = 0
        visited =  set(())
        count = 0
        answer = count

        
        for right in range(len(s)): 
            while s[right] in visited:
                visited.remove(s[left])
                left+=1
                count -= 0
            visited.add(s[right])
            count += 1
            answer = max(answer, count)
        return answer      
        


def main():
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("au", 2),
        ("dvdf", 3),
        ("abba", 2),
        ("tmmzuxt", 5),
        ("abcdef", 6),
        ("aaaaaa", 1),
    ]

    sol = Solution()

    for s, expected in test_cases:
        result = sol.lengthOfLongestSubstring(s)

        print("-" * 40)
        print(f"Input           : {s}")
        print(f"Expected Output : {expected}")
        print(f"Your Output     : {result}")
        print("PASS" if result == expected else "FAIL")


if __name__ == "__main__":
    main()