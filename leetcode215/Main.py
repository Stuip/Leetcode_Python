def sortedSquares(nums):
    # return sorted([value ** 2 for value in nums])
    n = len(nums)
    ans = [0] * n
    i, j, pos = 0, n - 1, 0
    while i <= j:
        num1, num2 = nums[i] ** 2, nums[j] ** 2
        if num1 < num2:  # 将两者最小优先放入数组中
            ans[pos] = num1
            i += 1
        else:
            ans[pos] = num2
            j -= 1
        pos += 1
    return ans

nums = [-4,-1,0,3,10]
ans = sortedSquares(nums)
print(ans)


