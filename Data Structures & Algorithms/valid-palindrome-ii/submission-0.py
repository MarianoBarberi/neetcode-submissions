class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        skipped = False
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif not skipped:
                skipped = True
                if s[l] == s[r - 1]:
                    r -= 1
                else:
                    l += 1
            else:
                return False
        return True