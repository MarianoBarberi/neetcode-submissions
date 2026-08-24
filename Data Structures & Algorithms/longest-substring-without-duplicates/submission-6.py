class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        stack = []
        while r <= len(s) - 1:
            while s[r] in stack:
                stack.pop(0)
                l += 1
            stack.append(s[r])
            r += 1
            res = max(res, r - l)
        return res