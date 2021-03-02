class Solution:
    def getNoZeroIntegers(self, n):
        for i in range(1,n):
            if self.haveNozero(n-i) and self.haveNozero(i):
                return [i, n-i]

    def haveNozero(self, num):
        num = list(str(num))
        for value in num:
            if value == "0":
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    result = s.getNoZeroIntegers(n=4102)
    print(result)
