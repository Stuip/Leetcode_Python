class Solution:
    def hammingDistance(self, x, y):
        x, y = list(bin(x))[2:], list(bin(y))[2:]
        if len(x) > len(y):
            num = len(x) - len(y)
            y = ["0"] * num + y
        else:
            num = len(y) - len(x)
            x = ["0"] * num + x
        res = 0
        for index in range(len(x)):
            if x[index] != y[index]:
                res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    x, y = 1, 4
    result = s.hammingDistance(x,y)
    print(result)