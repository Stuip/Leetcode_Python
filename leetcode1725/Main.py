class Solution:
    def countGoodRectangles(self, rectangles):
        num, res =0, list()
        for rectangle in rectangles:
            length= min(rectangle)
            res.append(length)
        for r in res:
            if r == max(res):
                num += 1
        return num


if __name__ == '__main__':
    s = Solution()
    rectangles = [[2,3],[3,7],[4,3],[3,7]]
    result = s.countGoodRectangles(rectangles)
    print(result)
