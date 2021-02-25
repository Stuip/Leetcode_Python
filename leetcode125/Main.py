class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())
        stack = list()
        for c in s:
            if 'a' <= c <= 'z' or "0" <= c <= "9":
                stack.append(c)
        i, j = 0, len(stack)-1
        while i <= j:
            if stack[i] != stack[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    string = "0P"
    result = s.isPalindrome(string)
    print(result)