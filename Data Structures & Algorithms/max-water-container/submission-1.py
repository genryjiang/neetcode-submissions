class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        a = 0
        # shrinking window
        while left < right:
            # movement options
            temp = min(heights[left], heights[right]) * (right-left)
            if temp > a:
                a = temp

            if heights[left] < heights[right]:
                # if the height of left is lower htan right, move left
                left += 1
            else:
                right -=1 # else, move right towards the left (diagram ref)
        return a