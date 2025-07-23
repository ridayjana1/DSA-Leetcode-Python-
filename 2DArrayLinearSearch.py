#2D matrix

class Solution:
    def twoArray(self, row, cols, key) -> int:
        matrix = [[1,2,3],[4,5,6],[7,8,9], [10,11,12]]
        for i in range(row):
            for j in range(cols):
                if matrix[i][j] == key:
                    return (i, j)
        return -1




sol = Solution()
print(sol.twoArray(4,3,11))

