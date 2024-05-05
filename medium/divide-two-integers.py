class Solution:
    def divide(self, dividend: int, divisor: int) -> int:     
        sign_dd = False if dividend < 0 else True
        sign_dv = False if divisor < 0 else True
        if divisor == 1:
            return dividend if dividend >= -2147483648 else -2147483648
        elif divisor == -1:
            return -dividend if -dividend < 2147483648 else 2147483647
        elif divisor == dividend:
            return 1
        elif divisor + dividend == 0:
            return -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        i = 1
        while dividend - divisor >= 0:
            if divisor**(i+1) > dividend:
                res += divisor**(i-1)
                dividend -= divisor**i
                i = 1
            else:
                i += 1
        if sign_dd == sign_dv:
            return res
        else:
            return -res
