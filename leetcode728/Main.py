class Solution:
    def selfDividingNumbers(self, left, right):
        res = []
        for i in range(left, right+1):
            if self.isDiv(i):
                res.append(i)
        return res

    def isDiv(self, num):
        arr = list(str(num))
        if '0' in arr:
            return False
        for v in arr:
            if v != '0' and num % int(v) != 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    left, right = 1, 22
    result = s.selfDividingNumbers(left, right)
    print(result)

