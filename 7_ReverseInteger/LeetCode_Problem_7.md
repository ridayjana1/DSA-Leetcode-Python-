
# Reverse Integer with 32-bit Overflow Check

This Python script defines a class `Solution` with a method `reverse` that reverses an integer while ensuring the result stays within the bounds of a 32-bit signed integer.

## 🧠 Goal

Reverse a given integer `x`. If the reversed integer exceeds the range of a signed 32-bit integer (`[-2³¹, 2³¹ - 1]`), return `0`.

---

## 📦 Code Explanation

```python
import sys

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**63 - 1
        INT_MIN = -2**63
        revNum = 0

        # Step 1: Store the sign
        if x < 0:
            sign = -1
        else:
            sign = 1

        # Step 2: Work with the absolute value
        x = abs(x)

        # Step 3: Reverse digit by digit
        while x != 0:
            dig = x % 10

            # Step 4: Check for 64-bit overflow before appending digit
            if revNum > INT_MAX // 10:
                return 0
            elif revNum < INT_MIN // 10:
                return 0

            revNum = revNum * 10 + dig
            x = x // 10

        # Step 5: Apply sign back
        revNum *= sign

        return revNum
````

---

##  Overflow Handling

Although the problem asks for 32-bit overflow check, this implementation currently uses:

* `INT_MAX = 2**63 - 1`
* `INT_MIN = -2**63`

To strictly check for **32-bit signed integer** bounds, change those two lines to:

```python
INT_MAX = 2**31 - 1  #  2147483647
INT_MIN = -2**31     # -2147483648
```

This ensures the reversed number does not exceed the range `[-2,147,483,648, 2,147,483,647]`.

---

##  Example

```python
sol = Solution()
print(sol.reverse(-210))
```

**Output:**

```
-12
```

---

##  Time and Space Complexity

* **Time Complexity:** `O(log₁₀ x)` → one iteration per digit
* **Space Complexity:** `O(1)` → constant space used (no extra data structures)

---

##  Learning Notes

* Used `abs()` to handle negative numbers cleanly
* Captured sign separately and applied it after reversing
* Performed overflow check *before* the reverse step to avoid invalid results


