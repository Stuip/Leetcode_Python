class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2*i for i in range(n)]
        num = nums[0]
        for index in range(1, len(nums)):
            num ^= nums[index]
        return num




if __name__ == '__main__':
    s = Solution()
    result = s.xorOperation(4,3)
    print(result)
