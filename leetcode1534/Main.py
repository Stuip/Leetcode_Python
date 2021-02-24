class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        cnt = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        cnt += 1
        return cnt



if __name__ == '__main__':
    s = Solution()
    arr = [3, 0, 1, 1, 9, 7]
    a, b, c = 7, 2, 3
    result = s.countGoodTriplets(arr, a, b, c)
    print(result)
