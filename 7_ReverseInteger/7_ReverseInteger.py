import sys
class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**63 - 1
        INT_MIN = -2**63
        revNum = 0
        if x < 0:
            sign = -1
        else:
            sign = 1
        x =abs(x)
        while x != 0:
            dig = x % 10
            if revNum > INT_MAX//10:
                return 0
            elif revNum < INT_MIN//10:
                return 0
            revNum = revNum * 10 + dig
            x = x//10
        revNum *= sign
        return revNum



sol = Solution()
print(sol.reverse(-210))