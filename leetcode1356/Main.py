class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key = lambda x: (bin(x).count("1"), x))


if __name__ == '__main__':
     s = Solution()
     arr = [1024,512,256,128,64,32,16,8,4,2,1]
     result = s.sortByBits(arr)
     print(result)