class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        num = max(candies)
        # isTrue = [False] * len(candies)
        for index in range(len(candies)):
            if (candies[index] + extraCandies) >= num:
                candies[index] = True
            else:
                candies[index] = False
        return candies


if __name__ == '__main__':
    s = Solution()
    result = s.kidsWithCandies(candies=[2,3,5,1,3], extraCandies=3)
    print(result)
