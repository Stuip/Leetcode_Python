class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = [(sum(mat[i]), i) for i in range(len(mat))]
        ans.sort()
        return [value[1] for value in ans[:k]]