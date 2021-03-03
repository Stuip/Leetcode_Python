class Solution:
    def frequencySort(self, nums):
        return sorted(nums, key=lambda x: (nums.count(x), -x))


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,1,3,2]
    result = s.frequencySort(nums)
    print(result)