def distributeCandies(candyType):
    mapping = dict()   # 键值对：类型-个数
    for value in candyType:
        if value not in mapping:
            mapping[value] = 1
        else:
            mapping[value] += 1
    print(mapping)
    index = len(candyType) // 2
    print(index)
    k = 0
    for num in mapping.values():
        if num > 0 and index > 0:
            index -= 1
            k += 1
    return k

candyType = [0,0,0,4]
ans = distributeCandies(candyType)
print(ans)
