class Solution:
    from itertools import combinations
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(range(1,n+1))] if k >= n else list(combinations(list(range(1,n+1)), k))
