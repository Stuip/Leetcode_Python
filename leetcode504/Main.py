class Solution:
    def convertToBase7(self, num):
        stack = list()
        if num == 0:
            return str(num)
        s = num
        num = abs(num)
        while num:
            stack.append(str(num % 7))
            num //= 7
        if s < 0:
            return "-" + "".join(stack[::-1])
        return "".join(stack[::-1])


if __name__ == '__main__':
    s = Solution()
    num = 7
    result = s.convertToBase7(num)
    print(result)