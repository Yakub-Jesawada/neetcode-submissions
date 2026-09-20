class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        for i in range(n):
            if i == 0:
                left_max[i] = height[i]
            else:
                left_max[i] = max(left_max[i-1],height[i])
        for j in reversed(range(n)):
            if j == n-1:
                right_max[j] = height[j]
            else:
                right_max[j] = max(right_max[j+1],height[j])
        for x in range(n):
            if x == 0:
                continue
            if x == n-1:
                continue
            water += min(left_max[x], right_max[x]) - height[x]
        return water