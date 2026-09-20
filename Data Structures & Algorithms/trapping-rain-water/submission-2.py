class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        for i in range(n):
            if i == 0:
                left_max[i] = height[i]
                continue
            left_max[i] = max(left_max[i-1], height[i])
        for j in reversed(range(n)):
            if j == n-1:
                right_max[j] = height[j]
                continue
            right_max[j] = max(right_max[j+1], height[j])
        for x in range(n):
            water += min(right_max[x], left_max[x]) - height[x]
        return water
