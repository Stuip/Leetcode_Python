class Solution:
    def maximumWealth(self, accounts):
        nums = list()
        for value in accounts:
            nums.append(sum(value))
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    accounts = [[1,2,3],[3,2,1]]
    s.maximumWealth(accounts)