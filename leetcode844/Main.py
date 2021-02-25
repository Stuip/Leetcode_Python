class Solution:
    def backspaceCompare(self, S, T):
        S, T = list(S), list(T)
        if self.delete_i(S) != self.delete_i(T):
            return False
        return True

    def delete_i(self,arr):
        stack = list()
        for c in arr:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return "".join(stack)


if __name__ == '__main__':
    s = Solution()
    S , T ="ab##", "c#d#"
    result = s.backspaceCompare(S, T)
    print(result)
