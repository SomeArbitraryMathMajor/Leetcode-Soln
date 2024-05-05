class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        d1 = (mat[i][i] for i in range(len(mat)))
        d2 = (mat[i][-1-i] for i in range(len(mat)))
        if len(mat) % 2 == 0:
            return sum(d1)+sum(d2)
        else:
            val = list(d1)
            return sum(val)+sum(d2)-val[int((len(mat)-1)/2)]
