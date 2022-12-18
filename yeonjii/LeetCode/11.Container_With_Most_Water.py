class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 브루트포스로 풀면 O(N^2)
        left = 0
        right = len(height)-1
        max_width = 0
        while right > left:
            max_width = max(max_width, (right-left)*min(height[right],height[left]))
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_width
