class Solution:
    def sortArrayByParityII(self, A):
        even, odd = [], []
        for value in A:
            if value % 2 == 0:
                even.append(value)
            else:
                odd.append(value)
        i, j, k = 0, 0, 0
        while k < len(A):
            A[k] = even[i]
            i += 1
            k += 1
            A[k] = odd[j]
            j += 1
            k += 1
        return A


if __name__ == '__main__':
    s = Solution()
    A = [4,1,2,1]
    result = s.sortArrayByParityII(A)
    print(result)