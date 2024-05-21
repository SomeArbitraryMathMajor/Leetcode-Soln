class Solution:
    import math
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return 2*a
        if a == -b:
            return 0
        while b & 0xffffffff != 0:
            c = (a & b) << 1
            a = a ^ b
            b = c
        if b > 0:
            return a & 0xffffffff
        return a
