class Solution:
    def convertToTitle(self, n: int) -> str:
        stack = list()
        mapping = dict()
        for i in range(0, 26):
            mapping[i] = chr(i+ord("A"))
        while n:
            n -= 1   # 需要规范化 因为26进制 需要从0-26开始
            stack.append(n % 26)
            n //= 26
        for i in range(len(stack)):
            stack[i] = mapping[stack[i]]
        return "".join(stack[::-1])


if __name__ == '__main__':
    s = Solution()
    n = 701
    result = s.convertToTitle(n)
    print(result)