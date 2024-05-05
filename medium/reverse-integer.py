class Solution:
    import math
    def reverse(self, x: int) -> int:
        out = int(math.copysign(int(str(abs(x))[::-1]), x))
        return out if (out >> 31) == 0 or (out >> 31) == -1 else 0
