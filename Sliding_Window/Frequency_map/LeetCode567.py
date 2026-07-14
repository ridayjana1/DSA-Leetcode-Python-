from re import S


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Write your solution here
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
            
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1

        if s1_counts == s2_counts:
                return True
            
        for i in range(n1, n2):
            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i-n1]) - ord('a')] -= 1
            if s1_counts == s2_counts:
                return True
        return False     


            

            
        

        


            # while hashing[checking] < length_s1:
            #     left_hashing = s2[left]
            #     hashing[left_hashing] -= 1
            #     print(hashing[left_hashing])





def main():
    test_cases = [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("adc", "dcda", True),
        ("hello", "ooolleoooleh", False),
        ("a", "a", True),
        ("abc", "bbbca", True),
        ("xyz", "afdgzyxksldfm", True),
    ]

    sol = Solution()

    for s1, s2, expected in test_cases:
        result = sol.checkInclusion(s1, s2)

        print("-" * 45)
        print(f"s1              : {s1}")
        print(f"s2              : {s2}")
        print(f"Expected Output : {expected}")
        print(f"Your Output     : {result}")
        print("PASS" if result == expected else "FAIL")


if __name__ == "__main__":
    main()