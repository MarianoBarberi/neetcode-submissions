class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        stack = set()
        while r <= len(s) - 1:
            while s[r] in stack:
                stack.remove(s[l])
                l += 1
            stack.add(s[r])
            r += 1
            res = max(res, r - l)
        return res