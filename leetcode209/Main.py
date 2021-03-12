class Solution:
    def minSubArrayLen(self, target, nums):
        if not nums:
            return 0
        left, res, total = 0, len(nums), 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, (right - left + 1))
                total -= nums[left]
                left += 1
        return 0 if res == len(nums) else res


if __name__ == '__main__':
    s = Solution()
    target = 7
    nums = [2,3,1,2,4,3]
    result = s.minSubArrayLen(target, nums)
    print(result)