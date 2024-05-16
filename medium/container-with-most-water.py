class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
        lb, ub = 0, -1
        distance = len(height) - 1
        max_area = distance * min(height[lb], height[ub])
        while lb - ub < len(height):
            if height[lb] < height[ub]:
                lb += 1
            else:
                ub -= 1
            distance -= 1
            if distance * min(height[lb], height[ub]) > max_area:
                max_area = distance * min(height[lb], height[ub])
        return max_area
