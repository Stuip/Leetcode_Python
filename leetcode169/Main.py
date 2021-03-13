class Solution:
    def majorityElement(self, nums: list) -> int:
        return self.getmajority(nums, 0, len(nums) - 1)

    def getmajority(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) >> 1
        leftmajor = self.getmajority(nums, left, mid)
        rightmajor = self.getmajority(nums, mid + 1, right)
        if leftmajor == rightmajor:  # 如果左右边的众数相等，则返回其中一个
            return leftmajor
        # 统计两者在合并的数组中，谁是众数
        leftcount = sum(1 for i in range(left, right + 1) if nums[i] == leftmajor)
        rightcount = sum(1 for j in range(left, right + 1) if nums[j] == rightmajor)
        return leftmajor if leftcount > rightcount else rightmajor


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 3]
    result = s.majorityElement(nums)
    print(result)
