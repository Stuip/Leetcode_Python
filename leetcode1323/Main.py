class Solution:
    def maximum69Number (self, num: int) -> int:
        stack = list(str(num))
        for i in range(len(stack)):
            if stack[i] == "6":
                stack[i] = "9"
                break
        return int("".join(stack))


if __name__ == '__main__':
    s = Solution()
    num = 9999
    result = s.maximum69Number(num)
    print(result)