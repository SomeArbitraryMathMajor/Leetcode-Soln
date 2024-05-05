class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recPow(a, b):
            if a == 1 or b == 0:
                return 1
            if b < 0:
                return 1/recPow(a, -b)
            return recPow(a**2, b//2)*a if b & 1 else recPow(a*a, b//2)
        return recPow(x, n)
