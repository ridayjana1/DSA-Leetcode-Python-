#  2D Matrix Basics in Python

This repository contains simple Python code examples that demonstrate how to work with **2D matrices (nested lists)** — a foundational concept in programming, especially in problem-solving, competitive coding, and interviews like LeetCode.

##  What’s Inside

- How to loop through a 2D matrix using `for` loops.
- How to print every element in a matrix cleanly.
- How to search for a specific `key` in a matrix.
- Common beginner mistakes (and how to fix them), such as:
  - Returning too early from a loop
  - Indexing mistakes like `row[matrix]` or `cols[matrix[i]]`

## Why This Matters

Understanding 2D matrices is crucial because:
- They represent real-world grids (like games, maps, or spreadsheets).
- They're used in many **LeetCode / interview questions**, especially in companies like Google, Amazon, and Microsoft.
- They form the base for advanced topics like **dynamic programming**, **image processing**, and **machine learning**.

##  Example Covered

We wrote a function like this:

```python
class Solution:
    def twoArray(self, row, cols, key) -> int:
        matrix = [[1,2,3],[4,5,6],[7,8,9], [10,11,12]]
        for i in range(row):
            for j in range(cols):
                if matrix[i][j] == key:
                    print(i, j)
                    return 1
        return -1
