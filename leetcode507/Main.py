class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """ 时间超时 """
        stack = list()
        for i in range(1,num):
            d1 = num / i
            d2 = num // i
            if d1 == d2:
                stack.append(i)
            if sum(stack) > num:
                return False
        if sum(stack) == num:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    num = 30402457
    result = s.checkPerfectNumber(num)
    print(result)