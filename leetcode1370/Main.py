class Solution:
    def sortString(self, s):
        nums = [0]*26
        result = list()
        for c in s:
            nums[ord(c) - ord('a')] += 1
        while sum(nums) > 0:
            for i in range(len(nums)):
                if nums[i] > 0:
                    ch = chr(i+ord('a'))
                    result.append(ch)
                    nums[i] -= 1
            for j in reversed(range(len(nums))):
                if nums[j] > 0:
                    ch = chr(j+ord('a'))
                    result.append(ch)
                    nums[j] -= 1
        return "".join(result)


if __name__ == '__main__':
    s = Solution()
    string = "leetcode"
    result = s.sortString(string)
    print(result)
