class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = list(str(x))
        i, j = 0, len(stack) - 1
        while i <= j:
            if stack[i]!= stack[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    x = 10
    result = s.isPalindrome(x)
    print(result)