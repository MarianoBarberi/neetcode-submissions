class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        res = 0
        while r != l:
            height = min(heights[l], heights[r])
            width = r - l
            res = max(res, height * width)
            if heights[r] == height:
                r -= 1
            elif heights[l] == height:
                l += 1
        return res