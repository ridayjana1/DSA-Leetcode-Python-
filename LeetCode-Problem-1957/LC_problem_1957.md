

````markdown
 Leetcode 1957 – Delete Characters to Make Fancy String

This repository contains a clean and beginner-friendly solution to Leetcode Problem #1957:  
**"Delete Characters to Make Fancy String"**

---

 Problem Summary

You're given a string `value`. Your task is to return a version of the string where **no character appears 3 or more times in a row.

 Example:

```text
Input:  "leeetcode"
Output: "leetcode"
````

The third `'e'` was removed because it made 3 in a row.

---

##  My Approach

### 🎯 Objective:

Avoid having any character repeat **three or more times** consecutively in the final string.

###  Strategy:

1. Use a variable `new_word` to build the result.
2. Use a `count` variable to keep track of consecutive repeating characters.
3. Loop through the input string:

   * If the current character is the same as the previous one → increment `count`.
   * Otherwise → reset `count` to `1`.
4. Only add the character to the result if `count < 3`.

---

##  Full Python Code

```python
value = "leeetcode"
new_word = ""
count = 1

for i in range(len(value)):
    if i > 0 and value[i] == value[i - 1]:
        count += 1
    else:
        count = 1

    if count < 3:
        new_word += value[i]

print(new_word)  # Output: "leetcode"
```

---

##  Step-by-Step Walkthrough

Let’s trace the input: `"leeetcode"`

| Index | Character | Previous | Count | Action | Result So Far |
| ----- | --------- | -------- | ----- | ------ | ------------- |
| 0     | `l`       | —        | 1     | Add    | `l`           |
| 1     | `e`       | `l`      | 1     | Add    | `le`          |
| 2     | `e`       | `e`      | 2     | Add    | `lee`         |
| 3     | `e`       | `e`      | 3     | Skip   | `lee`         |
| 4     | `t`       | `e`      | 1     | Add    | `leet`        |
| 5     | `c`       | `t`      | 1     | Add    | `leetc`       |
| 6     | `o`       | `c`      | 1     | Add    | `leetco`      |
| 7     | `d`       | `o`      | 1     | Add    | `leetcod`     |
| 8     | `e`       | `d`      | 1     | Add    | `leetcode`    |

✅ Final Output: `"leetcode"`

---

## ⏱ Time & Space Complexity

| Type             | Complexity |
| ---------------- | ---------- |
| Time Complexity  | `O(n)`     |
| Space Complexity | `O(n)`     |

* We iterate through the string once (`n` = length of string).
* We build a new string which, in the worst case, holds most of the original characters.

---

##  Key Learnings

* Using a **counter variable** lets us track repeating patterns efficiently.
* Avoiding premature `return` is important in loops — we let the full logic execute.
* This pattern is useful in many string manipulation tasks: **compressing**, **filtering**, or **cleaning data**.

---

##  Author

Made by **Riday Jana** as part of my daily coding journey.
Even small problems build strong fundamentals.
Feel free to fork, learn from, or contribute!

---
