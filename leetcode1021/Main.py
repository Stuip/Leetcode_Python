class Solution:
    def removeOuterParentheses(self, S):
        """
        借助栈来判断，把非外层括号放进答案中。
        怎么判断非外层括号？
            1, 左括号加入前，栈不为空
            2, 右括号加入并消括号后，栈不为空
        """
        res, stack = "", list()
        for c in S:
            if c == "(":
                if stack:  # 内层左括号
                    res += c
                stack.append("(")     # 左括号
            if c == ")":
                stack.pop()   # 弹出栈顶左括号
                if stack:
                    res += c
        return res


if __name__ == '__main__':
    s = Solution()
    result = s.removeOuterParentheses("(()())(())")
    print(result)