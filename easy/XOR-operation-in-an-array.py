class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = (start+2*i for i in list(range(n)))
        return reduce(lambda x,y: x^y, nums)
