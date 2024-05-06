class Solution:
    def mySqrt(self, x: int) -> int:
        lb, ub = 0, x
        while lb - ub <= 0:
            mid = (lb + ub)//2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                ub = mid - 1
            else:
                lb = mid + 1
        return ub
