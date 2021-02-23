class Solution:
    def sumOddLengthSubarrays(self, arr):
        total = 0
        for i in range(1,len(arr)+1,2):
            for index in range(len(arr)):
                if len(arr) - index >= i:
                    total += sum(arr[index:index+i])
        return total


if __name__ == '__main__':
    s = Solution()
    arr = [1, 4, 2, 5, 3]
    result = s.sumOddLengthSubarrays(arr)
    print(result)