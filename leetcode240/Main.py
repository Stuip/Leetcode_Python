class Solution:
    def searchMatrix(self, matrix, target):
        """
        从左下角或右下角开始
        :param matrix:
        :param target:
        :return:
        """
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])  # 行 列
        row, col = rows - 1, 0
        while row >= 0 and col < cols:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1

        return False


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    result = s.searchMatrix(matrix, target)
    print(result)