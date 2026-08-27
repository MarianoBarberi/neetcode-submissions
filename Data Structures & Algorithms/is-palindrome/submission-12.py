class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 0:
            return True

        s2 = ""
        for char in s:
            if char.isalnum():
                s2 += char.lower()

        l = 0
        r = len(s2) - 1

        print(s2)
        while l < r:
            if s2[l] != s2[r]:
                return False
            l += 1
            r -= 1
        return True