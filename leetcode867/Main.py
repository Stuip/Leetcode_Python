class Solution:
    def transpose(self, matrix):
        m, n = len(matrix), len(matrix[0])   # 行数  列数
        transposed = [[0] * m for _ in range(n)]  # 转置矩阵
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed


if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6]]
    result = s.transpose(matrix)
    print(result)